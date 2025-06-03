from flask import Flask
from app.interface.api import register_blueprints
from app.config.settings import settings

application = Flask(__name__)

register_blueprints(application)