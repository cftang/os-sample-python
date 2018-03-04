""" An example of how to insert a document """
import os
import sys
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from bson.objectid import ObjectId
from copy import deepcopy
import json
from send import save2rabbitmqH1


def save2mongoMap2(dbname, collection, doc):
    try:
        hostname = os.getenv('HOSTNAME')
        # hostname = 'x'
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

    # gen_time = datetime.strptime(doc['dt'], '%Y-%m-%d %H:%M:%S')
    # dummy_id = ObjectId.from_datetime(gen_time)

    z = {'dt': doc['dt'],
         'distance': doc['result']['taxi']['distance'],
         'duration': doc['result']['taxi']['duration'],
         'traffic_condition': doc['result']['traffic_condition'],
         'distance4': doc['result']['routes'][0]['steps'][12]['distance'],
         'duration4': doc['result']['routes'][0]['steps'][12]['duration'],
         'traffic_condition4': doc['result']['routes'][0]['steps'][12]['traffic_condition']
         }
    #z_mq = deepcopy(z)

    dbh[collection].insert(z)
    print("Successfully inserted document: %s" % z)


def save2mongoMap3(dbname,collection,doc):
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
    
    #gen_time = datetime.strptime(doc['dt'], '%Y-%m-%d %H:%M:%S') 
    #dummy_id = ObjectId.from_datetime(gen_time)

    z = {'dt': doc['dt'],
             'distance': doc['result']['taxi']['distance'],
             'duration': doc['result']['taxi']['duration'],
             'traffic_condition': doc['result']['traffic_condition'],
             'distance4': doc['result']['routes'][0]['steps'][4]['distance'],
             'duration4': doc['result']['routes'][0]['steps'][4]['duration'],
             'traffic_condition4': doc['result']['routes'][0]['steps'][4]['traffic_condition']
             }
    #z_mq = deepcopy(z)
    
    dbh[collection].insert(z)
    print("Successfully inserted document: %s" % z)



def save2mongoMap4(dbname, collection, doc):
    try:
        hostname = os.getenv('HOSTNAME')
        # hostname = 'x'
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

    # gen_time = datetime.strptime(doc['dt'], '%Y-%m-%d %H:%M:%S')
    # dummy_id = ObjectId.from_datetime(gen_time)

    z = {'dt': doc['dt'],
         'distance': doc['result']['taxi']['distance'],
         'duration': doc['result']['taxi']['duration'],
         'traffic_condition': doc['result']['traffic_condition'],
         'distance4': doc['result']['routes'][0]['steps'][3]['distance'],
         'duration4': doc['result']['routes'][0]['steps'][3]['duration'],
         'traffic_condition4': doc['result']['routes'][0]['steps'][3]['traffic_condition']
         }
    #z_mq = deepcopy(z)

    dbh[collection].insert(z)
    print("Successfully inserted document: %s" % z)


def save2mongoMap5(dbname, collection, doc):
    try:
        hostname = os.getenv('HOSTNAME')
        # hostname = 'x'
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

    # gen_time = datetime.strptime(doc['dt'], '%Y-%m-%d %H:%M:%S')
    # dummy_id = ObjectId.from_datetime(gen_time)

    z = {'dt': doc['dt'],
         'distance': doc['result']['taxi']['distance'],
         'duration': doc['result']['taxi']['duration'],
         'traffic_condition': doc['result']['traffic_condition'],
         'distance4': doc['result']['routes'][0]['steps'][2]['distance'],
         'duration4': doc['result']['routes'][0]['steps'][2]['duration'],
         'traffic_condition4': doc['result']['routes'][0]['steps'][2]['traffic_condition']
         }
    #z_mq = deepcopy(z)

    dbh[collection].insert(z)
    print("Successfully inserted document: %s" % z)


def main():
    user_doc = {
        "username": "janedoe",
        "firstname": "Jane",
        "surname": "Doe",
        "dt": datetime(1975, 1, 1),
        "email": "janedoe74@example.com",
        "score": 0
    }
    save2mongo('baidu', 'mycoll', user_doc)


if __name__ == "__main__":
    main()
