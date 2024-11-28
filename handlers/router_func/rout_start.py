from aiogram.types import Message
from database_func.get_allowed_users import get_allowed_users
from configparser import ConfigParser

config = ConfigParser()
config.read('secret_data/config.ini')

creator_id: int = int(config['Telegram']['creator_id'])


async def start_rout(message: Message) -> None:
    user_id: int = message.from_user.id

    allowed_users_id: list = await get_allowed_users()
    creator = user_id == creator_id
    allowed_user = (user_id in allowed_users_id) and (user_id != creator_id)
    not_allowed_user = (user_id not in allowed_users_id) and (user_id != creator_id)

    if creator:
        await message.answer(f"Hello, Creator\n\n"
                             f"What do you want to do today? 💭\n\n"
                             f"To run commands, click <b><i>/commands</i></b>👈\n\n"
                             f"To run command, press <b><i>/run_command</i></b> 👈\n\n"
                             f"Run commands in stream - <b><i>/run_commands</i></b> 👈\n\n"
                             f"Add command - <b><i>/add_command</i></b> 👈\n\n"
                             f"Del command - <b><i>/del_command</i></b> 👈\n\n"
                             f"----- Creator's Commands👇-----\n\n"
                             f"Add allowed user - <b><i>/add_user</i></b> 👈\n\n"
                             f"Delete allowed user - <b><i>/del_user</i></b> 👈\n\n"
                             f"Get logs - <b><i>/get_logs</i></b> 👈\n\n"
                             f"Drop logs - <b><i>/drop_logs</i></b> 👈\n\n"
                             f"Get allowed users - <b><i>/get_users</i></b> 👈"
                             f"\n\n\n<b><i>made by you 🫵</i></b>")

    elif allowed_user:
        await message.answer(f"Hello, I am a <b>SubProcessBot</b>🤖\n\n"
                             f"What do you want to do today? 💭\n\n"
                             f"To run commands, press <b><i>/commands</i></b> 👈\n\n"
                             f"To run command, press <b><i>/command</i></b> 👈\n\n"
                             f"Run commands in stream - <b><i>/run_commands</i></b> 👈\n\n"
                             f"Add command - <b><i>/add_command</i></b> 👈\n\n"
                             f"Del command - <b><i>/del_command</i></b> 👈"
                             f"\n\n\n<b><i>made by <a href='https://t.me/kolo_id '>kolo</a></i></b>",
                             disable_web_page_preview=True)

    elif not_allowed_user:
        await message.answer(f"Hello, I am a <b>SubProcessBot</b>🤖\n\n"
                             "<b>You do not have access to the bot, to get it write @kolo_id</b>"
                             f"\n\n\n<b><i>made by <a href='https://t.me/kolo_id '>kolo</a></i></b>",
                             disable_web_page_preview=True)
