from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from On_OFF_sensor_bot.filters import IsPrivate
from On_OFF_sensor_bot.loader import dp
from On_OFF_sensor_bot.states.registration import Registration


@dp.message_handler(IsPrivate(), Command('register'))
async def bot_register(message: types.Message):
    name = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text=f'{message.from_user.full_name}')
            ],
            [
                KeyboardButton(text='отменить регистрацию')
            ],
            ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer(f'Привет\n'
                         f'для регистрации введи свое имя:', reply_markup=name
                         )
    await Registration.name.set()

@dp.message_handler(IsPrivate(), state=Registration.name)
async def get_name(message: types.Message, state=FSMContext):
    answer = message.text
    await state.update_data(name=answer)
    phone = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='отменить регистрацию')
            ],
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer(f'<b>{answer}</b>, пришли номер телефона', reply_markup=phone)
    await Registration.phone.set()


@dp.message_handler(IsPrivate(), state=Registration.name)
async def get_phone(message: types.Message, state=FSMContext):
    answer = message.text
    markup = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text='отменить регистрацию')
            ],
        ],
        resize_keyboard=True,
    )
    try:
        if answer.replace('+', '').isnumeric():
            await state.update_data(phone=answer)

            await message.answer('теперь введи возраст, целым числом', reply_markup=markup)
            await Registration.age.set()
        else:
            await message.answer('введи корректный номер телефона', reply_markup=markup)
    except Exception:
        await message.answer('введи корректный номер телефона', reply_markup=markup)


@dp.message_handler(IsPrivate(), state=Registration.age)
async def get_age(message: types.Message, state=FSMContext):
    answer = message.text()
    if answer.isnumeric():
        if int(answer) < 150:
            await state.update_data(age=answer)

