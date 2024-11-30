from aiogram.types import Message
import os


async def drop_logs_rout(message: Message) -> None:
    os.remove("secret_data/logs.txt")

    await message.answer("Successful delete logs")

    return
