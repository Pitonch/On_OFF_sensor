# from aiogram import Bot, Dispatcher, types
# from aiogram.utils import executor
# from config_reader import TOKEN
# # from config_reader import config
#
# bot = Bot(token=TOKEN)
# # bot = Bot(token=config.bot_token.get_secret_value())
# dp = Dispatcher(bot)
#
# # реагировать боту на команду /start
#
# # @dp.message_handler( если пусто то все сообщения принимает )
#
#
# @dp.message_handler(commands=['start'])
# async def process_start_command(message: types.Message):
#     await message.answer("Привет!\nДобро пожаловать в дом")  # answer не повторяет вопрос
#
#
# @dp.message_handler(commands=['help'])
# async def process_start_command(message: types.Message):
#     await message.reply("Смотри, что я могу")  # reply повторяет вопрос
#
#
# @dp.message_handler(commands=["dice"])
# async def cmd_dice(message: types.Message):
#     await message.answer_dice(emoji="🎲")
#
#
# @dp.message_handler(commands=["text"])
# async def cmd_text(message: types.Message):
#     text = f'hello {message.from_user.full_name}'
#     await message.answer(text=text)
#     print(message.text)
#     print(message.from_user)
#
#
# # тип обрабатываемого сообщения только текстовые,поэтому скобки на первой строчке остаются пустыми
#
#
# # @dp.message_handler()
# # async def echo_message(msg: types.Message):
# #     await bot.send_message(msg.from_user.id, msg.text)
#
#
# # постоянно смотрит сообщения
#
#
# if __name__ == '__main__':
#     executor.start_polling(dp)
