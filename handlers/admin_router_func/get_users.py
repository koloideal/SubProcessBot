from aiogram import types
from aiogram.types import FSInputFile
from datetime import datetime
import sqlite3
import json
import os


async def get_users_bd_rout(message: types.Message) -> None:

    with sqlite3.connect('database/allowed_users.db') as connect:
        cursor = connect.cursor()
        cursor.execute('''SELECT * FROM allowed_users''')
        all_users = cursor.fetchall()
        cursor.close()

    to_dump_data: dict = {}

    for user in all_users:
        to_dump_data[user[1]]: dict = {

            'user_id': user[0],
            'user_username': user[1],
            'commands': user[2]

        }

    full_file_name: str = f'secret_data/allowed_users.json'

    with open(full_file_name, 'w', encoding='utf8') as file:

        json.dump(to_dump_data, file, indent=4, ensure_ascii=False)

    document: FSInputFile = FSInputFile(full_file_name)

    await message.answer_document(document=document, caption=f'before {datetime.now().strftime("%d-%m-%Y")}')

    os.remove(full_file_name)

    return
