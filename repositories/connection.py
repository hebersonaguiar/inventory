import os
import pika
from flask_mysqldb import MySQL
from dotenv import load_dotenv

load_dotenv()


# ----------------------
# Conexão com MySQL
# ----------------------
def get_connection(app):
    app.config['MYSQL_HOST'] = os.getenv("DB_HOST")
    app.config['MYSQL_USER'] = os.getenv("DB_USER")
    app.config['MYSQL_PASSWORD'] = os.getenv("DB_PASSWORD")
    app.config['MYSQL_DB'] = os.getenv("DB_NAME")

    mysql = MySQL(app)
    
    return mysql

# ----------------------
# Conexão com RabbitMQ
# ----------------------
def get_rabbitmq_connection():
    credentials = pika.PlainCredentials(
        username=os.getenv("RABBITMQ_USER"),
        password=os.getenv("RABBITMQ_PASSWORD")
    )

    parameters = pika.ConnectionParameters(
        host=os.getenv("RABBITMQ_HOST"),
        port=int(os.getenv("RABBITMQ_PORT", 5672)),
        credentials=credentials
    )

    return pika.BlockingConnection(parameters)