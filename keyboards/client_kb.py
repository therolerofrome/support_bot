from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup

b1 = KeyboardButton('/новый тикет')
b2 = KeyboardButton('/мои тикеты')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)

kb_client.add(b1).add(b2)