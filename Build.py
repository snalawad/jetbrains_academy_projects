import os
import sys
import configparser
import argparse
import time
import logging
import boto3
from botocore.exceptions import ClientError
import os


# python3 Build.py --config /home/prashant/PycharmProjects/AutoDQLambda_Deploy/deploy.properties
class BuildAutoDQ():
    def __init__(self, automationPath, buildPath, bitbucketBranch, bitbucketUsername, bitbucketPassword, awsAccessKeyId,
                 awsSecretAccessKey, awsRegion, bucketName):
        self.automationPath = automationPath
        self.buildPath = buildPath
        self.bitbucketBranch = bitbucketBranch
        self.bitbucketUsername = bitbucketUsername
        self.bitbucketPassword = bitbucketPassword
        self.awsAccessKeyId = awsAccessKeyId
        self.awsSecretAccessKey = awsSecretAccessKey
        self.awsRegion = awsRegion
        self.bucketName = bucketName

    # To Create Lambda function Build
    def BuildLambda(self):
        cloneUrl = "git clone -b " + bitbucketBranch + " https://" + bitbucketUsername + ":" + bitbucketPassword + "@bitbucket.org/dataeaze/auto_dq.git"
        print(cloneUrl)

        # path to the working directory
        os.chdir(self.automationPath)

        # clone develop branch
        os.system(cloneUrl)

        # create lambda Build
        os.chdir("auto_dq/dq_manage")
        os.system("zip -r9 autoDQLambda.zip *")
        currentPath = os.getcwd()
        lambdaBuildPath = str(currentPath) + "/" + "autoDQLambda.zip"
        print(lambdaBuildPath)
        self.copyTOS3(awsAccessKeyId, awsSecretAccessKey, awsRegion, automationPath, bucketName, buildPath)

        copy = "cp " + lambdaBuildPath + " " + buildPath
        os.popen(copy)
        print("Lambda Build created successfully")

    # to Create and Copy  dq_manage Build to S3
    def copyTOS3(self, awsAccessKeyId, awsSecretAccessKey, awsRegion, automationPath, bucketName, buildPath,
                 object_name=None):
        # path to the working directory
        os.chdir(automationPath)

        # create lambda dq_manage Build
        os.chdir("auto_dq")
        os.system("zip -r9 autoDQ.zip *")
        currentPath = os.getcwd()
        autoDqBuildPath = str(currentPath) + "/" + "autoDQ.zip"
        print("autoDqBuildPath:", autoDqBuildPath)
        copy = "cp " + autoDqBuildPath + " " + buildPath
        os.popen(copy)
        print("autoDQ Build created successfully")

        if object_name is None:
            object_name = os.path.basename(autoDqBuildPath)

            print("obeject_name:", object_name)

        # Upload the file
        session = boto3.Session(
            aws_access_key_id=awsAccessKeyId, aws_secret_access_key=awsSecretAccessKey)
        print(session)
        s3_client = session.client('s3')
        print("s3_client", s3_client)
        try:
            response = s3_client.upload_file(autoDqBuildPath, bucketName, object_name)
            print("Response:", response)
        except ClientError as e:
            logging.error(e)
            return False
        return True

    # To Create automation script Build
    def BuildAutomation(self):
        os.chdir(self.automationPath)
        os.chdir("auto_dq/scripts")
        os.system("zip -r9 AutomationBuild.zip *")
        currentPath = os.getcwd()
        automationBuildPath = str(currentPath) + "/" + "AutomationBuild.zip"
        print(automationBuildPath)
        copy = "cp " + automationBuildPath + " " + self.buildPath
        os.popen(copy)
        print("Automation Build Created successfully")

    # To create UI Build
    def BuildUI(self):
        cloneUrl = "git clone -b " + bitbucketBranch + " https://" + bitbucketUsername + ":" + bitbucketPassword + "@bitbucket.org/dataeaze/autodq_ui.git"
        print(cloneUrl)

        os.chdir(self.automationPath)
        os.system(cloneUrl)

        os.chdir("autodq_ui")
        os.system("zip -r9 UIBuild.zip *")
        currentPath = os.getcwd()
        UIBuildPath = str(currentPath) + "/" + "UIBuild.zip"
        print(UIBuildPath)
        os.chdir(automationPath)
        copy = "cp " + UIBuildPath + " " + self.buildPath
        os.popen(copy)
        print("UI Build Created successfully")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Provide arguments to deploy services")
    parser.add_argument("-c",
                        "--config",
                        required=True,
                        help="Please provide config file path")
    args = vars(parser.parse_args())
    if args['config']:
        configPath = args['config']
        print(configPath)
        config = configparser.ConfigParser()
        config.read(configPath)
        automationPath = config.get('prop Config', 'automationPath')
        buildPath = config.get('prop Config', 'buildPath')
        bitbucketBranch = config.get('prop Config', 'bitbucketBranch')
        bitbucketUsername = config.get('prop Config', 'bitbucketUsername')
        bitbucketPassword = config.get('prop Config', 'bitbucketPassword')
        awsAccessKeyId = config.get('prop Config', 'awsAccessKeyId')
        awsSecretAccessKey = config.get('prop Config', 'awsSecretAccessKey')
        awsRegion = config.get('prop Config', 'awsRegion')
        bucketName = config.get('prop Config', 'bucketName')
        os.chdir(automationPath)
        os.system("rm -r -f " + automationPath + "/autodq_ui")
        os.system("rm -r -f " + automationPath + "/auto_dq")
        os.system("rm -r -f " + buildPath)
        os.mkdir(buildPath)
        # os.mkdir(buildPath + "/sbin")

        # calling methods
        Build = BuildAutoDQ(automationPath, buildPath, bitbucketBranch, bitbucketUsername, bitbucketPassword,
                            awsAccessKeyId, awsSecretAccessKey, awsRegion, bucketName)
        Build.BuildLambda()
        Build.BuildAutomation()
        Build.BuildUI()

        # Creating master tar.gz file
        print("Creating master tar.gz")
        time.sleep(5.0)
        os.chdir(buildPath)
        os.system("tar -czvf Build.tar.gz *.zip")
        print("Successfully created Build")

        # To Remove Clone Repo's
        # os.system("rm -r -f " + automationPath + "/autodq_ui")
        # os.system("rm -r -f " + automationPath + "/auto_dq")
        # os.system("rm -r -f " + automationPath + "/build/*.zip")

    else:
        print("Please provide the required arguments")
        exit()
