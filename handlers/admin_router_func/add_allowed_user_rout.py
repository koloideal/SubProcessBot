from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.states import AddAllowedUserState


async def add_allowed_user_rout(message: types.Message, state: FSMContext) -> None:

    await message.answer('Enter username for adding allowed user')

    await state.set_state(AddAllowedUserState.wait_username_add_allowed_user)
