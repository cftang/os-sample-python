#!/opt/app-root/bin/python
import pika
import json
import time

parameters = pika.URLParameters('amqp://rtjojptm:wTajVRnB9IWJgI1KdHBdLLSxaAJtFTHm@mosquito.rmq.cloudamqp.com/rtjojptm')
connection = pika.BlockingConnection(parameters)

# Create normal 'Hello World' type channel.
channel = connection.channel()
channel.confirm_delivery()
channel.queue_declare(queue='h1', durable=True)

# We need to bind this channel to an exchange, that will be used to transfer
# messages from our delay queue.
channel.queue_bind(exchange='amq.direct',
                   queue='h1')
d = {'distance': 0}
for num in range(1, 200000000):
    channel.basic_publish(exchange='amq.direct',
                          routing_key='h1',
                          body=json.dumps(d),
                          properties=pika.BasicProperties(delivery_mode=2))
    time.sleep(60)
