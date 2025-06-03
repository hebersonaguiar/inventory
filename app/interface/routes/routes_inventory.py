from flask import Blueprint, request, jsonify
from app.application.services.inventory_service import InventoryService
from app.infrastructure.database.mysql_inventory_repository import MySQLInventoryRepository

inventory_bp = Blueprint('inventory', __name__, url_prefix='/api/v1/')

repository = MySQLInventoryRepository()
service = InventoryService(repository)

@inventory_bp.route('/host', methods=['GET'])
def get_hostname():
    try:
        data = request.json
        hostname = request.json.get('hostname', None)
        print(hostname)
        service.get_hostname(hostname[0])
        return jsonify({'message': 'Host get successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500