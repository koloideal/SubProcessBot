from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from ..states import RunCommandState


async def run_command_rout(message: Message, state: FSMContext, is_one=True) -> None:

    await message.answer(
        "Enter command for run now:"
    )
    await state.update_data({'is_one': is_one})
    await state.set_state(RunCommandState.wait_run_command)