from flask import Flask, render_template, request, redirect, url_for, flash, stream_with_context, g, session
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_jsonpify import jsonify
from repositories import connection
import json

application = Flask(__name__)
api = Api(application)
CORS(application, resources={r"/*": {"origins": "*"}})
application.secret_key = "flash message"

mysql = connection.get_connection(application)

@application.route('/hosts', methods=['GET'])
def hosts():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, hostname, ip, architecture, plataform, processor, so, distribution, mem_total, mem_free, up_time, mac_address FROM host_info")
        data = cur.fetchall()

        payload = []
        content = []

        for result in data:
            content = {
                'id': result[0],
                'hostname': result[1],
                'ip': result[2],
                'architecture': result[3],
                'plataform': result[4],
                'processor': result[5],
                'so': result[6],
                'distribution': result[7],
                'mem_total': result[8],
                'mem_free': result[9],
                'up_time': result[10],
                'mac_address': result[11]
            }
            
            payload.append(content)
            content = {}

        # return jsonify({'test': 'true'}), 200
        return jsonify(payload), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close
        