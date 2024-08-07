import sqlite3
from sqlite3 import Connection, Cursor
from aiogram import types
import logging


async def del_allowed_user(message: types.Message, user_username: str) -> None:

    connection: Connection = sqlite3.connect('database/allowed_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS allowed_users 
                      (id INTEGER,
                      username TEXT,
                      commands TEXT DEFAULT '',
                      UNIQUE(id))''')

    connection.commit()

    cursor.execute('''DELETE FROM allowed_users WHERE username = ?''', (user_username, ))

    connection.commit()

    cursor.close()
    connection.close()

    logging.warning(f'User @{user_username} is now not allowed user')

    await message.answer(f'@{user_username} is now not allowed user')
