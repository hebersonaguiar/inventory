from flask import Blueprint, request, jsonify
from app.application.services.inventory_service import InventoryService
from app.infrastructure.database.mysql_inventory_repository import MySQLInventoryRepository

inventory_bp = Blueprint('inventory', __name__, url_prefix='/api/v1/')

repository = MySQLInventoryRepository()
service = InventoryService(repository)

@inventory_bp.route('/host', methods=['GET'])
def get_inventory_by_hostname():
    try:
        data = request.get_json()
        result = service.get_inventory_by_hostname(data)
        return jsonify(result), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500