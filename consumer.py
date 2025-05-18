import pika
import json

def process_message(ch, method, properties, body):
    data = json.loads(body)
    # Aqui você pode chamar a função que insere os dados na base de dados
    print(f"Processando: {data}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='infrasa_inventory_queue', durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='infrasa_inventory_queue', on_message_callback=process_message)

print(' [*] Aguardando mensagens. Para sair pressione CTRL+C')
channel.start_consuming()
