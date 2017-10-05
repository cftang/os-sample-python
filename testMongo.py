""" An example of how to insert a document """
import os
import sys
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from send import h1

def save2rabbitmq(doc):
    z = {'dt': doc['dt'],
         'traffic_condition': doc['result']['traffic_condition'],
         'duration': doc['result']['routes'][0]['steps'][4]['duration'],
         'traffic_condition4': doc['result']['routes'][0]['steps'][4]['traffic_condition'] }

    print (z)
    h1(z)

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
    save2rabbitmq(doc)

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
