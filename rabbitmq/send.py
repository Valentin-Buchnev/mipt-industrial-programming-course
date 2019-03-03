#!/usr/bin/env python
import pika
import time
import random

conn_params = pika.ConnectionParameters('localhost', 5680)
connection = pika.BlockingConnection(conn_params)
channel = connection.channel()

channel.queue_declare(queue='first-queue')

while True:
    channel.basic_publish(exchange='',
			  routing_key='first-queue',
			  body='{}'.format(random.randint(1, 100)))
    time.sleep(random.randint(1, 10))

connection.close()
