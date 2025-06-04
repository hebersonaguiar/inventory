from messaging.rabbitmq_consumer_repository import process_message
from app.infrastructure.messaging.rabbitmq_connection import get_rabbitmq_connection
import os

def start_consumer(self):
    connection = get_rabbitmq_connection()
    channel = connection.channel()
    queue_name = os.getenv("RABBITMQ_QUEUE", "infrasa_inventory_queue")
    
    channel. queue_declare(queue=queue_name, durable=True)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=process_message)

    try:
        print("Aguardando mensagens da fila...")
        channel.start_consuming()
    except KeyboardInterrupt:
        print("Encerrando Consumer")
        channel.stop_consuming()
        connection.close()