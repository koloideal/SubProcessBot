import sqlite3
import re


async def get_commands(user_id) -> list:

    with sqlite3.connect('database/allowed_users.db') as connection:

        cursor = connection.cursor()

        cursor.execute('''
                CREATE TABLE IF NOT EXISTS allowed_users(
                id INTEGER,
                username TEXT NOT NULL,
                commands TEXT DEFAULT 'uname;'
                )''')

        connection.commit()

        cursor.execute('''SELECT commands FROM allowed_users WHERE id = ?''', (user_id, ))
        commands = cursor.fetchone()[0]

        commands = commands[:-1].split(';')

        cursor.close()

    return commands
