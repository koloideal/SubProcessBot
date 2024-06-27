from aiogram import types
from aiogram.fsm.context import FSMContext
from main_func.get_wi_fi_ssid import get_ssid
from handlers.router_func.rout_connect import ConnectWait


async def callbacks_connect_button(callback: types.CallbackQuery, state: FSMContext) -> None:

    action = callback.data

    ssid = get_ssid()

    match action:

        case 'connect':

            await callback.answer(f'Your server must be on this network: {ssid}')

            await callback.message.answer('Enter host, for example: 192.168.0.200')

            await state.set_state(ConnectWait.waiting_for_get_host)

        case 'select_connection':

            pass

        case 'delete_connection':

            pass
