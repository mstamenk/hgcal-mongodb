# hgcal-mongodb
MongoDB instruction and implementation for HGCAL ECON testing

## Requirements
MongoDB is a databased using BSON (binary JSON) and can simply convert JSON elements into a data and be read using python via `pymongo`.

Need to install MongoDB binaries to be able to create a local data base. See instructions [here](https://www.prisma.io/dataguide/mongodb/setting-up-a-local-mongodb-database#setting-up-mongodb-on-macos). 

Once the `mongod` command ran, the rest of the tutorial requires the `mongosh` for command line shell type of interactions with the database. The instructions can be found [here](https://www.mongodb.com/docs/mongodb-shell/install/), however the database can also be fully accessed via python. 

The python requirement is `pymongo` and needs to be installed via pip:

```
python -m pip install pymongo
```

## Starting the MongoDB local server

```
mongod --dbpath /usr/local/var/mongodb --logpath /usr/local/var/log/mongodb/mongo.log --fork
```


## Writing in the database and accessing it

A small script is shown to access and write in the data base using some json files. 

```
# Setup environment
source setup.sh

python scripts/write_db.py 
```



