from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import StatesGroup, State

from create_bot import dp, bot
#from data_base import sqlite_db
from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton, ParseMode, CallbackQuery

from keyboards import client_kb
from keyboards.other_kb import kb_other
from aiogram.dispatcher.filters import Text

class GetEmail(StatesGroup):
    waiting_for_email = State()
async def commands_start(message: types.Message):
    try:
        await message.answer("Привет! Я бот. Для работы мне нужен доступ к вашему контакту. Разрешить?",
                         reply_markup=kb_other)

    except:
        pass

@dp.callback_query_handler(Text(equals='allow_contact'))
async def process_callback_allow_contact(callback_query: CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await bot.send_message(callback_query.from_user.id, "Отлично! Теперь мне нужен ваш e-mail.", reply_markup=types.ReplyKeyboardRemove())
    await GetEmail.waiting_for_email.set()


@dp.message_handler(state=GetEmail.waiting_for_email)
async def process_email_step(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['email'] = message.text
        await state.finish()
    await message.answer(f"Спасибо, я сохранил ваш email: {data}.")


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(commands_start, commands=['start', 'help'])
    dp.register_message_handler(commands_start, commands=['новый тикет'])
    dp.register_message_handler(commands_start, commands=['мои тикеты'])
