from flask import Blueprint, request, jsonify # type: ignore
from app.application.services.inventory_service import InventoryService
from app.infrastructure.database.mysql_inventory_repository import MySQLInventoryRepository
from app.infrastructure.messaging.rabbitmq_producer_repository import RabbitMQInventoryRepository

inventory_bp = Blueprint('inventory', __name__, url_prefix='/api/v1/')

repositoryDatabase = MySQLInventoryRepository()
serviceDatabase = InventoryService(repositoryDatabase)
repositoryQueue = RabbitMQInventoryRepository()
serviceQueue = InventoryService(repositoryQueue)

@inventory_bp.route('/health', methods=['GET'])
def health_check():
    return jsonify(status='ok'), 200

@inventory_bp.route('/host', methods=['GET'])
def get_inventory_by_hostname():
    try:
        data = request.get_json()
        result = serviceDatabase.get_inventory_by_hostname(data)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@inventory_bp.route('/inventory', methods=['GET'])
def get_inventory():
    try:
        result = serviceDatabase.get_inventory()
        return jsonify(result), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@inventory_bp.route('/inventory', methods=['POST'])
def receive_inventory_data():
    try:
        data = request.get_json()

        serviceQueue.send_to_queue(data)

        return jsonify({'message': 'Dados enviados para fila com sucesso'}), 202
    except Exception as e:
        print("Erro ao enviar para fila:", e)
        return jsonify({'error': str(e)}), 500