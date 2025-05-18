import app
import pika
from consumer import process_message

app = app.application

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='infrasa_inventory_queue', durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='infrasa_inventory_queue', on_message_callback=process_message)

def run_app():
	app.run(debug=True, host='0.0.0.0', port='5000')

if __name__ == '__main__':
	with app.app_context():
		try:
			print('[*] Aguardando mensagens. Pressione CTRL+C para sair.')
			channel.start_consuming()
			run_app()
		except KeyboardInterrupt:
			print('[!] Encerrando consumidor.')
			channel.stop_consuming()
			connection.close()
