import json
import logging
import pika # type: ignore
from app.application.services.inventory_service import InventoryService
from app.infrastructure.database.mysql_inventory_repository import MySQLInventoryRepository
from app.infrastructure.messaging.rabbitmq_connection import get_rabbitmq_connection
import os

repository = MySQLInventoryRepository()
service = InventoryService(repository)

def process_message(ch, method, properties, body):
    try:
        data = json.load(body)

        print("Mensagem recebida da fila: ", data)

        service.insert_inventory(data)

        print("Dados inseridos no banco de dados com sucesso.")
        ch.basic_ack(delivery_tag=method.delivery_tag)
    
    except Exception as e:
        logging.error(f"Erro ao inserir dados no banco de dados: {e}")
        ch.basic_nack(delivery_tag=method.delivery_tag, requeue=False)