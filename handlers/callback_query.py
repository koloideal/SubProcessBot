from aiogram.types import CallbackQuery
from database_func.del_command import del_command
from database_func.get_commands import get_commands
from handlers.router_func.rout_run_commands import create_dynamic_keyboard


async def callback_query(callback: CallbackQuery):
    await del_command(callback)
    commands = await get_commands(callback.from_user.id)
    keyboard = await create_dynamic_keyboard(commands, True)
    await callback.message.edit_reply_markup(reply_markup=keyboard)

