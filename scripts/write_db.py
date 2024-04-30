# Script to write one entry into th DB using mongoDB locally
# this is just an example

import pymongo
import json
from pymongo import MongoClient, InsertOne
import os

client = pymongo.MongoClient("mongodb://127.0.0.1:27017") # Connect to local database

mydatabase = client['jsonDB'] # create new database
mycol = mydatabase['hex46'] # dict of type {'unique_id' : json_full_report}

path = os.path.expandvars('${MYROOT}')

jsonObj = json.load(open("%s/data/report_ECOND_2024-04-17_21-49-01.json"%path,'r'))
   
x = mycol.insert_one(jsonObj) # Write in DB

# Print written object

for obj in mydatabase['hex46'].find():
    print(obj)



