import pika
import json
import logging
import traceback
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
        logging.error(f"Erro ao inserir no banco: {str(e)}")
        logging.error("Erro ao inserir no banco:\n%s", traceback.format_exc())
