#https://youtube.com/playlist?list=PLalrWAGybpB-UHbRDhFsBgXJM1g6T4IvO
# run rabbitmq :
# docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.11-management

import pika
from loguru import logger
connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
channel = connection.channel()
channel.queue_declare(queue="Letterbox")
message = "hello this is a msg from producer"
channel.basic_publish(exchange="",routing_key="Letterbox",body=message)
logger.info("Transefredd succcessfully")
connection.close()