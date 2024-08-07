from aiogram import types
from aiogram.types import FSInputFile
from datetime import datetime
from aiogram.exceptions import TelegramBadRequest
import logging


async def get_logs_rout(message: types.Message) -> None:

    full_file_name: str = f'secret_data/logs.txt'

    document: FSInputFile = FSInputFile(full_file_name)

    captions: str = f'before {datetime.now().strftime("%d-%m-%Y")}'

    try:

        await message.answer_document(document=document, caption=captions)

    except Exception as e:

        logging.error(e, exc_info=True)

        await message.answer('Logs are empty, enter /start and try again')

    return
