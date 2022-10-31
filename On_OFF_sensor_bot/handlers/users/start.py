from aiogram import types
from On_OFF_sensor_bot.loader import dp
from On_OFF_sensor_bot.filters import IsPrivate
from On_OFF_sensor_bot.utils.misc import rate_limit


@rate_limit(limit=10, key='/start')
@dp.message_handler(IsPrivate(), text='/start')
async def command_start(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'Твой ID: {message.from_user.id}')
