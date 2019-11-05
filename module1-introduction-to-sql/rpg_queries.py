"""
Some test code to see if I understand 
how to work with SQL in python
"""


""" necessary imports """
import sqlite3 as sql
import os.path


""" connect the database to python"""
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "rpg_db.sqlite3")
conn = sql.connect(db_path)

""" create cursor 
we only need to close and commit a cursor 
if we change the database in some way
"""
curs = conn.cursor()

""" unique number of characters """
query = 'SELECT COUNT(character_id) FROM charactercreator_character;'
answer = curs.execute(query).fetchone()[0]
total_char = answer
print(f"Number of unique Characters: {answer}")


""" number of each class """
query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_mage;'
answer = curs.execute(query).fetchone()[0]
print(f"Number of mages: {answer}")

query = 'SELECT COUNT(mage_ptr_id) FROM charactercreator_necromancer;'
answer = curs.execute(query).fetchone()[0]
print(f"Number of necromancers: {answer}")

query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_thief;'
answer = curs.execute(query).fetchone()[0]
print(f"Number of thieves: {answer}")

query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_cleric;'
answer = curs.execute(query).fetchone()[0]
print(f"Number of clerics: {answer}")

query = 'SELECT COUNT(character_ptr_id) FROM charactercreator_fighter;'
answer = curs.execute(query).fetchone()[0]
print(f"Number of fighters: {answer}")


""" total number of items """
query = ('SELECT COUNT(name) FROM armory_item '
        'INNER JOIN charactercreator_character_inventory '
        'ON armory_item.item_id = charactercreator_character_inventory.item_id;')
answer = curs.execute(query).fetchone()[0]
total_items = answer
print(f"Total number of items amongst all characters: {answer}")

""" total number of weapons""" 
query = ('SELECT COUNT(name) FROM armory_item '
        'INNER JOIN charactercreator_character_inventory '
        'ON armory_item.item_id = charactercreator_character_inventory.item_id '
        'INNER JOIN armory_weapon ON armory_weapon.item_ptr_id = armory_item.item_id;')
answer = curs.execute(query).fetchone()[0]
total_weap = answer
print(f"Total number of weapons amongst all characters: {answer}")

""" total non-weapons """
total_non_weap = total_items - total_weap
print(f"Total number of non_weapons amongst all characters: {total_non_weap}")

""" total items in each inventory """
query = ('SELECT charactercreator_character.name, COUNT(item_id) '
        'FROM charactercreator_character_inventory '
        'INNER JOIN charactercreator_character '
        'ON charactercreator_character.character_id = '
        'charactercreator_character_inventory.character_id '
        'GROUP BY charactercreator_character.name;')
answer = curs.execute(query).fetchmany(20)
print(f"Total number of items in each character's inventory: {answer}")

""" total weapons in each inventory """
query = ('SELECT charactercreator_character.name, '
        'COUNT(armory_item.item_id) '
        'FROM charactercreator_character_inventory '
        'INNER JOIN charactercreator_character '
        'ON charactercreator_character.character_id = '
        'charactercreator_character_inventory.character_id '
        'INNER JOIN armory_item '
        'ON armory_item.item_id = '
        'charactercreator_character_inventory.item_id '
        'INNER JOIN armory_weapon '
        'ON armory_item.item_id = armory_weapon.item_ptr_id '
        'GROUP BY charactercreator_character.name;')
answer = curs.execute(query).fetchmany(20)
print(f"Total number of weapons in each character's inventory: {answer}")

""" Averages amongst characters """
""" avg items per character """
print(f"Average items per character: {total_items/total_char}")

""" avg weapons per character """
print(f"Average weapons per character: {total_weap/total_char}")
