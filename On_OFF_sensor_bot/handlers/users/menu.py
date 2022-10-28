from aiogram.dispatcher.filters import Command
from aiogram import types

from On_OFF_sensor_bot.keyboards.default import kb_menu
from On_OFF_sensor_bot.loader import dp


@dp.message_handler(Command('menu'))
async def menu(message: types.Message):
    await message.answer('выбери число из меню ниже', reply_markup=kb_menu)