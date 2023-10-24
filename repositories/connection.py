from flask_mysqldb import MySQL
import main

def get_connection():
    main.app.config['MYSQL_HOST'] = 'mysql'
    main.app.config['MYSQL_USER'] = 'root'
    main.app.config['MYSQL_PASSWORD'] = 'my-secret-pw'
    main.app.config['MYSQL_DB'] = 'inventory'

    mysql = MySQL(main.app)

    cur = mysql.connection.cursor()
    
    return cur


