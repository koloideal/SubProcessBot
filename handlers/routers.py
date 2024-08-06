from aiogram import types, F, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from handlers.router_func.rout_connect import AdminState, button_to_connect_rout
from handlers.router_func.rout_help import button_to_help_rout
from handlers.router_func.rout_start import start_rout
from handlers.admin_router_func.add_admin_rout import add_admin_rout
from handlers.admin_router_func.get_logs_rout import get_logs_rout
from handlers.admin_router_func.get_bd_with_users import get_users_bd_rout
from handlers.admin_router_func.drop_data import drop_data_rout
from midlwares.FilterByID import FilterByID

router: Router = Router()


@router.message(Command('start'))
async def start_routing(message: types.Message) -> None:
    await start_rout(message)


@router.message(FilterByID(),
                Command('commands'))
async def connect_routing(message: types.Message) -> None:
    await button_to_connect_rout(message)


@router.message(Command('add_user'))
async def add_admin_routing(message: types.Message, state: FSMContext) -> None:
    await add_admin_rout(message, state)


@router.message(Command('get_logs'))
async def get_logs_routing(message: types.Message) -> None:
    await get_logs_rout(message)


@router.message(Command('get_users'))
async def get_users_bd_routing(message: types.Message) -> None:
    await get_users_bd_rout(message)


@router.message(F.text == 'drop_logs')
async def drop_data_routing(message: types.Message) -> None:
    await drop_data_rout(message)


@router.message()
async def unknown_command(message: types.Message) -> None:
    await message.answer('Unknown command, enter /start')
