from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.router_func.rout_connect import ConnectWait
from main_func.get_wi_fi_ssid import get_ssid


ssid = get_ssid()


async def callbacks_connect_button(callback: types.CallbackQuery, state: FSMContext) -> None:

    action = callback.data

    match action:

        case 'connect':

            await callback.message.answer(f'Your server must be on this network: <pre>{ssid}</pre>',
                                          parse_mode='HTML')

            await callback.message.answer('For exit enter "<code>?exit</code>"\n'
                                          'Enter host, for example: <pre>192.168.0.200</pre>',
                                          parse_mode='HTML')

            await state.set_state(ConnectWait.waiting_for_get_host)

        case 'select_connection':

            pass

        case 'delete_connection':

            pass
