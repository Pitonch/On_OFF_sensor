from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='10'),
            KeyboardButton(text='20'),
        ],
        [
            KeyboardButton(text='100'),
        ],
        [
            KeyboardButton(text='Inline menu'),
            KeyboardButton(text='TEXT2'),
            KeyboardButton(text='TEXT3'),
        ]
    ],
    resize_keyboard=True
)
