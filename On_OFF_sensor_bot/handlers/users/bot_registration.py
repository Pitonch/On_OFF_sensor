from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

from On_OFF_sensor_bot.data_.config import admins_id
from On_OFF_sensor_bot.filters import IsPrivate
from On_OFF_sensor_bot.keyboards.default import kb_menu
from On_OFF_sensor_bot.loader import dp
from On_OFF_sensor_bot.states import Accept
from On_OFF_sensor_bot.states.registration import Registration
from On_OFF_sensor_bot.utils.dp_api import register_commands, dp_gino


@dp.message_handler(text='Отменить регистрацию', state=[Registration.name, Registration.phone, Registration.age])
async def quit(message: types.Message, state: FSMContext):
    await state.finish()
    await message.answer('Регистрация отменена', reply_markup=kb_menu)


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
            await register_commands.new_registration(user_id=message.from_user.id,
                                                     tg_first_name=message.from_user.first_name,
                                                     tg_last_name=message.from_user.last_name,
                                                     name=name,
                                                     phone=phone,
                                                     age=age,
                                                     status='created')
            await message.answer(f'Регистрация ОК\n'
                                 f'name: {name}\n'
                                 f'Age: {age}\n'
                                 f'Phone: {phone}\n'
                                 f'позвоним тебе по номеру {phone}')
            await state.finish()
        else:
            await message.answer('введите правльно возраст')
    else:
        await message.answer('введите правльно возраст целым числом')


@dp.message_handler(IsPrivate(), text='/registrations', user_id=admins_id)
async def get_reg(message: types.Message):
    reg = await register_commands.select_registration()
    ikb = InlineKeyboardMarkup(row_width=1,
                               inline_keyboard=[
                                   [
                                       InlineKeyboardButton(text='Accept', callback_data='Accept')
                                   ]
                               ])
    await message.answer(f'Дата создания: {reg.created_at}\n'
                         f'id:{reg.user_id}\n'
                         f'Дата создания: {reg.tg_first_name}\n'
                         f'Дата создания: {reg.tg_last_name}\n'
                         f'Дата создания: {reg.name}\n'
                         f'Дата создания: {reg.phone}\n'
                         f'Дата создания: {reg.age}\n',
                         reply_markup=ikb)


@dp.callback_query_handler(text='Accept')
async def accept(call: types.CallbackQuery):
    await call.message.answer(f'Insert id')
    await Accept.user_id.set()


@dp.message_handler(state=Accept.user_id)
async def accept(message: types.Message, state: FSMContext):
    await register_commands.accept_registration(int(message.text))
    await message.answer(f"It's ok: {message.text}")
    await state.finish()


