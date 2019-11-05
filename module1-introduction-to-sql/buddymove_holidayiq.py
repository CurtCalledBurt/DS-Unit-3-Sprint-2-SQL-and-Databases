""" part 2"""
import pandas as pd
import sqlite3 as sql
import os


""" file path """
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "buddymove_holidayiq.csv")

""" reading in csv and checking the shape and number of NaN's """
df = pd.read_csv(db_path)
print("Dataframe shape: ", df.shape)
print("Nulls in each column of dataframe:\n",df.isna().sum())


""" creating connection to new blank sqlite3 database file """
conn = sql.connect("buddymove_holidayiq.sqlite3")

""" fill new, blank sqlite db with data from buddymove_holidayiq.csv """
df.to_sql(name='buddymove_holidayiq', con=conn)

"""create cursor on new connection to buddymove """
curs = conn.cursor()

""" show number of rows by SQL query """
query = "SELECT COUNT('User Id') FROM buddymove_holidayiq;"
answer = curs.execute(query).fetchone()[0]
print(f"Number of Rows: {answer}")

query = ("SELECT COUNT('User Id') FROM buddymove_holidayiq "
        "WHERE Nature >= 100 AND Shopping >= 100 "
        "GROUP BY 'User Id';")
answer = curs.execute(query).fetchone()[0]
print(f"Number of Users with over 100 nature and shopping records: {answer}")