from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from main_func.run_command import run_command


async def run_command_second_step(message: Message, state: FSMContext) -> None:

    is_one = await state.get_data()
    is_one = is_one['is_one']
    command = message.text.strip()

    result = await run_command(command)

    if command != '_stop':
        if result:
            await message.answer(f'```bash\n{result}```', parse_mode='markdownv2')
        else:
            await message.answer('`Empty message`', parse_mode='markdownv2')

    if is_one or command == '_stop':
        await message.answer('Stop entering commands')
        await state.clear()
    else:
        await message.answer('Enter new command')
