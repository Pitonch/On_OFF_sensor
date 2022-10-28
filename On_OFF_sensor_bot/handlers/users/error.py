from aiogram import types
from On_OFF_sensor_bot.loader import dp


@dp.message_handler()
async def command_error(message: types.Message):
    await message.answer(f'Команды {message.text} не найден')

