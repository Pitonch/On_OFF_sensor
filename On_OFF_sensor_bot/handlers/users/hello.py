from aiogram import types
from On_OFF_sensor_bot.loader import dp


@dp.message_handler(text='/hello')
async def command_hello(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!')
