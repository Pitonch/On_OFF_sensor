import pathlib
from aiogram.types import ContentType, Message, InputFile
from pathlib import Path

from On_OFF_sensor_bot.loader import dp


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_photo_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)


@dp.message_handler(content_types=ContentType.VIDEO)
async def send_video_file_id(message: Message):
    await message.reply(message.video[-1].file_id)


@dp.message_handler(text='/photo')
async def send_photo(message: Message):
    chat_id = message.from_user.id
    photo_file_id = 'AgACAgIAAxkBAAIBPmNfxCwBkRjW1CiePTb8v3X_VDhsAAJdwDEbZuEAAUtJtZSrcOGmRAEAAwIAA20AAyoE'
    path = Path(__file__).parent.parent.parent.parent / 'media' /'images' / 'sensor.png'
    print(path)
    photo_bytes = InputFile(path_or_bytesio=path)  #'D:\it\On_OFF_sensor\media\images\sensor.png'
    video_file_id = ''

    # await dp.bot.send_photo(chat_id=chat_id, photo=photo_file_id)
    await dp.bot.send_photo(chat_id=chat_id, photo=photo_bytes)
    # await dp.bot.send_video(chat_id=chat_id, video=video_file_id)
