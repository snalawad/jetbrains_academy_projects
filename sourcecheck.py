import argparse
import os
import re

# Accepting arguments for source_directory, my_sql connection details and table name to update the MySQL entries to

parser = argparse.ArgumentParser(
    description='Utility to update MySQL tables on remote host')

parser.add_argument('-s', '--source_dir', help='Enter Path For CSV File')


#parser.add_argument('-sql', '--mysql_details', help='Enter path to MySql connection details')
#parser.add_argument('-dest', '--destination_table', help='Enter the name of table to be updated')

args = parser.parse_args()

# unction to iterate through the source_directory and read only CSV files and append them to files_in_dir dictionary

files_in_dir = { key:0
                 for key in os.listdir(args.source_dir)
                    if os.path.abspath(key).endswith(".csv")}


print('Following are the files present in the given directory', files_in_dir)

for file in files_in_dir:
    print(file)

