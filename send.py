import pika

def h1(doc):

    parameters = pika.URLParameters( 'amqp://rtjojptm:wTajVRnB9IWJgI1KdHBdLLSxaAJtFTHm@mosquito.rmq.cloudamqp.com/rtjojptm' )
    connection = pika.BlockingConnection(parameters)

    # Create normal 'Hello World' type channel.
    channel = connection.channel()
    channel.confirm_delivery()
    channel.queue_declare(queue='h1', durable=True)

    # We need to bind this channel to an exchange, that will be used to transfer
    # messages from our delay queue.
    channel.queue_bind(exchange='',
                       queue='h1')

    channel.basic_publish(exchange='',
                          routing_key='h1',
                          body=doc,
                          properties=pika.BasicProperties(delivery_mode=2))

    print ( " [x] Sent:" + doc )

    connection.close()
