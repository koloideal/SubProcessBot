from aiogram.types import CallbackQuery
from main_func.run_command import run_command


async def run_buttons(callback: CallbackQuery):

    result = await run_command(callback.data[:-6])

    if result:

        await callback.message.answer(f'```bash\n{result}```', parse_mode='markdownv2')

    else:

        await callback.message.answer('`Empty message`', parse_mode='markdownv2')


