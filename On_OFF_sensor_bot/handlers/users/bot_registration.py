from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from On_OFF_sensor_bot.data_.config import admins_id
from On_OFF_sensor_bot.filters import IsPrivate
from On_OFF_sensor_bot.loader import dp
from On_OFF_sensor_bot.states.registration import Registration
from On_OFF_sensor_bot.utils.dp_api import register_commands, dp_gino



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


@dp.message_handler(IsPrivate(), state=Registration.phone)
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
    answer = message.text
    if answer.isnumeric():
        if int(answer) < 150:
            await state.update_data(age=answer)
            data = await state.get_data()
            name = data.get('name')
            phone = data.get('phone')
            age = data.get('age')
            await message.answer(f'Регистрация ОК\n'
                                 f'name: {name}\n'
                                 f'Age: {age}\n'
                                 f'Phone: {phone}\n'
                                 f'позвоним тебе по номеру {phone}')
        else:
            await message.answer('введите правльно возраст')
    else:
        await message.answer('введите правльно возраст целым числом')


@dp.message_handler(IsPrivate(), text='/registrations', user_id=admins_id)
async def get_reg(message: types.Message):
    rega = await register_commands.select_registration()
    await message.answer((f'Дата создания:' {}))


