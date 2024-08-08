import logging
import sqlite3
from aiogram.types import CallbackQuery


async def del_command(callback: CallbackQuery) -> None:

    with sqlite3.connect('database/allowed_users.db') as connect:
        cursor = connect.cursor()
        cursor.execute('''SELECT commands FROM allowed_users WHERE id = ?''', (int(callback.from_user.id), ))
        results: str = cursor.fetchone()[0]
        commands = results.replace(callback.data[:-6]+';', '')
        cursor.execute('''UPDATE allowed_users SET commands = ? WHERE id = ?''', (commands, callback.from_user.id))
        cursor.close()

    logging.warning(f'Delete command')

    await callback.message.answer(f'Delete command {callback.data[:-6]}')


