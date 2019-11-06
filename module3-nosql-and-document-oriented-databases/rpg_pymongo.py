"""
inserting rpg data into cluster database
"""

"""
There were 2 main differences between pymongo and PostgreSql that 
I felt while doing this. The first was the syntax, and the second 
was how each used strings. The PyMongo syntax does not feel good or
intuitive to me. Every time we wanted to find something we needed to 
add .test to our db object before calling the .find command and I don't
have a solid understanding of what's going on there, "why can't we just 
call the .find command on db?" I found myself asking all the time.

However, PostgreSQL in python is VERY string heavy. Inputting commands as
strings, then running the code and having to fix errors and typoes in 
strings is also not fun. So, while I find the syntax of the data entry in 
Sql a bit more intuitive, the debugging of commands and data entree in 
PyMongo felt much cleaner and nicer. I got today's assignment debugged and 
running as intended much, much faster that yesterdays mostly due to the fact
that today our data entree was in libaries and dictionaries, and not a huge
multiple line long string.
"""


import pymongo
import json

client = pymongo.MongoClient("mongodb://admin:HemG8m35dwrcsJtY@cluster0-shard-00-00-q6cbk.mongodb.net:27017,cluster0-shard-00-01-q6cbk.mongodb.net:27017,cluster0-shard-00-02-q6cbk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.rpg

# get the the data from rpg.json into a dictionary
rpg_file = open('rpg.json')
rpg_str = rpg_file.read()
rpg_data = json.loads(rpg_str)[0:]

# insert the json data into the database
db.rpg.insert_many(rpg_data)

print(list(db.rpg.find()))