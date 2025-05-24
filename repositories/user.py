from repositories.connection import get_connection

def validate_user(username: str, password: str, app_connection) -> bool:
    conn = get_connection(app_connection)
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()

    cursor.close()
    conn.close()

    return user is not None