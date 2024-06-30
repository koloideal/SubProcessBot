from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from handlers.router_func.rout_connect import ConnectWait


async def wait_get_port(message: Message, state: FSMContext):

    port = message.text.strip()

    try:

        int(port)

    except ValueError:

        if port == '?exit':

            await message.answer('GoodBye')

            await state.clear()

        else:

            await message.answer('Port must be integer')

    else:

        await message.answer(f'Your port is <pre>{port}</pre>', parse_mode='HTML')

        await state.update_data({'port': port})

        await message.answer('For exit enter "<code>?exit</code>"\n'
                             'Enter the SSH client username')

        await state.set_state(ConnectWait.waiting_for_get_username)
