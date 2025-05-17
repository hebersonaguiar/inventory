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

@application.route('/health')
def health_check():
    return jsonify(status="ok"), 200

@application.route('/hosts', methods=['GET'])
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
                            h.updated_at
                        FROM hosts h;
                    """)
        ### SQL STATMENT USED TO CJF, TO BE DELETED
        # cur.execute("""SELECT h.id,h.hostname,h.ip,h.architecture,h.plataform,h.processor,h.so,h.distribution,h.mem_total,
        #                         h.mem_free,h.up_time,h.mac_address,h.created_at,h.updated_at,hi.cluster,hi.url,hi.scope,
        #                         hi.middleware,hi.framework,hi.environnment,hi.db_server,hi.db_name,hi.db_schema,
        #                         hi.db_user,hi.db_type,hi.kubernetes,hi.arch_ref,hi.monitoring_z,hi.situation,
        #                         hi.backup,hi.repository,hi.type,hb.auth,hb.permission,hb.responsible_cad,
        #                         hb.responsible_permission,hb.manager,hb.manager_substitute,hb.unit,hb.concierge_manager,
        #                         hb.sei_processor,hb.observation,hb.priority,hb.acronym,hb.sti_action,hb.datacenter,
        #                         hb.goal,hb.national_cjf,hi.app_language,hb.name
        #                 FROM hosts_new h
        #                 INNER JOIN hosts_aditional_infra_new hi ON h.hostname = hi.hostname
        #                 INNER JOIN hosts_business_new hb ON h.hostname = hb.hostname
        #                 ORDER BY h.id""")
        ### SQL STATMENT USED TO CJF, TO BE DELETED
        # cur.execute("""SELECT hosts.id, hosts.hostname, hosts.ip, hosts.architecture, hosts.plataform, 
        #                         hosts.processor, hosts.so, hosts.distribution, hosts.mem_total, hosts.mem_free, 
        #                         hosts.up_time, hosts.mac_address, hosts.created_at, hosts.updated_at, 
        #                         hi.environnment, hi.url, hi.cluster, hi.publication, hi.midleware, hi.framework, hi.app_language,
        #                         hb.priority, hb.risk, hb.acronym, hb.goal, hb.datacenter, hb.repository, hb.national_cjf 
        #                     FROM hosts_new
        #                     INNER JOIN hosts_aditional_infra_new hi ON hosts.hostname = hi.hostname
        #                     INNER JOIN hosts_business_new hb ON hosts.hostname = hb.hostname
        #                     ORDER BY hosts.id""")
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
            }
            ### SQL STATMENT USED TO CJF, TO BE DELETED
            # content = {
            #     'id': result[0],
            #     'hostname': result[1],
            #     'ip': result[2],
            #     'architecture': result[3],
            #     'plataform': result[4],
            #     'processor': result[5],
            #     'so': result[6],
            #     'distribution': result[7],
            #     'mem_total': result[8],
            #     'mem_free': result[9],
            #     'up_time': result[10],
            #     'mac_address': result[11],
            #     'created_at': result[12],
            #     'updated_at': result[13],
            #     'cluster': result[14],
            #     'url': result[15],
            #     'scope': result[16],
            #     'middleware': result[17],
            #     'framework': result[18],
            #     'environnment': result[19],
            #     'db_server': result[20],
            #     'db_name': result[21],
            #     'db_schema': result[22],
            #     'db_user': result[23],
            #     'db_type': result[24],
            #     'kubernetes': result[25],
            #     'arch_ref': result[26],
            #     'monitoring_z': result[27],
            #     'situation': result[28],
            #     'backup': result[29],
            #     'repository': result[30],
            #     'type': result[31],
            #     'auth': result[32],
            #     'permission': result[33],
            #     'responsible_cad': result[34],
            #     'responsible_permission': result[35],
            #     'manager': result[36],
            #     'manager_substitute': result[37],
            #     'unit': result[38],
            #     'concierge_manager': result[39],
            #     'sei_processor': result[40],
            #     'observation': result[41],
            #     'priority': result[42],
            #     'acronym': result[43],
            #     'sti_action': result[44],
            #     'datacenter': result[45],
            #     'goal': result[46],
            #     'national_cjf': result[47],
            #     'app_language': result[48],
            #     'name': result[49],
            ### SQL STATMENT USED TO CJF, TO BE DELETED
            # content = {
            #     'id': result[0],
            #     'hostname': result[1],
            #     'ip': result[2],
            #     'architecture': result[3],
            #     'plataform': result[4],
            #     'processor': result[5],
            #     'so': result[6],
            #     'distribution': result[7],
            #     'mem_total': result[8],
            #     'mem_free': result[9],
            #     'up_time': result[10],
            #     'mac_address': result[11],
            #     'created_at': result[12],
            #     'updated_at': result[13],
            #     'environnment': result[14],
            #     'url': result[15],
            #     'cluster': result[16],
            #     'publication': result[17],
            #     'midleware': result[18],
            #     'framework': result[19],
            #     'app_language': result[20],
            #     'priority': result[21],
            #     'risk': result[22],
            #     'acronym': result[23],
            #     'goal': result[24],
            #     'datacenter': result[25],
            #     'repository': result[26],
            #     'national_cjf': result[27],
            # }
            
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

        cur.execute("""SELECT
                            h.id 
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
                            h.updated_at
                        FROM hosts h
                        WHERE h.hostname = "{}"
                        ORDER BY h.id""".format(servername))
        ### SQL STATMENT USED TO CJF, TO BE DELETED
        # cur.execute("""SELECT h.id,h.hostname,h.ip,h.architecture,h.plataform,h.processor,h.so,h.distribution,h.mem_total,
        #                         h.mem_free,h.up_time,h.mac_address,h.created_at,h.updated_at,hi.cluster,hi.url,hi.scope,
        #                         hi.middleware,hi.framework,hi.environnment,hi.db_server,hi.db_name,hi.db_schema,
        #                         hi.db_user,hi.db_type,hi.kubernetes,hi.arch_ref,hi.monitoring_z,hi.situation,
        #                         hi.backup,hi.repository,hi.type,hb.auth,hb.permission,hb.responsible_cad,
        #                         hb.responsible_permission,hb.manager,hb.manager_substitute,hb.unit,hb.concierge_manager,
        #                         hb.sei_processor,hb.observation,hb.priority,hb.acronym,hb.sti_action,hb.datacenter,
        #                         hb.goal,hb.national_cjf,hi.app_language,hb.name
        #                     FROM hosts_new h
        #                     INNER JOIN hosts_aditional_infra_new hi ON h.hostname = hi.hostname
        #                     INNER JOIN hosts_business_new hb ON h.hostname = hb.hostname
        #                     WHERE h.hostname = "{}"
        #                     ORDER BY h.id""".format(servername))
        ### SQL STATMENT USED TO CJF, TO BE DELETED
        # cur.execute("""SELECT hosts.id, hosts.hostname, hosts.ip, hosts.architecture, hosts.plataform, 
        #                         hosts.processor, hosts.so, hosts.distribution, hosts.mem_total, hosts.mem_free, 
        #                         hosts.up_time, hosts.mac_address, hosts.created_at, hosts.updated_at, 
        #                         hi.environnment, hi.url, hi.cluster, hi.publication, hi.midleware, hi.framework, hi.app_language,
        #                         hb.priority, hb.risk, hb.acronym, hb.goal, hb.datacenter, hb.repository, hb.national_cjf 
        #                     FROM hosts_new
        #                     INNER JOIN hosts_aditional_infra_new hi ON hosts.hostname = hi.hostname
        #                     INNER JOIN hosts_business_new hb ON hosts.hostname = hb.hostname
        #                     WHERE hosts.hostname = "{}"
        #                     ORDER BY hosts.id""".format(servername))
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
            }
            # content = {
            #     'id': result[0],
            #     'hostname': result[1],
            #     'ip': result[2],
            #     'architecture': result[3],
            #     'plataform': result[4],
            #     'processor': result[5],
            #     'so': result[6],
            #     'distribution': result[7],
            #     'mem_total': result[8],
            #     'mem_free': result[9],
            #     'up_time': result[10],
            #     'mac_address': result[11],
            #     'created_at': result[12],
            #     'updated_at': result[13],
            #     'environnment': result[14],
            #     'url': result[15],
            #     'cluster': result[16],
            #     'publication': result[17],
            #     'midleware': result[18],
            #     'framework': result[19],
            #     'app_language': result[20],
            #     'priority': result[21],
            #     'risk': result[22],
            #     'acronym': result[23],
            #     'goal': result[24],
            #     'datacenter': result[25],
            #     'repository': result[26],
            #     'national_cjf': result[27],
            # }
            
            payload.append(content)
            content = {}

        # return jsonify({'test': 'true'}), 200
        return jsonify(payload), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close

### ADD HOSTS INFOS, IF EXISTIS, UPDATE
@application.route('/hosts', methods=['POST'])
def add_host():
    try:

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
        
        now = datetime.datetime.now()
        created_at = now.strftime("%d-%m-%Y %H:%M")

        curCheckHostname = mysql.connection.cursor()
        curCheckHostname.execute("""SELECT hostname 
                            FROM hosts h
                            WHERE h.hostname = "{}"
                    """.format(hostname))
        # curCheckHostname.execute("""SELECT hostname 
        #                     FROM hosts
        #                     WHERE hosts.hostname = "{}"
        #             """.format(hostname))
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
            # curUpdate.execute("""UPDATE hosts
            #             SET ip = '{}', 
            #             architecture = '{}', 
            #             plataform = '{}', 
            #             processor = '{}', 
            #             so = '{}', 
            #             distribution = '{}', 
            #             mem_total = '{}', 
            #             mem_free = '{}', 
            #             up_time = '{}', 
            #             mac_address = '{}' 
            #             WHERE hostname = '{}'""".format(ip, architecture, plataform, processor, so, distribution, mem_total, mem_free, up_time, mac_address, hostname))
            mysql.connection.commit()
            curUpdate.close

            # UPDATE Customers
            # SET ContactName = 'Alfred Schmidt', City = 'Frankfurt'
            # WHERE CustomerID = 1;
        else:
            print("Adicionando: ", hostname)
       
            cur = mysql.connection.cursor()
            # cur.execute("INSERT INTO hosts_business_new (hostname) VALUES ('{}')".format(hostname))

            # cur.execute("INSERT INTO hosts_aditional_infra_new (hostname) VALUES ('{}')".format(hostname))

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
    # finally:
    #     cur.close


### UPDATE INVENTORY
@application.route('/v1/updateiventory/<string:servername>', methods=['PUT'])
def update_infos(servername):
    try:

        cluster = str(request.json.get('cluster',None))
        url = str(request.json.get('url',None))
        scope = str(request.json.get('scope',None))
        middleware = str(request.json.get('middleware',None))
        framework = str(request.json.get('framework',None))
        app_language = str(request.json.get('app_language',None))
        environnment = str(request.json.get('environnment', None))
        db_server = str(request.json.get('db_server',None))
        db_name = str(request.json.get('db_name',None))
        db_schema = str(request.json.get('db_schema',None))
        db_user = str(request.json.get('db_user',None))
        db_type = str(request.json.get('db_type',None))
        kubernetes = str(request.json.get('kubernetes',None))
        arch_ref = str(request.json.get('arch_ref',None))
        monitoring_z = str(request.json.get('monitoring_z',None))
        situation = str(request.json.get('situation',None))
        backup = str(request.json.get('backup',None))
        repository = str(request.json.get('repository',None))
        type = str(request.json.get('type',None))
        auth = str(request.json.get('auth',None))
        permission = str(request.json.get('permission',None))
        responsible_cad = str(request.json.get('responsible_cad',None))
        responsible_permission = str(request.json.get('responsible_permission',None))
        manager = str(request.json.get('manager',None))
        manager_substitute = str(request.json.get('manager_substitute',None))
        unit = str(request.json.get('unit',None))
        concierge_manager = str(request.json.get('concierge_manager',None))
        sei_processor = str(request.json.get('sei_processor',None))
        observation = str(request.json.get('observation',None))
        priority = str(request.json.get('priority',None))
        acronym = str(request.json.get('acronym',None))
        sti_action = str(request.json.get('sti_action',None))
        name = str(request.json.get('name',None))
        datacenter = str(request.json.get('datacenter',None))
        goal = str(request.json.get('goal',None))
        national_cjf = str(request.json.get('national_cjf',None))



        updated_at = str(request.json.get('updated_at',None))

        cur = mysql.connection.cursor()
        
        cur.execute("UPDATE hosts SET updated_at='{}' WHERE hostname='{}'".format(updated_at, servername))

        # cur.execute("""UPDATE hosts_aditional_infra
        #             SET environnment='{}', url='{}', cluster='{}', publication='{}', midleware='{}', framework='{}', app_language='{}' 
        #             WHERE hostname='{}'""".format(environnment, url, cluster, publication, middleware, framework, app_language, servername))

        # cur.execute("""UPDATE hosts_business
        #             SET priority='{}', risk='{}', acronym='{}', goal='{}', datacenter='{}', repository='{}', national_cjf='{}'
        #             WHERE hostname='{}'""".format(priority, risk, acronym, goal, datacenter, repository, national_cjf, servername))

        cur.execute("""UPDATE hosts_aditional_infra_new
                    SET cluster='{}', 
                        url='{}', 
                        scope='{}', 
                        middleware='{}', 
                        framework='{}', 
                        app_language='{}', 
                        environnment='{}',
                        db_server='{}', 
                        db_name='{}', 
                        db_schema='{}', 
                        db_user='{}', 
                        db_type='{}', 
                        kubernetes='{}',
                        arch_ref='{}', 
                        monitoring_z='{}', 
                        situation='{}', 
                        backup='{}', 
                        repository='{}', 
                        type='{}'
                    WHERE hostname='{}'""".format(cluster,
                                                 url,
                                                 scope,
                                                 middleware,
                                                 framework,
                                                 app_language,
                                                 environnment,
                                                 db_server,
                                                 db_name,
                                                 db_schema,
                                                 db_user,
                                                 db_type,
                                                 kubernetes,
                                                 arch_ref,
                                                 monitoring_z,
                                                 situation,
                                                 backup,
                                                 repository,
                                                 type,
                                                 servername
                                                 ))

        cur.execute("""UPDATE hosts_business_new
                    SET auth='{}',
                        permission='{}',
                        responsible_cad='{}',
                        responsible_permission='{}',
                        manager='{}',
                        manager_substitute='{}',
                        unit='{}',
                        concierge_manager='{}',
                        sei_processor='{}',
                        observation='{}',
                        acronym='{}',
                        sti_action='{}',
                        name='{}',
                        datacenter='{}',
                        goal='{}',
                        national_cjf='{}',
                        priority='{}'
                    WHERE hostname='{}'""".format(auth,
                                                 permission,
                                                 responsible_cad,
                                                 responsible_permission,
                                                 manager,
                                                 manager_substitute,
                                                 unit,
                                                 concierge_manager,
                                                 sei_processor,
                                                 observation,
                                                 acronym,
                                                 sti_action,
                                                 name,
                                                 datacenter,
                                                 goal,
                                                 national_cjf,
                                                 priority,
                                                 servername))

        mysql.connection.commit()

        return jsonify({'host_info': 'updated'}), 200
    except Exception as error:
        return jsonify(error), 400
    finally:
        cur.close