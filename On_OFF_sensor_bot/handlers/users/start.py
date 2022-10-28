from aiogram import types
from On_OFF_sensor_bot.loader import dp


@dp.message_handler(text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'Твой ID: {message.from_user.id}')
