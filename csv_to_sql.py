import pandas as pd
import sqlite3
import os


def import_file(filename, title):
    filepath = input("Enter the name of the csv file (MUST BE IN CURRENT DIRECTORY): ")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        conn = sqlite3.connect(filename)
        df.to_sql(title, conn, if_exists='replace', index=False)
        print("Your table was successfully created as 'table.db.")
        conn.close()
    else:
        if not os.path.exists(filepath):
            print("The directory or file is invalid. Please try again.")


print("Welcome! This program will convert a csv file into a SQL database.")

database_name = input("What do you want to name this file as? (MUST END IN '.db'): ")
database_title = input("What is the title of your database?: ")

import_file(database_name, database_title)







