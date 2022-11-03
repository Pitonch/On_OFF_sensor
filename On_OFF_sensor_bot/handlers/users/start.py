from aiogram import types
from On_OFF_sensor_bot.loader import dp
from On_OFF_sensor_bot.filters import IsPrivate
from On_OFF_sensor_bot.utils.misc import rate_limit


@rate_limit(limit=10, key='/start')
@dp.message_handler(IsPrivate(), text='/start')  # ловит команду start
async def command_start(message: types.Message):  # создаем асинхронную функцию
    # отправляем сообщение пользователю
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'Твой ID: {message.from_user.id}')
