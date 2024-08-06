import sqlite3


async def get_connects(user_id) -> list:

    connection = sqlite3.connect('database/ssh_client_data.db')
    cursor = connection.cursor()

    cursor.execute('''
            CREATE TABLE IF NOT EXISTS connections(
            id INTEGER,
            host TEXT NOT NULL,
            port TEXT NOT NULL,
            username TEXT NOT NULL,
            password TEXT NOT NULL
            )''')

    connection.commit()

    cursor.execute('''
    SELECT * FROM connections WHERE id = ?
    ''', (int(user_id), ))

    connects = cursor.fetchall()

    cursor.close()
    connection.close()

    return connects
