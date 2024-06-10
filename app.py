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
        cur.execute("""SELECT hosts.id, hosts.hostname, hosts.ip, hosts.architecture, hosts.plataform, 
                                hosts.processor, hosts.so, hosts.distribution, hosts.mem_total, hosts.mem_free, 
                                hosts.up_time, hosts.mac_address, hosts.created_at, hosts.updated_at, 
                                hi.environnment, hi.url, hi.cluster, hi.publication, hi.midleware, hi.framework, hi.app_language,
                                hb.priority, hb.risk, hb.acronym, hb.goal, hb.datacenter, hb.repository, hb.national_cjf 
                            FROM hosts
                            INNER JOIN hosts_aditional_infra hi ON hosts.hostname = hi.hostname
                            INNER JOIN hosts_business hb ON hosts.hostname = hb.hostname
                            ORDER BY hosts.id""")
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
                'updated_at': result[13],
                'environnment': result[14],
                'url': result[15],
                'cluster': result[16],
                'publication': result[17],
                'midleware': result[18],
                'framework': result[19],
                'app_language': result[20],
                'priority': result[21],
                'risk': result[22],
                'acronym': result[23],
                'goal': result[24],
                'datacenter': result[25],
                'repository': result[26],
                'national_cjf': result[27],
            }
            
            payload.append(content)
            content = {}

        # return jsonify({'test': 'true'}), 200
        return jsonify(payload), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close

@application.route('/hosts/<string:servername>', methods=['GET'])
def getHostsByUsername(servername):
    try:
        cur = mysql.connection.cursor()
        cur.execute("""SELECT hosts.id, hosts.hostname, hosts.ip, hosts.architecture, hosts.plataform, 
                                hosts.processor, hosts.so, hosts.distribution, hosts.mem_total, hosts.mem_free, 
                                hosts.up_time, hosts.mac_address, hosts.created_at, hosts.updated_at, 
                                hi.environnment, hi.url, hi.cluster, hi.publication, hi.midleware, hi.framework, hi.app_language,
                                hb.priority, hb.risk, hb.acronym, hb.goal, hb.datacenter, hb.repository, hb.national_cjf 
                            FROM hosts
                            INNER JOIN hosts_aditional_infra hi ON hosts.hostname = hi.hostname
                            INNER JOIN hosts_business hb ON hosts.hostname = hb.hostname
                            WHERE hosts.hostname = "{}"
                            ORDER BY hosts.id""".format(servername))
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
                'updated_at': result[13],
                'environnment': result[14],
                'url': result[15],
                'cluster': result[16],
                'publication': result[17],
                'midleware': result[18],
                'framework': result[19],
                'app_language': result[20],
                'priority': result[21],
                'risk': result[22],
                'acronym': result[23],
                'goal': result[24],
                'datacenter': result[25],
                'repository': result[26],
                'national_cjf': result[27],
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

        curCheckHostname = mysql.connection.cursor()
        curCheckHostname.execute("""SELECT hostname 
                            FROM hosts
                            WHERE hosts.hostname = "{}"
                    """.format(hostname))
        data = curCheckHostname.fetchall()
        print(data)

        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO hosts_business (hostname) VALUES ('{}')".format(hostname))

        cur.execute("INSERT INTO hosts_aditional_infra (hostname) VALUES ('{}')".format(hostname))

        cur.execute("INSERT INTO hosts (hostname, ip, architecture, plataform, processor, so, distribution, mem_total, mem_free, up_time, mac_address, created_at) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (hostname, ip, architecture, plataform, processor, so, distribution, mem_total, mem_free, up_time, mac_address, created_at))
        mysql.connection.commit()

        return jsonify({'host_add': 'true'}), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close

@application.route('/v1/updateiventory/<string:servername>', methods=['PUT'])
def update_infos(servername):
    try:

        url = str(request.json.get('url',None))
        cluster = str(request.json.get('cluster',None))
        publication = str(request.json.get('publication',None))
        environnment = str(request.json.get('environnment', None))
        middleware = str(request.json.get('middleware',None))
        framework = str(request.json.get('framework',None))
        app_language = str(request.json.get('app_language',None))
        priority = str(request.json.get('priority',None))
        risk = str(request.json.get('risk',None))
        acronym = str(request.json.get('acronym',None))
        datacenter = str(request.json.get('datacenter',None))
        repository = str(request.json.get('repository',None))
        national_cjf = str(request.json.get('national_cjf',None))
        goal = str(request.json.get('goal',None))
        updated_at = str(request.json.get('updated_at',None))

        cur = mysql.connection.cursor()
        
        cur.execute("UPDATE hosts SET updated_at='{}' WHERE hostname='{}'".format(updated_at, servername))

        cur.execute("""UPDATE hosts_aditional_infra
                    SET environnment='{}', url='{}', cluster='{}', publication='{}', midleware='{}', framework='{}', app_language='{}' 
                    WHERE hostname='{}'""".format(environnment, url, cluster, publication, middleware, framework, app_language, servername))

        cur.execute("""UPDATE hosts_business
                    SET priority='{}', risk='{}', acronym='{}', goal='{}', datacenter='{}', repository='{}', national_cjf='{}'
                    WHERE hostname='{}'""".format(priority, risk, acronym, goal, datacenter, repository, national_cjf, servername))

        mysql.connection.commit()

        return jsonify({'host_info': 'updated'}), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close



