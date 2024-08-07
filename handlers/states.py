from aiogram.fsm.state import StatesGroup, State


class AddAllowedUserState(StatesGroup):

    wait_username_add_allowed_user: State = State()


class DelAllowedUserState(StatesGroup):

    wait_username_del_allowed_user: State = State()


class AddCommandState(StatesGroup):

    wait_add_command: State = State()
