from flask import Flask, render_template, request, redirect, url_for, flash, stream_with_context, g, session
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_jsonpify import jsonify
from repositories import connection

application = Flask(__name__)
api = Api(application)
CORS(application, resources={r"/*": {"origins": "*"}})
application.secret_key = "flash message"

mysql = connection.get_connection(application)

@application.route('/test', methods=['GET'])
def test():
    try:
        cur = mysql.connection.cursor()
        cur.execute("select * from test")
        data = cur.fetchall()

        return jsonify({'test': 'true'}), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close
        