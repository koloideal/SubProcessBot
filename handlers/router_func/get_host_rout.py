from aiogram import types
from aiogram.fsm.context import FSMContext


async def get_host_rout(message: types.Message, state: FSMContext) -> None:

    await message.answer(f'your host is {message.text.strip()}')

    await state.clear()
