"""
code to try to upload the titanic.csv to elaphantsql as a 
sql table
"""

""" imports """
import pandas as pd
import sqlite3 as sql
import os
import psycopg2

"""Personal Info"""
""" DELETE ME """



"""Create connection to elephantsql and create cursor """
pg_conn = psycopg2.connect(dbname=dbname, 
                        user=user, 
                        password=password, 
                        host=host)
pg_curs = pg_conn.cursor()


""" making the titanic.csv into a sql table"""
""" file path """
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "titanic.csv")

""" reading in titanic csv """
df = pd.read_csv(db_path)
""" removing troublesome apostrophes from names"""
df['Name'] = df['Name'].str.replace("'","")

""" creating connection to new, blank sqlite3 database file """
conn = sql.connect("titanic.sqlite3")

""" fill the new, blank sqlite3 file with data from titanic.csv """
df.to_sql(name='titanic', con=conn)

""" create connection and cursor to titanic.sqlite3 in sql """
sl_conn = sql.connect('titanic.sqlite3')
sl_curs = sl_conn.cursor()

sl_curs.execute('PRAGMA table_info(titanic);')

""" create empty table in elaphantsql """
create_titanic_table = """
    CREATE TABLE titanic (
        id SERIAL PRIMARY KEY,
        survived INT,
        class INT,
        name VARCHAR,
        sex VARCHAR,
        age INT,
        num_sibling_spouce_aboard INT,
        num_parents_children_aboard INT,
        fare FLOAT
    );
    
"""
pg_curs.execute(create_titanic_table)

""" fill table in elephantsql """
passengers = sl_curs.execute('SELECT * FROM titanic;').fetchall()
# print(passengers)
# count = 0
for passenger in passengers:
    insert_passenger = """
        INSERT INTO titanic
        (survived, class, name, sex, age, 
        num_sibling_spouce_aboard, 
        num_parents_children_aboard, 
        fare)
        VALUES """ + str(passenger[1:]) + """;"""
    # count += 1
    # print(passengers[1:])
    pg_curs.execute(insert_passenger)
# print(count)
pg_curs.close()
pg_conn.commit()