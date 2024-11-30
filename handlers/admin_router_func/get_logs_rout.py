from aiogram.types import Message
from aiogram.types import FSInputFile
from datetime import datetime
import logging


async def get_logs_rout(message: Message) -> None:

    full_file_name: str = 'secret_data/logs.txt'
    document: FSInputFile = FSInputFile(full_file_name)
    captions: str = f'before {datetime.now().strftime("%d-%m-%Y")}'

    try:
        await message.answer_document(document=document, caption=captions)

    except Exception as e:
        logging.error(e, exc_info=True)
        await message.answer('Logs are empty, enter /start and try again')
