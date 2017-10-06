#!/usr/bin/env python
import pika
import json
import datetime

import plotly.plotly as py
import plotly.tools as tls
import plotly.graph_objs as go

stream_ids = tls.get_credentials_file()['stream_ids']

token_1 = stream_ids[0]   
token_2 = stream_ids[1]
token_3 = stream_ids[2]   
token_4 = stream_ids[3]

stream_id1 = dict(token=token_1, maxpoints=288)
stream_id2 = dict(token=token_2, maxpoints=288)
stream_id3 = dict(token=token_3, maxpoints=288)
stream_id4 = dict(token=token_4, maxpoints=288)

trace1 = go.Scatter(x=[], y=[], stream=stream_id1, name='trace1')
trace2 = go.Scatter(x=[], y=[], stream=stream_id2, name='trace2', marker=dict(color='rgb(148, 103, 18)'))
trace3 = go.Scatter(x=[], y=[], stream=stream_id3, name='trace3', marker=dict(color='rgb(48, 153, 89)'))
trace4 = go.Scatter(x=[], y=[], stream=stream_id4, name='trace4', marker=dict(color='rgb(8, 203, 189)'))

data = [trace1, trace2, trace3, trace4 ]
layout = go.Layout(
    title='Streaming Four Traces',
    yaxis=dict(
    title='y'
   )
)
                  
fig = go.Figure(data=data, layout=layout)
plot_url = py.plot(fig, filename='multple-trace-axes-streaming', fileopt = 'extend')

s_3 = py.Stream(stream_id=token_3)
s_4 = py.Stream(stream_id=token_4)
s_3.open()
s_4.open()

parameters = pika.URLParameters( 'amqp://rtjojptm:wTajVRnB9IWJgI1KdHBdLLSxaAJtFTHm@mosquito.rmq.cloudamqp.com/rtjojptm' )
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.confirm_delivery()
channel.queue_declare(queue='hello',durable = True)


# Create normal 'Hello World' type channel.
#channel = connection.channel()
#channel.confirm_delivery()
#channel.queue_declare(queue='hello', durable=True)

# We need to bind this channel to an exchange, that will be used to transfer 
# messages from our delay queue.
channel.queue_bind(exchange='amq.direct',
                           queue='hello')

def callback(ch, method, properties, p_body):
    print(" [x] Received %r" % p_body)
    # 2 streaming 
    j = json.loads( p_body.decode("utf-8") )
    distance = j['distance']
    if distance > 0 :
        x = j['dt']
        y = j['duration4']
        print (x)
        print (y)
        s_3.write(dict(x=x,y=y))
        y = j['traffic_condition4']*300
        print (x)
        print (y)
        s_4.write(dict(x=x,y=y))
    else :
        s_3.heartbeat()
        s_4.heartbeat()
        print(    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

channel.basic_consume(callback, queue='hello', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
