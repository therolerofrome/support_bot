from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from aiogram.contrib.fsm_storage.memory import MemoryStorage

storage = MemoryStorage()

bot = Bot(token='6205286454:AAGq97o63bBRr7yd93PoRnSZ0x5HrFQdBH8')
dp = Dispatcher(bot, storage=storage)