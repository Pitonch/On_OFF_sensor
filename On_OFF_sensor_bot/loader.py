from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from On_OFF_sensor_bot.data_ import config

# создаем переменную бота где Bot токен бота
from On_OFF_sensor_bot.utils.dp_api.dp_gino import db

bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)

storage = MemoryStorage()

# создаем диспетчер

dp = Dispatcher(bot, storage=storage)  # подключили хранилище к диспетчеру  storage=storage


__all__ = ['bot', 'storage', 'dp', 'db']
