import threading
import app
import pika
import os
from consumer import process_message
from repositories.connection import get_rabbitmq_connection
from dotenv import load_dotenv

load_dotenv()

app = app.application

def start_consumer():


	connection = get_rabbitmq_connection()
	channel = connection.channel()
	queue_name = os.getenv("RABBITMQ_QUEUE")

	channel.queue_declare(queue=queue_name, durable=True)
	channel.basic_qos(prefetch_count=1)
	channel.basic_consume(queue=queue_name, on_message_callback=process_message)

	with app.app_context():
		try:
			print('[*] Aguardando mensagens. Pressione CTRL+C para sair.')
			channel.start_consuming()
		except KeyboardInterrupt:
			print('[!] Encerrando consumidor.')
			channel.stop_consuming()
			connection.close()

if __name__ == '__main__':
	consumer_thread = threading.Thread(target=start_consumer, daemon=True)
	consumer_thread.start()

	app.run(debug=True, host='0.0.0.0', port='5000')

