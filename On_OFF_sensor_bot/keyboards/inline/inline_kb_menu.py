from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# колличество кнопок в ряду

ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Massage', callback_data='Massage'),
                                        InlineKeyboardButton(text='URL', url='https://www.youtube.com/watch?v=2Il_Ab-s0W8&list=PLPELDof3v08efHGT3gVLPCXG5cKRo50Nn&index=5&ab_channel=Redly')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Alert', callback_data='alert'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='заменить кнопки', callback_data='кнопки2'),
                                    ]

                                ])


