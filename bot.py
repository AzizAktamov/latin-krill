from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F,types
from aiogram.types import Message
from data import config
import asyncio
import logging
import sys
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton , CallbackQuery
from menucommands.set_bot_commands  import set_default_commands
from baza.sqlite import Database
from filters.admin import IsBotAdminFilter
from filters.check_sub_channel import IsCheckSubChannels
from keyboard_buttons import admin_keyboard
from aiogram.fsm.context import FSMContext
from middlewares.throttling import ThrottlingMiddleware #new
from states.reklama import Adverts
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram.types import ContentType
import time 
from criltolatin import latindan_crill,crilldan_latin, latindan_arab, latindan_kores, arabdan_latin, koresdan_latin
from keyboardbutton import til_button
from aiogram.fsm.state import StatesGroup, State


ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS

dp = Dispatcher()









@dp.startup()
async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishga tushdi")
        except Exception as err:
            logging.exception(err)

#bot ishga tushganini xabarini yuborish
@dp.shutdown()
async def off_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
            await bot.send_message(chat_id=int(admin),text="Bot ishdan to'xtadi!")
        except Exception as err:
            logging.exception(err)




async def main() -> None:
    global bot,db
    bot = Bot(TOKEN)
    db = Database(path_to_db="main.db")
    db.create_table_users()
    await set_default_commands(bot)
    dp.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))
    await dp.start_polling(bot)
    




if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)

    asyncio.run(main())