from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
#from data_base import sqlite_db

from .validators import is_valid_email

from create_bot import dp, bot

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, CallbackQuery
from aiogram.dispatcher.filters import Text

from keyboards.client_kb import kb_client, kb_client_ticket, kb_client_yn
from keyboards.other_kb import kb_other



class NewTicket(StatesGroup):
    product = State() # Какой продукт
    summary = State() # Проблема или вопрос по функционал
    description = State() # Описание вопроса
    photo = State() # Скриншоты если надо



"""   Знакомство с новым пользователем   """

class GetEmail(StatesGroup):
    waiting_for_email = State()
    #ID = State()
async def commands_start(message: types.Message):
    try:
        await message.answer("Привет! Я бот. Для работы мне нужен доступ к вашему контакту. Разрешить?",
                         reply_markup=kb_other)
    except:
        pass


async def process_callback_allow_contact(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Отлично! Теперь мне нужен ваш e-mail.", reply_markup=types.ReplyKeyboardRemove())
    await GetEmail.waiting_for_email.set()


async def process_email_step(message: types.Message, state: FSMContext):
    if is_valid_email(message.text) == True:
        async with state.proxy() as data:
            email = message.text
            id = message.from_user.id
            await state.finish()
        await message.answer(f"Спасибо, я сохранил ваш email: {email} id: {id}", reply_markup=kb_client)
    else:
        await message.answer("Email введен не правильно")





"""  Мои тикеты   """

async def my_ticket(message: types.Message):
    await bot.send_message(message.from_user.id, 'Находится в разработке...', reply_markup=kb_client)


""" Создание тикета"""
#Начало диалога создания тикета
async def create_new_ticket(message: types.Message):
    await bot.send_message(message.from_user.id, 'Напишите продукт', reply_markup=types.ReplyKeyboardRemove())
    await NewTicket.product.set()


#Выход из состояния
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await message.reply('ОК')

#Ловим первый ответ и пишем в словарь
async def load_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['product'] = message.text
    await NewTicket.next()
    await message.reply('У вас проблема или вопрос по функционалу?', reply_markup=kb_client_ticket)

#Ловим второй ответ
async def load_summary(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['summary'] = message.text
    await NewTicket.next()
    await message.reply('Опишите свой вопрос или проблему')

#Ловим третий ответ
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await NewTicket.next()
    return await message.reply('Вам нужно загрузить скриншоты?', reply_markup=kb_client_yn)

#Ловим "да"
async def answer_yes(message: types.Message):
    await bot.send_message(message.from_user.id, 'Загрузите от 1 до 10 картинки')

#Ловим "Фото"
async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = [photo.file_id for photo in message.photo] # Сохраняет ID фотографии.
        ### Код для скачивания файлов###
        # file = await bot.get_file(message.photo[-1].file_id)
        # await message.photo[-1].download(file_.file_path.split('photos/')[1])
    await bot.send_message(message.from_user.id, 'Тикет успешно создан!', reply_markup=kb_client)
    #await sqlite_db.sql_add_command(state)
    await state.finish()

#Ловим не правильный тип данных
async def incorrect_type(message: types.Message, state: FSMContext):
    await bot.send_message(message.from_user.id, 'Нужно загрузить фотографии')

#Ловим "нет"
async def load_photo_none(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = None
    await bot.send_message(message.from_user.id, 'Тикет успешно создан!', reply_markup=kb_client)
    #await sqlite_db.sql_add_command(state)
    await state.finish()





def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_callback_query_handler(process_callback_allow_contact, Text(equals='allow_contact'))
    dp.register_message_handler(process_email_step, state=GetEmail.waiting_for_email)
    dp.register_message_handler(create_new_ticket, Text(equals= 'Новый тикет', ignore_case=True), state=None)
    dp.register_message_handler(my_ticket, Text(equals='Мои тикеты', ignore_case=True), state=None)
    dp.register_message_handler(cancel_handler,Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(load_product, state=NewTicket.product)
    dp.register_message_handler(load_summary, state=NewTicket.summary)
    dp.register_message_handler(load_description, state=NewTicket.description)
    dp.register_message_handler(answer_yes, Text(equals='Да', ignore_case=True), state=NewTicket.photo)
    dp.register_message_handler(load_photo, content_types=['photo'], state=NewTicket.photo)
    dp.register_message_handler(load_photo_none, Text(equals='Нет', ignore_case=True), state=NewTicket.photo)
    dp.register_message_handler(incorrect_type, state=NewTicket.photo)

