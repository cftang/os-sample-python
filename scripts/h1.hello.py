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

s_1 = py.Stream(stream_id=token_1)
s_2 = py.Stream(stream_id=token_2)
s_1.open()
s_2.open()

parameters = pika.URLParameters( 'amqp://rtjojptm:wTajVRnB9IWJgI1KdHBdLLSxaAJtFTHm@mosquito.rmq.cloudamqp.com/rtjojptm' )
connection = pika.BlockingConnection(parameters)

channel = connection.channel()
channel.confirm_delivery()
channel.queue_declare(queue='h1',durable = True)


# Create normal 'Hello World' type channel.
#channel = connection.channel()
#channel.confirm_delivery()
#channel.queue_declare(queue='hello', durable=True)

# We need to bind this channel to an exchange, that will be used to transfer 
# messages from our delay queue.
channel.queue_bind(exchange='amq.direct',
                           queue='hello')

# Create our delay channel.
delay_channel = connection.channel()
delay_channel.confirm_delivery()

# This is where we declare the delay, and routing for our delay channel.
delay_channel.queue_declare(queue='hello_delay', durable=True,  arguments={
      'x-message-ttl' : 86400000, # Delay until the message is transferred in milliseconds.
        'x-dead-letter-exchange' : 'amq.direct', # Exchange used to transfer the message from A to B.
          'x-dead-letter-routing-key' : 'hello' # Name of the queue we want the message transferred to.
          })

def callback(ch, method, properties, p_body):
    print(" [x] Received %r" % p_body)
    # forward  message to delay queue
    delay_channel.basic_publish(exchange='',
        routing_key='hello_delay',
        body=p_body,
        properties=pika.BasicProperties(delivery_mode=2))
    # 2 streaming 
    j = json.loads( p_body.decode("utf-8") )
    distance = j['distance']
    if distance > 0 :
        x = j['dt']
        y = j['duration4']
        print (x)
        print (y)
        s_1.write(dict(x=x,y=y))
        y = j['traffic_condition4']*300
        print (x)
        print (y)
        s_2.write(dict(x=x,y=y))
    else :
        s_1.heartbeat()
        s_2.heartbeat()
        print(    datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f'))

channel.basic_consume(callback, queue='h1', no_ack=True)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
