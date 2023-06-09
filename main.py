from aiogram.utils import executor
from create_bot import dp
#from data_base import sqlite_db
import logging

logging.basicConfig(level=logging.INFO)


async def on_startup(_): #Запускаем при помощи полинга очень полезно вывести служебную информацию
    #sqlite_db.sql_start()
    print('Бот вышел в онлайн')


from Handlers import client

client.register_handlers_client(dp)
#admin.register_handlers_client(dp)



executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
