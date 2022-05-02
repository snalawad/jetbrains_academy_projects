import pandas as pd
from sqlalchemy import create_engine
import argparse
import os
import sys

engine = create_engine(
    'mysql+mysqlconnector://remote:Pass%40123@ec2-18-188-248-131.us-east-2.compute.amazonaws.com:3306/startup',
    echo=False)
# Accepting arguments for source_directory, my_sql connection details and table name to update the MySQL entries to

parser = argparse.ArgumentParser(
    description='Utility to update MySQL tables on remote host')

parser.add_argument('-s', '--source_dir', help='Enter Path For CSV File')
parser.add_argument('-sql','--mysql_details', help='Enter path to MySql connection details')
parser.add_argument('-dest','--destination_table', help='Enter the name of table to be updated')

args = parser.parse_args()


# Function to iterate through the source_directory and read only CSV files and append them to files_in_dir dictionary

files_in_dir = { key:0
                 for key in os.listdir(args.source_dir)
                    if os.path.abspath(key).endswith(".csv")}


print('Following are the files present in the given directory', files_in_dir)


data = pd.read_csv(source_dir)


# Empty dictionary to store list CSV files in directory
files_in_dir = {}

# Function to iterate through the source_directory and read only CSV files and append them to files_in_dir dictionary

if args.source_dir:
    for file in args.source_dir:

        if os.path.abspath(file.name).endswith('.csv'):
            files_in_dir[(os.path.abspath(file.name))] = 0

        else:
            print("The file %s is not a .csv file and it will be ignored" % (file.name))


try:
    data.to_sql(name='StartupData', con=engine, if_exists='replace', index=False)
    print('Records Updated')

except:
    print('Error connecting to the remote host')


