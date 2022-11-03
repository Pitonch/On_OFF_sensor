from asyncpg import UniqueViolationError

from On_OFF_sensor_bot.utils.dp_api.dp_gino import db
from On_OFF_sensor_bot.utils.dp_api.schemas.user import User


async def add_user(user_id: int, name: str, update_name: str):
    try:
        user = User(user_id=user_id, name=name, update_name=update_name)
        await user.create()
    except UniqueViolationError:
        print('нет пользователя')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_users():
    count = await db.func.count(User.user_id).gino.scalar()
    return count


async def select_user(user_id):
    user = await User.query.where(User.user_id == user_id).gino.first()
    return user


async def update_user_name(user_id, new_name):
    user = await select_user(user_id)
    await user.update(update_name=new_name).apply()
