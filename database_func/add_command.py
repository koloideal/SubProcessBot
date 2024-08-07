import logging
import sqlite3
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


async def add_command(message: Message, state: FSMContext) -> None:

    command = message.text.strip()

    with sqlite3.connect('database/allowed_users.db') as connect:
        cursor = connect.cursor()
        cursor.execute('''SELECT commands FROM allowed_users WHERE id = ?''', (message.from_user.id, ))
        results = cursor.fetchone()[0]
        commands = results + ';' + command
        cursor.execute('''UPDATE allowed_users SET commands = ? WHERE id = ?''', (commands, message.from_user.id))
        cursor.close()

    await state.clear()

    logging.warning(f'Adding new command')

    await message.answer(f'Adding new command')


