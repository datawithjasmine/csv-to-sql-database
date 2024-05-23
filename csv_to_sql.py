# CSV-TO-SQL CONVERSION PROGRAM created by JASMINE MITCHELL

#           This script takes csv files and convert them to a SQL Database and Table
#                                      --- COMMENTS ---

# 1. I IMPORTED THE FOLLOWING LIBRARIES
#    - Pandas: to create a DataFrame from the csv file and convert it into a table.
#    - SQLite3: to set up the SQL database from the DataFrame.
#    - OS: to check if the csv file exists.
import pandas as pd
import sqlite3
import os

# 2. The IMPORT_FILE function prompts the user for the name of the csv file
#    and checks to see if it exists. If it does, it will create a table and
#                   then set it up as a database file.
#    If the csv file does not exist in the current directory, then it will tell
#                          the user to try again.


def import_file(filename, title):
    filepath = input("Enter the name of the csv file (MUST BE IN CURRENT DIRECTORY): ")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        conn = sqlite3.connect(filename)
        df.to_sql(title, conn, if_exists='replace', index=False)
        print("Your table was successfully created!")
        conn.close()
    else:
        if not os.path.exists(filepath):
            print("The directory or file is invalid. Please try again.")

# 3. First, the program starts off with a welcome message. Then prompts the user
#      for a name to give the file. The user also has to give the table a name.
#     The function will then execute, making the file and the program will end.

print("Welcome! This program will convert a csv file into a table.")

database_name = input("What do you want to name this file as? (MUST END IN '.db'): ")
database_title = input("What is the title of your table? (NO SPACES! USE UNDERSCORES): ")

import_file(database_name, database_title)

print("-- END OF PROGRAM --")







