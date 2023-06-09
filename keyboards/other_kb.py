from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton, \
    InlineKeyboardMarkup

b1 = KeyboardButton('Предоставить доступ', request_contact=True, callback_data='allow_contact')







kb_other=ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)





kb_other.add(b1)
