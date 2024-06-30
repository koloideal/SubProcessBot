import sqlite3
from aiogram.types import CallbackQuery


async def delete_connect(callback: CallbackQuery, callback_data) -> None:

    user_id = callback.from_user.id
    host = callback_data.host
    username = callback_data.username

    connection = sqlite3.connect("database/ssh_client_data.db")
    cursor = connection.cursor()

    cursor.execute('''
    DELETE FROM connections WHERE id = ? AND host = ? AND username = ?
    ''', (user_id, host, username))

    connection.commit()

    cursor.close()
    connection.close()

    await callback.message.answer('Successfully deleted connection')

    await callback.message.delete()
