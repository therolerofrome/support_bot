from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup

b1 = KeyboardButton('Новый тикет')
b2 = KeyboardButton('Мои тикеты')

b3 = KeyboardButton('Проблема')
b4 = KeyboardButton('Вопрос')
b5 = KeyboardButton('Отмена')

yes = KeyboardButton('Да')
no = KeyboardButton('Нет')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb_client_ticket = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_yn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2)
kb_client_ticket.add(b3).add(b4).add(b5)
kb_client_yn.add(yes).add(no)

