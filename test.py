""" An example of how to insert a document """
import os
import sys
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from send import h1
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

def save2rabbitmq(doc):
    z = {'dt': doc['dt'],
         'distance': doc['result']['taxi']['distance'],
         'duration': doc['result']['taxi']['duration'],
         'traffic_condition': doc['result']['traffic_condition'],
         'distance4': doc['result']['routes'][0]['steps'][4]['distance'],
         'duration4': doc['result']['routes'][0]['steps'][4]['duration'],
         'traffic_condition4': doc['result']['routes'][0]['steps'][4]['traffic_condition']
         }
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
    #save2rabbitmq(doc)

def findlast2day(dbname,collection):
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
    c = dbh[collection].count() -288*2
    z = dbh[collection].find(skip=c)
    #z = dbh[collection].find({'dt': '2017-10-08 01:22:38'}).limit(1)

    #z = dbh[collection].find({'dt': {'$gte':'2017-10-08 01:22:38'}}).limit(2)

    list = []
    for doc in z: 
        #print(doc)
        dt = doc['dt']
        distance = doc['result']['taxi']['distance'],
        duration = doc['result']['taxi']['duration'],
        traffic_condition = doc['result']['traffic_condition'],
        distance4 = doc['result']['routes'][0]['steps'][4]['distance'],
        duration4 = doc['result']['routes'][0]['steps'][4]['duration'],
        traffic_condition4 = doc['result']['routes'][0]['steps'][4]['traffic_condition']
        #print ('%s,%d,%d,%d,%d' % ( dt ,duration[0], traffic_condition[0], duration4[0], traffic_condition4) )
        list.append({'dt':dt,'duration':duration,'traffic_condition':traffic_condition,
                     'duration4':duration4,'traffic_condition4':traffic_condition4}) 
    print ("Successfully retrieved document: %d" % z.count(True) )
    # https://docs.mongodb.com/manual/reference/method/cursor.count/#cursor.count
    # applySkipLimit

    #print (len(list))
    df = pd.DataFrame(list)
    myplotly(df)

def myplotly(df):

    trace1 = go.Scatter(
        x=df['dt'],
        y=df['duration'],
        name='today duration',
        marker= {"color": "rgb(31,119,180)"}
    )
    trace2 = go.Scatter(
        x=df['dt'],
        y=df['traffic_condition'],
        name='today traffic condition',
        marker= {"color": "rgb(255,127,14)"}
    )
    trace3 = go.Scatter(
        x=df['dt'],
        y=df['duration4'],
        name='yesterday duration',
        marker= {"color": "rgb(214,39,40)"}
    )
    trace4 = go.Scatter(
        x=df['dt'],
        y=df['traffic_condition4'],
        name='yesterday traffic condition',
        marker= {"color": "rgb(148,103,189)"}
    )
    data = [trace1, trace2, trace3, trace4]
    layout = go.Layout(
        title='multiple y-axes example'
    )
    fig = go.Figure(data=data, layout=layout)
    plot_url = py.plot(fig, filename='multiple-axes-multiple',fileopt='overwrite')

def main():
    user_doc = {
        "username": "janedoe",
        "firstname": "Jane",
        "surname": "Doe",
        "dateofbirth": datetime(1975, 1, 1),
        "email": "janedoe74@example.com",
        "score": 0
    }
    save2mongo('baidu', 'mycoll', user_doc)

if __name__ == "__main__":
    findlast2day('baidu','map3')
