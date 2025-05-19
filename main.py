import threading
import app
import pika
import os
from consumer import process_message
from repositories import connection 
from dotenv import load_dotenv

load_dotenv()

app = app.application

def start_consumer():


	conn = connection.get_rabbitmq_connection()
	channel = conn.channel()
	queue_name = os.getenv("RABBITMQ_QUEUE")

	channel.queue_declare(queue=queue_name, durable=True)
	channel.basic_qos(prefetch_count=1)
	channel.basic_consume(queue=queue_name, on_message_callback=process_message)

	# connection = pika.BlockingConnection(pika.ConnectionParameters(os.getenv("RABBITMQ_HOST")))
	# channel = connection.channel()
	# channel.queue_declare(queue=os.getenv("RABBITMQ_QUEUE"), durable=True)
	# channel.basic_qos(prefetch_count=1)
	# channel.basic_consume(queue=os.getenv("RABBITMQ_QUEUE"), on_message_callback=process_message)

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

