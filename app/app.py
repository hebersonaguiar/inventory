from flask import Flask
from app.interface.api import register_blueprints
from app.config.settings import Settings

application = Flask(__name__)
application.settings.from_mapping(Settings())

register_blueprints(application)