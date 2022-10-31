from aiogram import types
from On_OFF_sensor_bot.loader import dp


@dp.message_handler(text='10')
async def buttons_test(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'выбрал {message.text}')


@dp.message_handler(text='20')
async def buttons_test(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'выбрал {message.text}')


@dp.message_handler(text='100')
async def buttons_test(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'выбрал {message.text}')

