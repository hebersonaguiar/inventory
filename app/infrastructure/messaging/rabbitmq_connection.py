import pika
from app.config.settings import settings

def get_rabbitmq_connection():
    credentials = pika.PlainCredentials(settings.RABBITMQ_USER, settings.RABBITMQ_PASSWORD)
    parameters = pika.ConnectionParameters(host=settings.RABBITMQ_HOST, credentials=credentials)
    connection = pika.BlockingConnection(parameters)
    return connection
