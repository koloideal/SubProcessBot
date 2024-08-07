from aiogram import types
from aiogram.fsm.context import FSMContext
from configparser import ConfigParser
from telethon.sync import TelegramClient
from telethon.errors.rpcerrorlist import UsernameInvalidError
from database_func.add_allowed_user import add_allowed_user
from telethon.helpers import TotalList


config: ConfigParser = ConfigParser()
config.read("secret_data/config.ini")


api_id: str = config['Telegram']['api_id']
api_hash: str = config['Telegram']['api_hash']


client: TelegramClient = TelegramClient('session', int(api_id), api_hash)


async def get_username_for_add_admin_rout(message: types.Message, state: FSMContext) -> None:

    try:

        await client.start()

        if message.text.startswith('t.me/') or message.text.startswith('https://t.me/'):

            raise ValueError

        future_allowed_user_username: str = message.text.strip() if message.text[0] != '@' else message.text[1:].strip()

        user: TotalList = await client.get_participants(future_allowed_user_username)

        if user[0].bot or len(user) != 1:

            raise ValueError

    except (UsernameInvalidError, ValueError):

        await message.answer('Invalid username')

    else:

        user_username: str = future_allowed_user_username
        user_id: int = int(user[0].id)

        await add_allowed_user(message=message,
                               user_username=user_username,
                               user_id=user_id)

    finally:

        await client.disconnect()

        await state.clear()

    return
