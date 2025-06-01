import mysql.connector
from mysql.connector import Error
from app.config.settings import settings

def get_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host=settings.DB_HOST,
            user=settings.DB_USER,
            password=settings.DB_PASSWORD,
            database=settings.DB_NAME
        )
        return connection
    except Error as e:
        print(f"Erro ao conectar no MySQL: {e}")
        raise
