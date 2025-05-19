from flask import Flask, render_template, request, redirect, url_for, flash, stream_with_context, g, session
from flask_restful import Resource, Api
from flask_cors import CORS
from flask_jsonpify import jsonify
from repositories import connection
import json, datetime
from producer import send_to_queue

application = Flask(__name__)
api = Api(application)
CORS(application, resources={r"/*": {"origins": "*"}})
application.secret_key = "flash message"

mysql = connection.get_connection(application)

### HEALTH CHECK VERIFICATION
### TO-DO: IMPROVE HEALTH CHECK, EX, DATABASE CHECK
@application.route('/health')
def health_check():
    return jsonify(status="ok"), 200

### GET ALL HOSTS
@application.route('/api/v1/hosts', methods=['GET'])
def hosts():
    try:
        cur = mysql.connection.cursor()
        cur.execute("""SELECT 
                            h.id,
                            h.hostname,
                            h.ipv4,
                            h.arch,
                            h.processor,
                            h.so,
                            h.distribution,
                            h.mem_total,
                            h.mem_free,
                            h.up_time,
                            h.mac_address,
                            h.created_at,
                            h.updated_at,
                            hi.env,
                            hi.url,
                            hi.is_internal,
                            hi.midleware,
                            hi.app_language,
                            hi.app_system,
                            hi.location,
                            hi.notes
                        FROM hosts h
                        INNER JOIN hosts_aditional_infos hi ON h.hostname = hi.hostname
                        ORDER BY h.id;
                    """)
        data = cur.fetchall()

        payload = []
        content = []

        for result in data:
            content = {
                'id': result[0],
                'hostname': result[1],
                'ipv4': result[2],
                'arch': result[3],
                'processor': result[4],
                'so': result[5],
                'distribution': result[6],
                'mem_total': result[7],
                'mem_free': result[8],
                'up_time': result[9],
                'mac_address': result[10],
                'created_at': result[11],
                'updated_at': result[12],
                'env': result[13],
                'url': result[14],
                'is_internal': result[15],
                'midleware': result[16],
                'app_language': result[17],
                'app_system': result[17],
                'location': result[18],
                'notes': result[19],
            }
            
            payload.append(content)
            content = {}

        return jsonify(payload), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close

### GET ONLY ONE HOST BY HOSTNAME
@application.route('/api/v1/hosts/<string:servername>', methods=['GET'])
def getHostsByUsername(servername):
    try:
        cur = mysql.connection.cursor()

        cur.execute("""SELECT 
                            h.id,
                            h.hostname,
                            h.ipv4,
                            h.arch,
                            h.processor,
                            h.so,
                            h.distribution,
                            h.mem_total,
                            h.mem_free,
                            h.up_time,
                            h.mac_address,
                            h.created_at,
                            h.updated_at,
                            hi.env,
                            hi.url,
                            hi.is_internal,
                            hi.midleware,
                            hi.app_language,
                            hi.app_system,
                            hi.location,
                            hi.notes
                        FROM hosts h
                        INNER JOIN hosts_aditional_infos hi ON h.hostname = hi.hostname
                        WHERE h.hostname = "{}"
                        ORDER BY h.id""".format(servername))
        data = cur.fetchall()

        payload = []
        content = []

        for result in data:
            content = {
                'id': result[0],
                'hostname': result[1],
                'ipv4': result[2],
                'arch': result[3],
                'processor': result[4],
                'so': result[5],
                'distribution': result[6],
                'mem_total': result[7],
                'mem_free': result[8],
                'up_time': result[9],
                'mac_address': result[10],
                'created_at': result[11],
                'updated_at': result[12],
                'env': result[13],
                'url': result[14],
                'is_internal': result[15],
                'midleware': result[16],
                'app_language': result[17],
                'app_system': result[17],
                'location': result[18],
                'notes': result[19],
            }
                    
            payload.append(content)
            content = {}

        return jsonify(payload), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close


@application.route('/api/v1/hosts/queue', methods=['POST'])
def receive_inventory():
    hostname = str(request.json.get('hostname', None))
    ipv4 = str(request.json.get('ipv4', None))
    arch = str(request.json.get('arch', None))
    processor = str(request.json.get('processor', None))
    so = str(request.json.get('so', None))
    distribution = str(request.json.get('distribution', None))
    mem_total = str(request.json.get('mem_total', None))
    mem_free = str(request.json.get('mem_free', None))
    up_time = str(request.json.get('up_time', None))
    mac_address = str(request.json.get('mac_address', None))

    data = {
        'hostname': hostname,
        'ipv4': ipv4,
        'arch': arch,
        'processor': processor,
        'so': so,
        'distribution': distribution,
        'mem_total': mem_total,
        'mem_free': mem_free,
        'up_time': up_time,
        'mac_address': mac_address
    }

    ## SEND INFOS TO QUEUE
    send_to_queue(data)

    return jsonify({'status': 'Data send to queue'}), 202

### ADD HOSTS INFOS, IF EXISTIS, UPDATE
@application.route('/api/v1/hosts', methods=['POST'])
def insert_inventory(hostname: str, ipv4: str, arch: str, processor: str, so: str, distribution: str, mem_total: str, mem_free: str, up_time: str, mac_address: str):
    try:


        print("Print Types App")
        
        print(type(hostname))

        hostname = str(hostname)
        ipv4 = str(ipv4)
        arch = str(arch)
        processor = str(processor)
        so = str(so)
        distribution = str(distribution)
        mem_total = str(mem_total)
        mem_free = str(mem_free)
        up_time = str(up_time)
        mac_address = str(mac_address)

        # hostname = str(request.json.get('hostname', None))
        # ipv4 = str(request.json.get('ipv4', None))
        # arch = str(request.json.get('arch', None))
        # processor = str(request.json.get('processor', None))
        # so = str(request.json.get('so', None))
        # distribution = str(request.json.get('distribution', None))
        # mem_total = str(request.json.get('mem_total', None))
        # mem_free = str(request.json.get('mem_free', None))
        # up_time = str(request.json.get('up_time', None))
        # mac_address = str(request.json.get('mac_address', None))
        
        now = datetime.datetime.now()
        created_at = now.strftime("%d-%m-%Y %H:%M")

        curCheckHostname = mysql.connection.cursor()
        curCheckHostname.execute("""SELECT hostname 
                            FROM hosts h
                            WHERE h.hostname = "{}"
                    """.format(hostname))
        data = curCheckHostname.fetchall()

        content = []

        for result in data:
            content = {
                result[0],
            }
        print(content)

        if hostname in content:
            print("Atualizando: ", hostname)
            curUpdate = mysql.connection.cursor()
            curUpdate.execute("""UPDATE hosts
                        SET ipv4 = '{}', 
                        arch = '{}', 
                        processor = '{}', 
                        so = '{}', 
                        distribution = '{}', 
                        mem_total = '{}', 
                        mem_free = '{}', 
                        up_time = '{}', 
                        mac_address = '{}',
                        updated_at = '{}' 
                        WHERE hostname = '{}'""".format(ipv4, arch, processor, so, distribution, mem_total, mem_free, up_time, mac_address, created_at, hostname))
            mysql.connection.commit()
            curUpdate.close
        else:
            print("Adicionando: ", hostname)
       
            cur = mysql.connection.cursor()

            cur.execute("INSERT INTO hosts_aditional_infos (hostname) VALUES ('{}')".format(hostname))

            cur.execute("""INSERT INTO hosts (
                                hostname, 
                                ipv4, 
                                arch,
                                processor, 
                                so, 
                                distribution, 
                                mem_total, 
                                mem_free, 
                                up_time, 
                                mac_address, 
                                created_at
                                ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)""", 
                                (hostname, ipv4, arch, processor, so, distribution, mem_total, mem_free, up_time, mac_address, created_at))
            mysql.connection.commit()
            cur.close

        return jsonify({'host_add': 'true'}), 200
    except Exception as error:
        return jsonify(error), 400


### UPDATE INVENTORY ADDITIONAL INFOS
@application.route('/api/v1/updateiventory/<string:servername>', methods=['PUT'])
def update_infos(servername):
    try:

        env = str(request.json.get('env',None))
        url = str(request.json.get('url',None))
        is_internal = str(request.json.get('is_internal',None))
        midleware = str(request.json.get('midleware',None))
        app_language = str(request.json.get('app_language',None))
        app_system = str(request.json.get('app_system',None))
        location = str(request.json.get('location',None))  
        notes = str(request.json.get('notes',None))
        updated_at = str(request.json.get('updated_at',None))           

        cur = mysql.connection.cursor()
        
        cur.execute("UPDATE hosts SET updated_at='{}' WHERE hostname='{}'".format(updated_at, servername))

        cur.execute("""UPDATE hosts_aditional_infos
                    SET env='{}', 
                        url='{}', 
                        is_internal='{}', 
                        midleware='{}', 
                        app_language='{}', 
                        app_system='{}', 
                        location='{}',
                        notes='{}'
                    WHERE hostname='{}'""".format(env,
                                                 url,
                                                 is_internal,
                                                 midleware,
                                                 app_language,
                                                 app_system,
                                                 location,
                                                 notes,
                                                 servername
                                                 ))
        mysql.connection.commit()

        return jsonify({'host_info': 'updated'}), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close