from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.states import DelAllowedUserState


async def del_allowed_user_rout(message: types.Message, state: FSMContext) -> None:

    await message.answer('Enter username for delete allowed user')

    await state.set_state(DelAllowedUserState.wait_username_del_allowed_user)
