from aiogram import types

from On_OFF_sensor_bot.keyboards.default import kb_test
from On_OFF_sensor_bot.loader import dp


@dp.message_handler(text='TEXT2')
async def test(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'что про меню', reply_markup=kb_test)
