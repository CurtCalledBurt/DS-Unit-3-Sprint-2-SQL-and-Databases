"""
code to experiment with pymongo databases

note, when running from terminal, enter the command as 
"python -m PyMongo_test" without the .py on the end. 
A .py on the end causes an error for some reason.
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

client = pymongo.MongoClient("mongodb://admin:HemG8m35dwrcsJtY@cluster0-shard-00-00-q6cbk.mongodb.net:27017,cluster0-shard-00-01-q6cbk.mongodb.net:27017,cluster0-shard-00-02-q6cbk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.test

# Count how many documents
db.test.count_documents({'x': 1})

# Insert document
db.test.insert_one({'x': 1})

# count documents again
db.test.count_documents({'x': 1})

# find a particular document
db.test.find_one({'x': 1})
db.test.find({'x': 1})

# create cursor
curs = db.test.find({'x': 1})

#see documents in cursor
list(curs)


#create docs to add to db
samantha_doc = {
    'favorite animal': ['Kokopo', 'Dog']
}

rosie_doc = {
    'favorite animal': 'Snake',
    'favorite color': 'Cyan'
}

amer_doc = {
    'favorite animal': 'Red Panda'
}

me_doc = {
    'favorite animal': 'Sparrow',
    'favorite color': 'Blue'
}

# insert docs into db
db.test.insert_many([samantha_doc, rosie_doc, amer_doc, me_doc])

# check that insert worked
# print(list(db.test.find()))

# Make a lot more documents
more_doc = []
for i in range(10):
  doc = {'even': i % 2 == 0}
  doc['value'] = i
  more_doc.append(doc)

# insert the newly made documents
db.test.insert_many(more_doc)

# get odd numbers
# print(list(db.test.find({'even': False})))

# get amer_doc by asking for favorite animal
# print(list(db.test.find({'favorite animal': 'Red Panda'})))

# update doc with value of 3 to 8
db.test.update_one({'value': 3}, 
                    {'$inc': {'value': 5}})

# update multiple docs, add 100 to all evens
db.test.update_many({'even': True},
                    {'$inc': {'value': 100}})

# check updates went okay
# print(list(db.test.find({'even': True})))

# delete unwanted column
db.test.delete_many({'even': False})

# check if deletion worked
# print(list(db.test.find()))

# make a tuple that we will later insert into db
rpg_character = (1, 'King Bobby', 10, 3, 0, 0, 0)

# wrap tuple into a dictionary so insert_one works
db.test.insert_one({'rpg_character': rpg_character})

# check if Bobby made it in
# print(list(db.test.find()))

# insert a doc of rpg stats from King Bobby
db.test.insert_one({
    'sql_id': rpg_character[0],
    'name': rpg_character[1],
    'hp': rpg_character[2],
    'level': rpg_character[3]
})

# check if the stats made it in
# print(list(db.test.find()))


# One final check to make sure everything we did worked,
# and we'll also comment out the other print commands 
# so that we'll have a less cluttered terminal output
print(list(db.test.find()))
