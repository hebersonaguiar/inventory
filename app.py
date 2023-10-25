from flask import Flask, render_template, request, redirect, url_for, flash, stream_with_context, g, session
from flask_restful import Resource, Api
from flask_cors import CORS

application = Flask(__name__)
api = Api(application)
CORS(application, resources={r"/*": {"origins": "*"}})
application.secret_key = "flash message"