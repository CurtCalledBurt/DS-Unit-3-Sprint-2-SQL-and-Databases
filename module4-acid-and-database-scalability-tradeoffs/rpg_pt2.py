import pymongo
import json

client = pymongo.MongoClient("mongodb://admin:HemG8m35dwrcsJtY@cluster0-shard-00-00-q6cbk.mongodb.net:27017,cluster0-shard-00-01-q6cbk.mongodb.net:27017,cluster0-shard-00-02-q6cbk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster0-shard-0&authSource=admin&retryWrites=true&w=majority")
db = client.rpg

# get the the data from rpg.json into a dictionary
rpg_file = open('rpg copy.json')
rpg_str = rpg_file.read()
rpg_data = json.loads(rpg_str)[0:]


# insert the json data into the database
# set data_in to False to add the data to the MongoDB 
# collection, after running the program once set 
# data_in to True to prevent duplicates.
data_in = True
if data_in == False:
    db.rpg.insert_many(rpg_data)

#num of chars
print('Number of characters: ', len(list(db.rpg.find({"model": "charactercreator.character"}))))
#num fighters
print('Number of fighters: ', len(list(db.rpg.find({"model": "charactercreator.fighter"}))))
#num mages
print('Number of mages: ', len(list(db.rpg.find({"model": "charactercreator.mage"}))))
#num thieves
print('Number of thieves: ', len(list(db.rpg.find({"model": "charactercreator.thief"}))))
#num clerics
print('Number of clerics: ', len(list(db.rpg.find({"model": "charactercreator.cleric"}))))
#num necromancers
print('Number of necromancers: ', len(list(db.rpg.find({"model": "charactercreator.necromancer"}))))

#number of item and weapon options
print('Number of non-weapon item choices (not total): ', len(list(db.rpg.find({"model": "armory.item"}))))
print('Number of weapon choices (not total): ', len(list(db.rpg.find({"model": "armory.weapon"}))))

# total weapons and items across all inventories, under construction
# db.rpg.find({"model": "charactercreator.character"}).aggregate({"$project": {"NumberOfItemsInArray": {"$size": "$inventory"}}})
# db.rpg.find({"model": "charactercreator.character"}).inventory.length

# print(db.rpg.aggregate({ "InventorySize": {"$size": "$inventory" } }))

# print(db.rpg.aggregate([{"$project": {"inventory_size": {"$size": "$inventory"}}}]))

# print(db.rpg.aggregate([{"$project": {"inventory_size": {"$size": {"fields": "inventory"}}}}]))
