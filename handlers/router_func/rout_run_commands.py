from aiogram.types import Message, InlineKeyboardMarkup
from aiogram.types import InlineKeyboardButton
from database_func.get_commands import get_commands


MAX_ROW_LENGTH = 20


async def create_dynamic_keyboard(button_texts, delete=False):
    keyboard = []
    row = []
    current_row_length = 0

    for text in button_texts:
        button = InlineKeyboardButton(text=text, callback_data=text+'TO_RUN' if not delete else text+'TO_DEL')
        if current_row_length + len(text) > MAX_ROW_LENGTH:
            keyboard.append(row)
            row = []
            current_row_length = 0
        row.append(button)
        current_row_length += len(text)

    if row:
        keyboard.append(row)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)


async def commands_buttons_rout(message: Message) -> None:

    commands = await get_commands(message.from_user.id)

    keyboard = await create_dynamic_keyboard(commands)

    await message.answer(
        "Your commands, press it to run",
        reply_markup=keyboard
    )
