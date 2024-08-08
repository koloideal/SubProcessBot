from aiogram.types import Message
from handlers.router_func.rout_run_commands import create_dynamic_keyboard
from database_func.get_commands import get_commands


async def del_commands_buttons_rout(message: Message) -> None:

    commands = await get_commands(message.from_user.id)

    keyboard = await create_dynamic_keyboard(commands, True)

    await message.answer(
        "Your commands, press it to **delete**",
        reply_markup=keyboard,
        parse_mode='markdownv2'
    )
