from aiogram.fsm.state import StatesGroup, State


class AddAllowedUserState(StatesGroup):

    wait_username_allowed_user: State = State()


class AddCommandState(StatesGroup):

    wait_add_command: State = State()
