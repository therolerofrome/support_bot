from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State
#from data_base import sqlite_db
import requests
import json
from .validators import is_valid_email

from create_bot import dp, bot

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ParseMode, CallbackQuery
from aiogram.dispatcher.filters import Text

from keyboards.client_kb import kb_client, kb_client_ticket, kb_client_yn, kb_client_environment, kb_client_system, \
    kb_client_cancel
from keyboards.other_kb import kb_other



class NewTicket(StatesGroup):
    type_id = State() # Тип тикета
    environment_id = State() # Вид среды
    system_id = State() # Вид система
    theme = State() # Тема тикета
    description = State() # Описание вопроса
    ticket_priority = State() # Приоритет
    #photo = State() # Скриншоты если надо



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


async def process_callback_allow_contact(message: types.Message):
    phone_number = message.contact.phone_number
    await bot.send_message(message.from_user.id, "Отлично! Теперь мне нужен ваш e-mail.", reply_markup=types.ReplyKeyboardRemove())
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
#Выход из состояния
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return
    await state.finish()
    await bot.send_message(message.from_user.id, 'Хорошо', reply_markup=kb_client)


#Начало диалога создания тикета
async def create_new_ticket(message: types.Message):
    await bot.send_message(message.from_user.id, 'У вас проблема или вопрос по функционалу?', reply_markup=kb_client_ticket)
    await NewTicket.type_id.set()


#Ловим  ответ и заполняем тип тикета
async def load_type_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == 'Проблема':
            data['type_id'] = 'dc7ab77b-f599-40ee-ad6e-92df05f3e27e'
        elif message.text == 'Вопрос':
            data['type_id'] = 'ff8e4a2c-4096-499c-8e44-9e31f3d49f2e'
    await NewTicket.next()
    await bot.send_message(message.from_user.id,'Выберите среду', reply_markup=kb_client_environment)

# Ловим  ответ и заполняем тип среды
async def load_environment_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == 'PROD':
            data['environment_id'] = '6d173c80-1c32-441f-b18b-fec0bbd29d46'
        elif message.text == 'DEV':
            data['environment_id'] = 'c4068def-6469-4078-9609-74ea13599d44'
        elif message.text == 'TEST':
            data['environment_id'] = '514a4b1e-edd7-4e73-b0aa-098055d7d8a6'
    await NewTicket.next()
    await bot.send_message(message.from_user.id,'Выберите систему', reply_markup=kb_client_system)

#Ловим  ответ и заполняем систему
async def load_system_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['system_id'] = '1af428dd-7cdc-4e9d-96fe-1bbc7adcafe9'
    await NewTicket.next()
    await bot.send_message(message.from_user.id,'Напишите тему', reply_markup=kb_client_cancel)

#Ловим  ответ и заполняем тему тикета
async def load_theme(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['theme'] = message.text
    await NewTicket.next()
    await bot.send_message(message.from_user.id,'Опишите свой вопрос или проблему', reply_markup=kb_client_cancel)


#Ловим  ответ и заполняем описание тикета
async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
    await NewTicket.next()
    return await message.reply('Выберите приоритет', reply_markup=)

async def load_ticket_priority(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.text == 'Без приоритета':
            data['ticket_priority'] = '943e9262-40b7-4308-b331-488f10d9e7b0'
        elif message.text == 'Низкий':
            data['ticket_priority'] = 'e964f5e1-1257-480a-8cf2-516008162f4a'
        elif message.text == 'Средний':
            data['ticket_priority'] = '1bd92fc0-30bb-48a6-a95c-a34221ac92be'
        elif message.text == 'Высокий':
            data['ticket_priority'] = 'ed806be0-cda1-44af-bd48-0577dfd1ca4f'
        elif message.text == 'Критический':
            data['ticket_priority'] = '75ddb269-5aae-40c5-83f8-eff3eeff935d'
    # await NewTicket.next()
    bot.send_message(message.from_user.id, 'Тикет успешно создан!', reply_markup=kb_client)
    # await bot.send_message(message.from_user.id,'Вам нужно загрузить фото?', reply_markup=kb_client_yn)

    """Пост реквест"""

    url3 = 'http://external-integration.dev.t1support-portal.dev.ts/api/v1/ticket'

    data_request = {

        "typeId": data['type_id'],
        "theme": data['theme'],
        "description": data['description'],
        "environmentId": data['environment_id'],
        "systemId": data['system_id'],
        "ticketPriority": data['ticket_priority'],

    }

    session = requests.Session()
    response3 = session.post(url3, data=json.dumps(data_request), headers={
        'Content-type': 'application/json',
        'Accept': 'application/json',
    })

    await state.finish()

'''Сегмент с загрузкой фото'''

#Ловим "да"
# async def answer_yes(message: types.Message):
#     await bot.send_message(message.from_user.id, 'Загрузите от 1 до 10 картинки')

#Ловим "Фото"
# async def load_photo(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['photo'] = [photo.file_id for photo in message.photo] # Сохраняет ID фотографии.
#         ### Код для скачивания файлов###
#         # file = await bot.get_file(message.photo[-1].file_id)
#         # await message.photo[-1].download(file_.file_path.split('photos/')[1])
#     await bot.send_message(message.from_user.id, 'Тикет успешно создан!', reply_markup=kb_client)
#     await state.finish()

#Ловим не правильный тип данных
# async def incorrect_type(message: types.Message, state: FSMContext):
#     await bot.send_message(message.from_user.id, 'Нужно загрузить фотографии')

#Ловим "нет"
# async def load_photo_none(message: types.Message, state: FSMContext):
#     async with state.proxy() as data:
#         data['photo'] = None
#     await bot.send_message(message.from_user.id, 'Тикет успешно создан!', reply_markup=kb_client)
#     await state.finish()





def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(cancel_handler, Text(equals='отмена', ignore_case=True), state='*')
    dp.register_message_handler(process_callback_allow_contact, content_types=['contact'])
    dp.register_message_handler(process_email_step, state=GetEmail.waiting_for_email)
    dp.register_message_handler(create_new_ticket, Text(equals= 'Новый тикет', ignore_case=True))
    dp.register_message_handler(my_ticket, Text(equals='Мои тикеты', ignore_case=True))
    dp.register_message_handler(load_type_id, state=NewTicket.type_id)
    dp.register_message_handler(load_environment_id, state=NewTicket.environment_id)
    dp.register_message_handler(load_environment_id, state=NewTicket.system_id)
    dp.register_message_handler(load_theme, state=NewTicket.theme)
    dp.register_message_handler(load_description, state=NewTicket.description)
    dp.register_message_handler(load_ticket_priority, state=NewTicket.ticket_priority)



    '''Сегмент с фото'''
    # dp.register_message_handler(answer_yes, Text(equals='Да', ignore_case=True), state=NewTicket.photo)
    # dp.register_message_handler(load_photo, content_types=['photo'], state=NewTicket.photo)
    # dp.register_message_handler(load_photo_none, Text(equals='Нет', ignore_case=True), state=NewTicket.photo)
    # dp.register_message_handler(incorrect_type, state=NewTicket.photo)



