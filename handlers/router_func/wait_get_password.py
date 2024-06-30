from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from database_func.add_connect import add_connect


async def wait_get_password(message: Message, state: FSMContext):

    password = message.text.strip()

    if password == '?exit':

        await message.answer('GoodBye')

        await state.clear()

    else:

        result_pswd = (password[0] + ('*' * (len(password)-2)) + password[-1]) if len(password) > 2 else len(password) * '*'

        await message.delete()

        await message.answer(f'Your password is <pre>{result_pswd}</pre>', parse_mode='HTML')

        await state.update_data({'password': password, 'id': message.from_user.id})

        ssh_client_data = await state.get_data()

        result = await add_connect(ssh_client_data)

        if not result:

            await message.answer('Connection successfully added')

            # await client_ssh()

        else:

            await message.answer(f'Something went wrong, error:'
                                 f'<pre>{result}</pre>', parse_mode='HTML')

            await state.clear()
