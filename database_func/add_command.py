import sqlite3
from aiogram.fsm.context import FSMContext
from aiogram.types import Message


async def add_command(message: Message, state: FSMContext) -> None:

    command = str(message.text.strip().split())

    with sqlite3.connect('database/allowed_users.db') as connect:
        cursor = connect.cursor()
        cursor.execute('''SELECT commands FROM allowed_users WHERE id = ?''', (message.from_user.id, ))
        results = cursor.fetchone()
        results = results if results[0] else 'None'
        commands = ';'.join(list(results)) if results != 'None' else ''
        commands = (commands + ';' + command) if commands else command
        cursor.execute('''UPDATE allowed_users SET commands = ? WHERE id = ?''', (commands, message.from_user.id))
        cursor.close()

    await message.answer('Successful adding command')

    await state.clear()


