import pandas as pd
import sqlite3
import os


def import_file():
    filepath = input("Enter the name of the csv file (MUST BE IN CURRENT DIRECTORY): ")
    if os.path.exists(filepath):
        df = pd.read_csv(filepath)
        conn = sqlite3.connect('table.db')
        df.to_sql('my table', conn, if_exists='replace', index=False)
        print("Your table was successfully created as 'table.db.")
        conn.close()
    else:
        if not os.path.exists(filepath):
            print("The directory or file is invalid. Please try again.")

import_file()







