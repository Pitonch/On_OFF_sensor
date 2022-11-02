import asyncio
from On_OFF_sensor_bot.data_ import config
from On_OFF_sensor_bot.utils.dp_api import quick_commands as commands
from On_OFF_sensor_bot.utils.dp_api.dp_gino import db


async def db_test():
    await db.set_bind(config.POSTGRES_URI)
    await db.gino.drop_all()
    await db.gino.create_all()

    await commands.add_user(1, 'papa', 'mama')
    # await commands.add_user(8678, 'dbv', '12')
    # await commands.add_user(75, 'asdgas', 'dsf')
    # await commands.add_user(5, 'xzcb', '147')
    # await commands.add_user(9783, 'zxb', '54')

    users = await commands.select_all_users()
    print(users)

    count = await commands.count_users()
    print(count)

    user = await commands.select_user(1)
    print(user)

    await commands.update_use_name(1, 'new name')
    print(user)


# loop = asyncio.get_running_loop()
asyncio.run(db_test())
