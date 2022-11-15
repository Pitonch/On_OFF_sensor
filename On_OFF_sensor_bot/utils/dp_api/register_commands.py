from asyncpg import UniqueViolationError

from On_OFF_sensor_bot.utils.dp_api.schemas.registration import Registration


async def new_registration(user_id: int, tg_first_name: str, tg_last_name: str, name: str, age: str, phone: str, status: str):
    try:
        registration = Registration(user_id=user_id, tg_first_name=tg_first_name, tg_last_name=tg_last_name, name=name, age=age, phone=phone, status=status)
        await registration.create()
    except UniqueViolationError:
        print('Регистрация не создана')


async def select_registration():
    registration = await Registration.query.where(Registration.status == 'created').gino.first()
    return registration


async def select_registration_by_user_id(user_id: int):
    registration = await Registration.query.where(Registration.user_id == 'created').gino.first()
    return registration


async def accept_registration(user_id: int):
    registration = await select_registration_by_user_id(user_id)
    await registration.update(status='accepted').apply()
