import sqlite3
from sqlite3 import Connection, Cursor


async def get_allowed_users() -> list:

    connection: Connection = sqlite3.connect('database/allowed_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS allowed_users 
                     (id int,
                      username varchar(50),
                      UNIQUE(id))''')

    connection.commit()

    cursor.execute('''SELECT id FROM allowed_users''')

    allowed_users_id: list = [ids[0] for ids in cursor.fetchall()]

    connection.commit()

    cursor.close()
    connection.close()

    return allowed_users_id
