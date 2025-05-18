import pika
import json

def send_to_queue(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='infrasa_inventory_queue', durable=True)
    channel.basic_publish(
        exchange='',
        routing_key='infrasa_inventory_queue',
        body=json.dumps(data),
        properties=pika.BasicProperties(
            delivery_mode=2,  # Torna a mensagem persistente
        )
    )
    connection.close()
