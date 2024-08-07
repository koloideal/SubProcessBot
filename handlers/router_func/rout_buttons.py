from aiogram.types import CallbackQuery
from main_func.run_command import run_command


async def buttons(callback: CallbackQuery):

    result = await run_command(callback.data.strip())

    await callback.message.answer(f'```bash\n{result}```', parse_mode='markdownv2')


