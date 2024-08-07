from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.states import AddCommandState


async def add_command_rout(message: types.Message, state: FSMContext) -> None:

    await message.answer('Enter new command')

    await state.set_state(AddCommandState.wait_add_command)
