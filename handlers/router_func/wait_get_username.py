from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from handlers.router_func.rout_connect import ConnectWait


async def wait_get_username(message: Message, state: FSMContext):

    username = message.text.strip()

    if username == '?exit':

        await message.answer('GoodBye')

        await state.clear()

    else:

        await message.answer(f'Your username is <pre>{username}</pre>', parse_mode='HTML')

        await state.update_data({'username': username})

        await message.answer('For exit enter "<code>?exit</code>"\n'
                             'Enter the SSH client password')

        await state.set_state(ConnectWait.waiting_for_get_password)
