import sqlite3
from sqlite3 import Connection, Cursor


async def get_allowed_users(return_username=False) -> list:

    connection: Connection = sqlite3.connect('database/allowed_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS allowed_users 
                     (id INTEGER,
                      username TEXT,
                      commands TEXT DEFAULT 'uname',
                      UNIQUE(id))''')

    connection.commit()

    if not return_username:

        cursor.execute('''SELECT id FROM allowed_users''')

    else:

        cursor.execute('''SELECT username FROM allowed_users''')

    allowed_users_id: list = [item[0] for item in cursor.fetchall()]

    connection.commit()

    cursor.close()
    connection.close()

    return allowed_users_id
