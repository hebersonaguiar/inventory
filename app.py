from flask import Flask, render_template, request, redirect, url_for, flash, stream_with_context, g, session
from flask_restful import Resource, Api
from flask_cors import CORS


def define_app():
    app = Flask(__name__)
    api = Api(app)
    CORS(app, resources={r"/*": {"origins": "*"}})
    app.secret_key = "flash message"

    return app, api