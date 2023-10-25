from flask_mysqldb import MySQL

def get_connection(app):
    print("Connections")
    app.config['MYSQL_HOST'] = "mysql"
    app.config['MYSQL_USER'] = "root"
    app.config['MYSQL_PASSWORD'] = "my-secret-pw"
    app.config['MYSQL_DB'] = "inventory"

    mysql = MySQL(app)
    
    return mysql