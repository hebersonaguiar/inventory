import pika
import json
import os
from dotenv import load_dotenv

load_dotenv()

def send_to_queue(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters(os.getenv("RABBITMQ_HOST")))
    channel = connection.channel()
    channel.queue_declare(queue=os.getenv("RABBITMQ_QUEUE"), durable=True)
    channel.basic_publish(
        exchange='',
        routing_key=os.getenv("RABBITMQ_QUEUE"),
        body=json.dumps(data),
        properties=pika.BasicProperties(
            delivery_mode=2,  # Torna a mensagem persistente
        )
    )
    connection.close()
