from aiogram import types
from aiogram.fsm.context import FSMContext
from database_func.del_allowed_user import del_allowed_user
from database_func.get_allowed_users import get_allowed_users


async def get_username_for_del_allowed_user_rout(message: types.Message, state: FSMContext) -> None:

    allowed_users = await get_allowed_users(True)

    if message.text.strip() not in allowed_users:

        await message.answer('Invalid username')

        await state.clear()

    else:

        await del_allowed_user(message, message.text.strip())
