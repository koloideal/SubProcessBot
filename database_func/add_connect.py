import sqlite3


async def add_connect(ssh_client_data: dict) -> None:

    try:

        user_id = ssh_client_data["id"]
        username = ssh_client_data["username"]
        password = ssh_client_data["password"]
        port = ssh_client_data["port"]
        host = ssh_client_data["host"]

        connection = sqlite3.connect("database/ssh_client_data.db")

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
        INSERT INTO connections(id, host, port, username, password)
        VALUES (?, ?, ?, ?, ?)
        ''', (user_id, host, port, username, password))

        connection.commit()

        cursor.close()
        connection.close()

    except sqlite3.Error as error:

        return error

    else:

        return
