from flask import Flask
from app.interface.api.routes_inventory import inventory_bp
# from .auth_routes import auth_bp  # future

def register_blueprints(app: Flask):
    app.register_blueprints(inventory_bp)