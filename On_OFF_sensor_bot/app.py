async def on_startup(dp):

    import filters
    filters.setup(dp)
    import middlewares
    middlewares.setup(dp)

    from On_OFF_sensor_bot.loader import db
    from On_OFF_sensor_bot.utils.dp_api.dp_gino import on_startup
    print('подключение к БД postgresql')
    await on_startup(dp)

    # print('Удаление БД')
    # await db.gino.drop_all()

    print('Создание БД')
    await db.gino.create_all()
    print('Готово')



    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    from utils.set_bot_cammands import set_default_commands
    await set_default_commands(dp)
    print('Бот запущен')


if __name__ == '__main__':
    from aiogram import executor
    from On_OFF_sensor_bot.handlers import dp

    executor.start_polling(dp, on_startup=on_startup)

