from aiogram import types
from aiogram.fsm.context import FSMContext
import re
from handlers.router_func.rout_connect import ConnectWait


async def get_host_rout(message: types.Message, state: FSMContext) -> None:

    ip = message.text.strip()

    is_local_ip = bool(re.match(r"^192\.168\.[0-9]{1,3}\.[0-9]{1,3}$", ip))

    if ip == '?exit':

        await message.answer('GoodBye')

        await state.clear()

    elif is_local_ip:

        await message.answer(f'Your host is <pre>{ip}</pre>')

        await state.update_data({'host': ip})

        await message.answer('For exit enter "<code>?exit</code>"\n'
                             'Enter port, default is <pre>21</pre>', parse_mode='HTML')

        await state.set_state(ConnectWait.waiting_for_get_port)

    else:

        await message.answer('Entered string is not a local ip in the range'
                             ' <pre>192.168.0.0 - 192.168.255.255</pre>')
