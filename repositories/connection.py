from flask_mysqldb import MySQL
# import app


class MysqlDB:
    def __init__(self):
        self.app = None
    
    def ini_app(self,app):
        self.app = app
        self.connect()

    def connect(self):
        self.app.config['MYSQL_HOST'] = "mysql"
        self.app.config['MYSQL_USER'] = "root"
        self.app.config['MYSQL_PASSWORD'] = "my-secret-pw"
        self.app.config['MYSQL_DB'] = "inventory"

        return self.app


# def get_connection():
#     print("Connections")
#     app.app.config['MYSQL_HOST'] = "mysql"
#     app.app.config['MYSQL_USER'] = "root"
#     app.app.config['MYSQL_PASSWORD'] = "my-secret-pw"
#     app.app.config['MYSQL_DB'] = "inventory"

#     mysql = MySQL(app.app)

#     # cur = mysql.connection.cursor()
    
#     return mysql


