from aiogram import types
from aiogram.types import CallbackQuery

from On_OFF_sensor_bot.keyboards.default import kb_test
from On_OFF_sensor_bot.keyboards.inline import ikb_menu, ikb_menu2
from On_OFF_sensor_bot.loader import dp


@dp.message_handler(text='Inline menu')
async def show_inline_menu(message: types.Message):
    await message.answer(f'Inline buttons below', reply_markup=ikb_menu)


@dp.callback_query_handler(text='Massage')
async def send_message(call: CallbackQuery):
    await call.message.answer('Кнопки заменены', reply_markup=kb_test)


@dp.callback_query_handler(text='alert')
async def send_message(call: CallbackQuery):
    await call.answer('Кнопки заменены', show_alert=True)  #show_alert=True показывает алерт под ОК, без этого просто сообщение


# кнопки2

@dp.callback_query_handler(text='кнопки2')
async def send_message(call: CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu2)
