from flask_mysqldb import MySQL
import app

def get_connection():
    print("Connections")
    app.app.config['MYSQL_HOST'] = "mysql"
    app.app.config['MYSQL_USER'] = "root"
    app.app.config['MYSQL_PASSWORD'] = "my-secret-pw"
    app.app.config['MYSQL_DB'] = "inventory"

    mysql = MySQL(app)

    # cur = mysql.connection.cursor()
    
    return mysql


