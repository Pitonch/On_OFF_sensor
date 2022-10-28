from aiogram import Bot, Dispatcher, types
from On_OFF_sensor_bot.data_ import config

# создаем переменную бота где Bot токен бота

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

# создаем диспетчер

dp = Dispatcher(bot)
