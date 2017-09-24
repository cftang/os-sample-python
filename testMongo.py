""" An example of how to insert a document """
import sys
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

def save2mongo(dbname,collection,doc):
    try:
        #c = Connection(host="localhost", port=27017)
        #c = MongoClient()
        c =MongoClient(
            "mongodb://user1:password1@localhost:27017/"+dbname)
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