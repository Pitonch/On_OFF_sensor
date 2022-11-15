from aiogram.dispatcher.filters.state import StatesGroup, State


class Registration(StatesGroup):
    name = State()
    phone = State()
    age = State()


class Accept(StatesGroup):
    user_id = State()

