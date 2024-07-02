from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from database_func.add_connect import add_connect
from database_func.get_connects import get_connects
from main_func.ssh_client import ssh_client


async def wait_get_password(message: Message, state: FSMContext):

    password = message.text.strip()

    if password == '?exit':

        await message.answer('GoodBye')

        await state.clear()

    else:

        result_pswd = (password[0] + ('*' * (len(password)-2)) + password[-1]) \
            if len(password) > 2 else len(password) * '*'

        await message.delete()

        await message.answer(f'Your password is <pre>{result_pswd}</pre>', parse_mode='HTML')

        await state.update_data({'password': password, 'id': message.from_user.id})

        ssh_client_data = await state.get_data()

        being_connects = await get_connects(message.from_user.id)

        if_being_connect = False

        for connect in being_connects:

            if ssh_client_data['host'] == connect[1] and ssh_client_data['username'] == connect[3]:

                if_being_connect = True

                break

            else:

                continue

        if not if_being_connect:

            result = await add_connect(ssh_client_data)

            if not result:

                await message.answer('Connection successfully added')

                await ssh_client(message=message,
                                 host=ssh_client_data['host'],
                                 port=ssh_client_data['port'],
                                 username=ssh_client_data['username'],
                                 password=ssh_client_data['password'])

            else:

                await message.answer(f'Something went wrong, error:'
                                     f'<pre>{result}</pre>', parse_mode='HTML')

                await state.clear()

        else:

            await ssh_client(message=message,
                             host=ssh_client_data['host'],
                             port=ssh_client_data['port'],
                             username=ssh_client_data['username'],
                             password=ssh_client_data['password'])
