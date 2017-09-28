""" An example of how to insert a document """
import os
import sys
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def save2mongo(dbname,collection,doc):
    try:
        hostname = os.getenv('HOSTNAME')
        if hostname:
            c = MongoClient("mongodb://db1:user1@ds155684.mlab.com:55684/baidu")
            print("cloud")
        else:
            c = MongoClient("mongodb://user1:password1@localhost:27017/" + dbname)
            print("local")
    except ConnectionFailure as e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    dbh = c[dbname]
    dbh[collection].insert(doc)
    print ("Successfully inserted document: %s" % doc)

def main():
    user_doc = {
    "username" : "janedoe",
    "firstname" : "Jane",
    "surname" : "Doe",
    "dateofbirth" : datetime(1975, 1, 1),
    "email" : "janedoe74@example.com",
    "score" : 0
    }
    save2mongo('baidu','mycoll', user_doc)

if __name__ == "__main__":
    main()