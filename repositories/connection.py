from flask_mysqldb import MySQL
import app

t = app.define_app()

def get_connection():
    print("Connections")
    t.config['MYSQL_HOST'] = "mysql"
    t.config['MYSQL_USER'] = "root"
    t.config['MYSQL_PASSWORD'] = "my-secret-pw"
    t.config['MYSQL_DB'] = "inventory"

    mysql = MySQL(t)

    # cur = mysql.connection.cursor()
    
    return mysql


