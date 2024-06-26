from aiogram import types
from aiogram.fsm.context import FSMContext


async def callbacks_connect_button(callback: types.CallbackQuery, state: FSMContext) -> None:

    action = callback.data

    match action:

        case 'connect':

            pass

        case 'select_connection':

            pass

        case 'delete_connection':

            pass
