from aiogram.filters import BaseFilter
from aiogram.types import Message
from database_func.get_allowed_users import get_allowed_users
from configparser import ConfigParser

config = ConfigParser()
config.read('secret_data/config.ini')

creator_id = int(config['Telegram']['creator_id'])


class FilterByAllowedUser(BaseFilter):

    async def __call__(self, message: Message) -> bool:

        get_allowed_users_id = await get_allowed_users()

        return (message.from_user.id in get_allowed_users_id) or (creator_id == message.from_user.id)
