from app.infrastructure.messaging.rabbitmq_connection import get_rabbitmq_connection
from app.config.settings import settings

def start_consumer(callback_funtion):
    connection = get_rabbitmq_connection()
    channel = connection.channel()

    channel.queue_declare(queue=settings.RABBITMQ_QUEUE, durable=true)
    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=settings.RABBITMQ_QUEUE, on_message_callback=callback_funtion)

    try:
        print("[*] Aguardando mensagens...")
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
        connection.close()