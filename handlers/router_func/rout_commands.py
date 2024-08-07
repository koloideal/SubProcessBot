from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State


class AllowedUserState(StatesGroup):
    waiting_for_add_command: State = State()


class CreatorState(StatesGroup):
    waiting_for_add_allowed_user: State = State()
    waiting_for_del_allowed_user: State = State()


async def commands_buttons_rout(message: Message) -> None:



    return
