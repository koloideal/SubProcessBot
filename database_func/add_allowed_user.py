import sqlite3
from sqlite3 import Connection, Cursor
from aiogram import types
import logging


async def add_allowed_user(message: types.Message, user_id: int, user_username: str) -> None:

    connection: Connection = sqlite3.connect('database/allowed_users.db')
    cursor: Cursor = connection.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS allowed_users 
                      (id INTEGER,
                      username TEXT,
                      commands TEXT DEFAULT '',
                      UNIQUE(id))''')

    connection.commit()

    cursor.execute('''INSERT OR IGNORE INTO allowed_users 
                      (id, username, commands)
                      VALUES (?, ?, ?)''',
                   (user_id, user_username, None))

    connection.commit()

    cursor.close()
    connection.close()

    logging.warning(f'User @{user_username} is now an allowed user or already was')

    await message.answer(f'@{user_username} is now an allowed user or already was')
