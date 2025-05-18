import pika
import json
from app import insert_inventory

def process_message(ch, method, properties, body):
    try:
        data = json.loads(body)

        hostname = data.get('hostname')
        ipv4 = data.get('ipv4')
        arch = data.get('arch')
        processor = data.get('processor')
        so = data.get('so')
        distribution = data.get('distribution')
        mem_total = data.get('mem_total')
        mem_free = data.get('mem_free')
        up_time = data.get('up_time')
        mac_address = data.get('mac_address')

        insert_inventory(hostname, ipv4, arch, processor, so, distribution, mem_total, mem_free, up_time, mac_address)


        print(f"[✓] Dados do host: {hostname} inseridos.")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    except Exception as e:
        print(f"[✗] Erro ao processar mensagem: {e}")

connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
channel = connection.channel()
channel.queue_declare(queue='infrasa_inventory_queue', durable=True)
channel.basic_qos(prefetch_count=1)
channel.basic_consume(queue='infrasa_inventory_queue', on_message_callback=process_message)


if __name__ == '__main__':
    try:
        print('[*] Aguardando mensagens. Pressione CTRL+C para sair.')
        channel.start_consuming()
    except KeyboardInterrupt:
        print('[!] Encerrando consumidor.')
        channel.stop_consuming()
        connection.close()

# print(' [*] Aguardando mensagens. Para sair pressione CTRL+C')
# channel.start_consuming()
