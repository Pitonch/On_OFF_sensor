from aiogram import types
from On_OFF_sensor_bot.loader import dp
from On_OFF_sensor_bot.filters import IsPrivate
from On_OFF_sensor_bot.utils.misc import rate_limit
from On_OFF_sensor_bot.utils.dp_api import quick_commands as commands


@rate_limit(limit=10, key='/start')
@dp.message_handler(IsPrivate(), text='/start')  # ловит команду start
async def command_start(message: types.Message):  # создаем асинхронную функцию
    try:
        user = await commands.select_user(message.from_user.id)
        if user.status == 'active':
            await message.answer(f'Привет {user.first_name}\n'
                                 f'Ты уже зарегестрирован')
        elif user.status == 'baned':
            await message.answer('ты забанен')
    except Exception:
        await commands.add_user(user_id=message.from_user.id,
                                first_name=message.from_user.first_name,
                                last_name=message.from_user.last_name,
                                username=message.from_user.username,
                                status='active')
        await message.answer('Ты успешно зарегестрирован')


@rate_limit(limit=10)
@dp.message_handler(IsPrivate(), text='/ban')  # ловит команду ban
async def get_ban(message: types.Message):  # создаем асинхронную функцию
    await commands.update_status(user_id=message.from_user.id, status='baned')
    await message.answer('Ты забанен')


@rate_limit(limit=10)
@dp.message_handler(IsPrivate(), text='/unban')  # ловит команду ban
async def get_unban(message: types.Message):  # создаем асинхронную функцию
    await commands.update_status(user_id=message.from_user.id, status='active')
    await message.answer('Ты разбанен')


@rate_limit(limit=10)
@dp.message_handler(IsPrivate(), text='/profile')  # ловит команду ban
async def profile(message: types.Message):  # создаем асинхронную функцию
    user = await commands.select_user(message.from_user.id)
    await message.answer(f'ID: {user.user_id}\n'
                         f'first_name: {user.first_name}\n'
                         f'last_name: {user.last_name}\n'
                         f'username: {user.username}\n'
                         f'status: {user.status}')
