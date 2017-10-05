import pika
import json

def h1(doc):

    parameters = pika.URLParameters( 'amqp://rtjojptm:wTajVRnB9IWJgI1KdHBdLLSxaAJtFTHm@mosquito.rmq.cloudamqp.com/rtjojptm' )
    connection = pika.BlockingConnection(parameters)

    # Create normal 'Hello World' type channel.
    channel = connection.channel()
    channel.confirm_delivery()
    channel.queue_declare(queue='h1', durable=True)

    # We need to bind this channel to an exchange, that will be used to transfer
    # messages from our delay queue.
    channel.queue_bind(exchange='amq.direct',
                       queue='h1')

    channel.basic_publish(exchange='amq.direct',
                          routing_key='h1',
                          body=json.dumps(doc),
                          properties=pika.BasicProperties(delivery_mode=2))

    print ( " [x] Sent:" + json.dumps(doc) )

    connection.close()

def main():
    user_doc = {
    "username" : "janedoe",
    "firstname" : "Jane",
    "surname" : "Doe",
    "email" : "janedoe74@example.com",
    "score" : 0
    }
    h1( user_doc)

if __name__ == "__main__":
    main()
