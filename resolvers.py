from db import get_connection

def resolve_players():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT username FROM user_info")
    result = cursor.fetchall()
    conn.close()
    return result