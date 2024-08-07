from aiogram import types
import os


async def drop_logs_rout(message: types.Message) -> None:

    os.remove('secret_data/logs.txt')

    await message.answer('Successful delete logs')

    return
