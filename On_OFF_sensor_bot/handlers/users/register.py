from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from On_OFF_sensor_bot.loader import dp

from On_OFF_sensor_bot.states import Register


@dp.message_handler(Command('register'))  # /register будет работать вот это
async def register(message: types.Message):
    await message.answer('Привет, ты начал регистрацию, \nвведи свое имя')
    await Register.test1.set()  # ввод имени


@dp.message_handler(state=Register.test1)  # ловим сообщение по состоянию register.test1
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test1=answer)
    await message.answer('сколько тебе лет')
    await Register.test2.set()


@dp.message_handler(state=Register.test2)  # ловим сообщение по состоянию register.test1
async def state1(message: types.Message, state: FSMContext):
    answer = message.text

    await state.update_data(test2=answer)
    data = await state.get_data()
    name = data.get('test1')
    years = data.get('test2')
    await message.answer(f'регистрация завершена\n'
                         f'твое имя {name}\n'
                         f'тебе {years} лет')

    await state.finish()


