from flask import Flask
from app.interface.routes.routes_inventory import inventory_bp
# from .auth_routes import auth_bp  # future

def register_blueprints(app: Flask):
    app.register_blueprint(inventory_bp)