import pika
import json
import os
from repositories.connection import get_rabbitmq_connection
from dotenv import load_dotenv

load_dotenv()


def send_to_queue(data):
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    queue_name = os.getenv("RABBITMQ_QUEUE")

    channel.queue_declare(queue=queue_name, durable=True)
    channel.basic_publish(
        exchange="",
        routing_key=queue_name,
        body=json.dumps(data),
        properties=pika.BasicProperties(
            delivery_mode=2,  # Torna a mensagem persistente
        ),
    )
    connection.close()