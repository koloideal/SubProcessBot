from aiogram.filters import BaseFilter
from aiogram.types import Message
from database_func.get_allowed_users import get_allowed_users


class FilterByID(BaseFilter):

    async def __call__(self, message: Message) -> bool:

        get_allowed_users_id = await get_allowed_users()

        return message.from_user.id in get_allowed_users_id
