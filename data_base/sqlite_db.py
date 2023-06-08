import sqlite3 as sql
from create_bot import bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def sql_start():
    global db, cur
    db = sql.connect('support_bot-master.db')
    cur = db.cursor()
    if db:
        print('DB connected OK')
    db.execute('CREATE TABLE IF NOT EXISTS list('
               'summary TEXT,'
               'product TEXT PRIMARY KEY,'
               'description TEXT,'
               'photo TEXT,'
               'email TEXT,'
               'ID INT)'
               )
    db.commit()


async def sql_add_command(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO list VALUES (?, ?, ?, ?, ?, ?)', tuple(data.values()))
        db.commit()

async def sql_read(message):
    for ret in cur.execute('SELECT * FROM list').fetchall():
        await bot.send_message(message.from_user.id, ret[0])




