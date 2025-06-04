from app.infrastructure.messaging.rabbitmq_connection import get_rabbitmq_connection
import json
import os
import pika # type: ignore

class RabbitMQInventoryRepository:

    def __init__(self):
        self.queue_name = os.getenv("RABBITMQ_QUEUE", "infrasa_inventory_queue")

    def send_to_queue(self, data: dict) -> str:
        connection = get_rabbitmq_connection()
        channel = connection.channel()

        channel.queue_declare(queue=self.queue_name, durable=True)
        message = json.dumps(data)

        channel.basic_publish(
            exchange='',
            routing_key=self.queue_name,
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2, # Torna a mensagem persistente
            )
        )

        connection.close()