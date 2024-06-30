from aiogram import types
from aiogram.fsm.context import FSMContext
from handlers.router_func.rout_connect import ConnectWait
from main_func.get_wi_fi_ssid import get_ssid
from database_func.get_connects import get_connects
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData


class SelectConnectOrDeleteData(CallbackData, prefix="my", sep="#"):
    host: str
    port: str
    username: str
    password: str
    action: str


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

            connects = await get_connects(user_id=callback.from_user.id)

            buttons = []

            if connects:

                for connect in connects:
                    host, port, username, password = connect[1:]

                    callback_data = SelectConnectOrDeleteData(host=host,
                                                              port=port,
                                                              username=username,
                                                              password=password,
                                                              action='connect').pack()

                    buttons.append([InlineKeyboardButton(text=host + ' / ' + username, callback_data=callback_data)])

                keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=buttons)

                await callback.message.answer('Select connection to connect', reply_markup=keyboard)

            else:

                await callback.message.answer('No such')

        case 'delete_connection':

            connects = await get_connects(user_id=callback.from_user.id)

            buttons = []

            if connects:

                for connect in connects:
                    host, port, username, password = connect[1:]

                    callback_data = SelectConnectOrDeleteData(host=host,
                                                              port=port,
                                                              username=username,
                                                              password=password,
                                                              action='delete').pack()

                    buttons.append([InlineKeyboardButton(text=host + ' / ' + username, callback_data=callback_data)])

                keyboard: InlineKeyboardMarkup = InlineKeyboardMarkup(inline_keyboard=buttons)

                await callback.message.answer('Select connection to delete', reply_markup=keyboard)
