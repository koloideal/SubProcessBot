from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.fsm.state import StatesGroup, State
from database_func.get_banned_users import get_banned_users
from handlers.router_func.rout_start import creator_id


class ConnectWait(StatesGroup):
    waiting_for_get_host: State = State()
    waiting_for_get_port: State = State()
    waiting_for_get_password: State = State()
    waiting_for_get_username: State = State()


class AdminState(StatesGroup):
    waiting_for_add_admin: State = State()
    waiting_for_del_admin: State = State()
    waiting_for_ban_user: State = State()
    waiting_for_unban_user: State = State()


async def button_to_connect_rout(message: Message) -> None:
    user_id: int = message.from_user.id

    banned_users: list = await get_banned_users()

    if (user_id in banned_users) and (user_id != creator_id):

        await message.answer(f"You can't use the bot."
                             f"\n\n<u><b>You were blocked</b></u>"
                             f"\n\n\nAbout the unban - <a href='https://t.me/kolo_id'>kolo</a>",
                             disable_web_page_preview=True)

    else:

        connect: InlineKeyboardButton = InlineKeyboardButton(text='Connect',
                                                             callback_data='connect')

        select_connection: InlineKeyboardButton = InlineKeyboardButton(text='Select connection',
                                                                       callback_data='select_connection')

        delete_connection: InlineKeyboardButton = InlineKeyboardButton(text='Delete connection',
                                                                       callback_data='delete_connection')

        buttons: list = [

            [connect, select_connection],
            [delete_connection]

        ]

        keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=buttons)

        await message.answer('<b>Select the necessary button</b>', reply_markup=keyboard)

    return
