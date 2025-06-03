from flask import Flask
from app.interface.api import register_blueprints
from app.config.config import load_config

application = Flask(__name__)
application.config.from_mapping(load_config())

register_blueprints(application)