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
dbname = 'izonavft'
user = 'izonavft'
password = 'rnkuz1Hs8I7ccy3uLCmaONWEfkb8908B'
host = 'salt.db.elephantsql.com'

"""Create connection to elephantsql and create cursor """
pg_conn = psycopg2.connect(dbname=dbname, 
                        user=user, 
                        password=password, 
                        host=host)
pg_curs = pg_conn.cursor()


# """


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
# pg_curs.execute(create_titanic_table)

""" fill table in elephantsql """
""" only execute once, for the first time through set  
data_in = True, after one run through, set data_in = False """
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


# """


pg_conn = psycopg2.connect(dbname=dbname, 
                        user=user, 
                        password=password, 
                        host=host)
pg_curs = pg_conn.cursor()


""" test """
string = 'SELECT * FROM titanic'
print(pg_curs.execute(string).fetchall() )

""" survivors """
string = "SELECT COUNT(Name) as survivors FROM titanic WHERE Survived = 1;"
print(pg_curs.execute(string))
""" non-survivors """
string = "SELECT COUNT(Name) as died FROM titanic WHERE Survived = 0;"
print(pg_curs.execute(string).fetchall())

""" people per class"""
string = "SELECT Pclass, COUNT(Name) as num_in_class FROM titanic GROUP BY Pclass;"
print(pg_curs.execute(string).fetchall())
""" deaths by class"""
string = "SELECT Pclass, COUNT(Name) as died FROM titanic WHERE Survived = 0 GROUP BY Pclass;"
print(pg_curs.execute(string).fetchall())
""" survived by class """
string = "SELECT Pclass, COUNT(Name) as survived FROM titanic WHERE Survived = 1 GROUP BY Pclass;"
print(pg_curs.execute(string).fetchall())

""" average age of survivors """
string = "SELECT AVG(Age) as avg_age FROM titanic WHERE Survived = 1;"
print(pg_curs.execute(string).fetchall())
""" average age of deceased """
string = "SELECT AVG(Age) as avg_age FROM titanic WHERE Survived = 0;"
print(pg_curs.execute(string).fetchall())

""" age per class"""
string = "SELECT Pclass, AVG(Age) as avg_age FROM titanic GROUPY BY Pclass"
print(pg_curs.execute(string).fetchall())

""" avg fare per class """
string = "SELECT Pclass, AVG(Fare) as avg_fare FROM titanic GROUP BY Pclass"
print(pg_curs.execute(string).fetchall())

""" avg fare per survival """
string = "SELECT Survived, AVG(Fare) as avg_fare FROM titanic GROUP BY Survived"
print(pg_curs.execute(string).fetchall())

""" avg sib/spouse aboard by class"""
string = "SELECT Pclass, AVG(num_Sibling_Spouce_Aboard) as avg_sib_sp FROM titanic GROUP BY Pclass"
print(pg_curs.execute(string).fetchall())

""" avg sib/spouse aboard by survival """
string = "SELECT Survived, AVG(num_Sibling_Spouce_Aboard) as avg_sib_sp FROM titanic GROUP BY Survived"
print(pg_curs.execute(string).fetchall())

""" avg parent/children aboard by class """
string = "SELECT Pclass, AVG(num_Parents_Children_Aboard) as avg_par_child FROM titanic GROUP BY Pclass"
print(pg_curs.execute(string).fetchall())

""" avg parent/children aboard by survival """
string = "SELECT Survived, AVG(num_Parents_Children_Aboard) as avg_par_child FROM titanic GROUP BY Survived"
print(pg_curs.execute(string).fetchall())

""" check for duplicate names """
string = "SELECT Name, COUNT(Name) FROM titanic GROUP BY Name"
print(pg_curs.execute(string).fetchall())
