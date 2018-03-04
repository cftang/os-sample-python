""" An example of how to insert a document """
import os
import sys
from datetime import datetime
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import pymongo
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go
from scripts.dateadd import dayAdd

def save2rabbitmq(doc):
    z = {'dt': doc['dt'],
         'distance': doc['result']['taxi']['distance'],
         'duration': doc['result']['taxi']['duration'],
         'traffic_condition': doc['result']['traffic_condition'],
         'distance4': doc['result']['routes'][0]['steps'][4]['distance'],
         'duration4': doc['result']['routes'][0]['steps'][4]['duration'],
         'traffic_condition4': doc['result']['routes'][0]['steps'][4]['traffic_condition']
         }
    print(z)

def save2mongo(dbname,collection,doc):
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
    dbh[collection].insert(doc)
    print("Successfully inserted document: %s" % doc)
    #save2rabbitmq(doc)


def findlast2day(dbname, collection, title):
    try:
        hostname = os.getenv('HOSTNAME')
        # hostname = 'x'
        if hostname:
            c = MongoClient("mongodb://db1:user1@ds155684.mlab.com:55684/baidu")
            print("cloud " + collection)
        else:
            c = MongoClient("mongodb://user1:password1@localhost:27017/" + dbname)
            print("local " + collection)
    except ConnectionFailure as e:
        sys.stderr.write("Could not connect to MongoDB: %s" % e)
        sys.exit(1)
    dbh = c[dbname]
    c = dbh[collection].count() - 288
    z = dbh[collection].find(projection={"dt": 1, "duration4": 1, "traffic_condition4": 1}, skip=c)\
        .sort("dt", pymongo.ASCENDING)

    list1 = []
    list2 = []
    list3 = []
    row = 0
    d2 = ''
    for doc in z:
        d2 = doc['dt']
    d2 = d2[0:10]

    z.rewind()
    for doc in z: 
        #print(doc)
        row += 1
        dt = doc['dt']
        duration4 = int(doc['duration4']/60),
        traffic_condition4 = doc['traffic_condition4']
        if dt.startswith(d2):
            if traffic_condition4 == 1:
                list1.append({'dt': dt, 'duration4': duration4})
            elif traffic_condition4 == 2:
                list1.append({'dt': dt, 'duration4': duration4})
                list2.append({'dt': dt, 'duration4': duration4})
            elif traffic_condition4 == 3:
                list1.append({'dt': dt, 'duration4': duration4})
                list2.append({'dt': dt, 'duration4': duration4})
                list3.append({'dt': dt, 'duration4': duration4})
    print("Successfully retrieved document: %d" % z.count(True))
    # https://docs.mongodb.com/manual/reference/method/cursor.count/#cursor.count
    # applySkipLimit

    #print (len(list))
    df1 = pd.DataFrame(list1)
    df2 = pd.DataFrame(list2)
    df3 = pd.DataFrame(list3)

    myplotly(df1, df2, df3, collection, title)


# https://plot.ly/python/dot-plots/
def myplotly(df1, df2, df3, collection, title):

    trace1 = go.Scatter(
        x=df1['dt'],
        y=df1['duration4'],
        name=u'通畅',
        marker={"color": "rgb(31,119,180)"}
    )
    trace2 = go.Scatter(
        x=df2['dt'],
        y=df2['duration4'],
        name=u'缓慢',
        mode='markers',
        marker=dict(
            color='rgba(255,255,0, 0.95)',
            line=dict(
                color='rgba(255,255,0, 1.0)',
                width=1,
            ),
            symbol='circle',
            size=10,
        )
    )
    trace3 = go.Scatter(
        x=df3['dt'],
        y=df3['duration4'],
        name=u'拥堵',
        mode='markers',
        marker=dict(
            color='rgba(255, 0, 0, 0.95)',
            line=dict(
                color='rgba(255, 0, 0, 1.0)',
                width=1,
            ),
            symbol='circle',
            size=16,
        )
    )
    data = [trace1, trace2, trace3]

    # axes range
    # https://plot.ly/python/axes/

    layout = go.Layout(
        title=title + df2['dt'][len(df2.index) - 1]
    )
    fig = go.Figure(data=data, layout=layout)
    py.plot(fig, filename='colorfulLine', fileopt='overwrite', auto_open=False)


if __name__ == "__main__":
    findlast2day('baidu', sys.argv[1], sys.argv[2])
