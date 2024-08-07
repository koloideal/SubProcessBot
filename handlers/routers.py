from aiogram import types, Router
from aiogram.types import CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from database_func.add_command import add_command
from handlers.admin_router_func.wait_username_add_admin import get_username_for_add_admin_rout
from handlers.router_func.rout_add_command import add_command_rout
from handlers.router_func.rout_start import start_rout
from handlers.admin_router_func.add_allowed_user_rout import add_allowed_user_rout
from handlers.admin_router_func.get_logs_rout import get_logs_rout
from handlers.admin_router_func.get_users import get_users_bd_rout
from handlers.admin_router_func.drop_data import drop_data_rout
from midlwares.FilterByAllowedUser import FilterByAllowedUser
from midlwares.FilterByCreator import FilterByCreator
from handlers.states import AddAllowedUserState, AddCommandState

router: Router = Router()


@router.message(Command('start'))
async def start_routing(message: types.Message) -> None:
    await start_rout(message)


@router.message(FilterByAllowedUser(),
                Command('commands'))
async def connect_routing(message: types.Message) -> None:
    pass


@router.message(FilterByCreator(),
                Command('add_user'))
async def add_allowed_user_routing(message: types.Message, state: FSMContext) -> None:
    await add_allowed_user_rout(message, state)


@router.message(FilterByCreator(),
                Command('get_logs'))
async def get_logs_routing(message: types.Message) -> None:
    await get_logs_rout(message)


@router.message(FilterByCreator(),
                Command('get_users'))
async def get_users_bd_routing(message: types.Message) -> None:
    await get_users_bd_rout(message)


@router.message(FilterByCreator(),
                Command('drop_logs'))
async def drop_data_routing(message: types.Message) -> None:
    await drop_data_rout(message)


@router.message(FilterByAllowedUser(),
                Command('add_command'))
async def add_command_routing(message: types.Message, state: FSMContext) -> None:
    await add_command_rout(message, state)


@router.message(AddAllowedUserState.wait_username_allowed_user)
async def add_allowed_user_routing(message: types.Message, state: FSMContext) -> None:
    await get_username_for_add_admin_rout(message, state)


@router.message(AddCommandState.wait_add_command)
async def add_command_routing(message: types.Message, state: FSMContext) -> None:
    await add_command(message,state)


@router.message()
async def unknown_command(message: types.Message) -> None:
    await message.answer('Unknown command, enter /start')
