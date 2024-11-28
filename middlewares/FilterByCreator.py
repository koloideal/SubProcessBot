from aiogram.filters import BaseFilter
from aiogram.types import Message
from configparser import ConfigParser

config = ConfigParser()
config.read('secret_data/config.ini')

creator_id = int(config['Telegram']['creator_id'])


class FilterByCreator(BaseFilter):

    async def __call__(self, message: Message) -> bool:

        return creator_id == message.from_user.id
