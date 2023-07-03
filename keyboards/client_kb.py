from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardMarkup

b1 = KeyboardButton('Новый тикет')
b2 = KeyboardButton('Мои тикеты')

b3 = KeyboardButton('Проблема')
b4 = KeyboardButton('Вопрос')
b5 = KeyboardButton('Отмена')

b6 = KeyboardButton('PROD')
b7 = KeyboardButton('DEV')
b8 = KeyboardButton('TEST')

b9 = KeyboardButton('ДемоСфера')

b10 = KeyboardButton('Без приоритета')
b11 = KeyboardButton('Низкий')
b12 = KeyboardButton('Средний')
b13 = KeyboardButton('Высокий')
b14 = KeyboardButton('Критический')


yes = KeyboardButton('Да')
no = KeyboardButton('Нет')


kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
kb_client_ticket = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_yn = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_cancel = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_environment = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_system = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client_priority = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

kb_client.add(b1).add(b2)
kb_client_ticket.add(b3).add(b4).add(b5)
kb_client_yn.add(yes).add(no)
kb_client_cancel.add(b5)
kb_client_environment.add(b6).add(b7).add(b8).add(b5)
kb_client_system.add(b9).add(b5)
kb_client_priority.add(b10).add(b11).add(b12).add(b13).add(b14).add(b5)







