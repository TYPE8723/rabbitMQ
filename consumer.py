import pika
from loguru import logger
def on_message_received(ch,method,properties,body):
    print(f"recievd new message :{body}")

connection_parameters = pika.ConnectionParameters("localhost")

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()
channel.queue_declare(queue="Letterbox")

channel.basic_consume(queue="Letterbox",auto_ack=True,on_message_callback=on_message_received)

logger.info("Start consuming")

channel.start_consuming()