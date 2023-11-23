from flask import Flask, render_template, request, redirect, url_for, flash, stream_with_context, g, session
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_jsonpify import jsonify
from repositories import connection
import json, datetime

application = Flask(__name__)
api = Api(application)
CORS(application, resources={r"/*": {"origins": "*"}})
application.secret_key = "flash message"

mysql = connection.get_connection(application)

@application.route('/hosts', methods=['GET'])
def hosts():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT id, hostname, ip, architecture, plataform, processor, so, distribution, mem_total, mem_free, up_time, mac_address, created_at, updated_at FROM hosts")
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
                'mac_address': result[11],
                'created_at': result[12],
                'updated_at': result[13]
            }
            
            payload.append(content)
            content = {}

        # return jsonify({'test': 'true'}), 200
        return jsonify(payload), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close

@application.route('/hosts', methods=['POST'])
def add_host():
    try:

        hostname = str(request.json.get('hostname', None))
        ip = str(request.json.get('ip', None))
        architecture = str(request.json.get('architecture', None))
        plataform = str(request.json.get('plataform', None))
        processor = str(request.json.get('processor', None))
        so = str(request.json.get('so', None))
        distribution = str(request.json.get('distribution', None))
        mem_total = str(request.json.get('mem_total', None))
        mem_free = str(request.json.get('mem_free', None))
        up_time = str(request.json.get('up_time', None))
        mac_address = str(request.json.get('mac_address', None))
        
        now = datetime.datetime.now()
        created_at = now.strftime("%d-%m-%Y %H:%M")


        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO hosts (hostname, ip, architecture, plataform, processor, so, distribution, mem_total, mem_free, up_time, mac_address, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (hostname, ip, architecture, plataform, processor, so, distribution, mem_total, mem_free, up_time, mac_address, created_at))
        mysql.connection.commit()

        return jsonify({'host_add': 'true'}), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close