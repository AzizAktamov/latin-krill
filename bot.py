from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from data import config
import asyncio
import logging
import sys
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
import time 
from criltolatin import latindan_crill,crilldan_latin, latindan_arab, latindan_kores, arabdan_latin, koresdan_latin
from keyboardbutton import til_button


ADMINS = config.ADMINS
TOKEN = config.BOT_TOKEN
CHANNELS = config.CHANNELS

dp = Dispatcher()


@dp.message(CommandStart())
async def start_command(message:Message):
    full_name = message.from_user.full_name
    telegram_id = message.from_user.id
    try:
        db.add_user(full_name=full_name,telegram_id=telegram_id)
        await message.answer(text="Assalomu alaykum, botimizga hushkelibsiz\nBu botda siz lotin yozuvidan kril yozuviga o'tkazadi✅..", reply_markup=til_button)
    except:
        await message.answer(text="Assalomu alaykum, botimizga hushkelibsiz\nBu botda siz lotin yozuvidan kril yozuviga o'tkazadi✅..", reply_markup=til_button)


@dp.message(IsCheckSubChannels())
async def kanalga_obuna(message:Message):
    text = ""
    inline_channel = InlineKeyboardBuilder()
    for index,channel in enumerate(CHANNELS):
        ChatInviteLink = await bot.create_chat_invite_link(channel)
        inline_channel.add(InlineKeyboardButton(text=f"{index+1}-kanal❌",url=ChatInviteLink.invite_link))
    inline_channel.adjust(1,repeat=True)
    button = inline_channel.as_markup()
    await message.answer(f"{text} Kanallarga azo bo'ling〽️",reply_markup=button)



@dp.message(Command("help"))
async def help_commands(message:Message):
    await message.answer("Lotin -- Krill\nKrill -- Lotin\nManashu tartibda\n\nIltimos kanalarimizga obuna bo'ling\n☎️Admin:@aminjon_2521\n☎️Reklama bo'yicha:@solo_hub")





#Admin panel uchun
@dp.message(Command("admin"),IsBotAdminFilter(ADMINS))
async def is_admin(message:Message):
    await message.answer(text="Admin menu",reply_markup=admin_keyboard.admin_button)


@dp.message(F.text=="Foydalanuvchilar soni",IsBotAdminFilter(ADMINS))
async def users_count(message:Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

@dp.message(F.text=="Reklama yuborish",IsBotAdminFilter(ADMINS))
async def advert_dp(message:Message,state:FSMContext):
    await state.set_state(Adverts.adverts)
    await message.answer(text="Reklama yuborishingiz mumkin !")

@dp.message(Adverts.adverts)
async def send_advert(message:Message,state:FSMContext):
    
    message_id = message.message_id
    from_chat_id = message.from_user.id
    users = await db.all_users_id()
    count = 0
    for user in users:
        try:
            await bot.copy_message(chat_id=user[0],from_chat_id=from_chat_id,message_id=message_id)
            count += 1
        except:
            pass
        time.sleep(0.5)
    
    await message.answer(f"Reklama {count}ta foydalanuvchiga yuborildi")
    await state.clear()


@dp.message(Command("count"))
async def all_users_count(message:Message):
    counts = db.count_users()
    text = f"Botimizda {counts[0]} ta foydalanuvchi bor"
    await message.answer(text=text)

user_state = {}

# 'latin-crill' tugmasi bosilganda matn so'rash funksiyasi
@dp.message(F.text == 'latin-crill')
async def ask_for_text(message: Message):
    user_state[message.from_user.id] = 'latin-crill'  # Holatni saqlaymiz
    await message.answer("Matnni yuboring, uni Kirill alifbosiga o'zgartiraman.")

# 'latin-arab' tugmasi bosilganda matn so'rash funksiyasi
@dp.message(F.text == 'latin-arab')
async def prompt_for_text(message: Message):
    user_state[message.from_user.id] = 'latin-arab'  # Holatni saqlaymiz
    await message.answer("Matnni yuboring, uni Arab alifbosiga o'zgartiraman.")

# 'latin-kores' tugmasi bosilganda matn so'rash funksiyasi
@dp.message(F.text == 'latin-kores')
async def prompt_for_korean_text(message: Message):
    user_state[message.from_user.id] = 'latin-kores'  # Holatni saqlaymiz
    await message.answer("Matnni yuboring, uni Koreys alifbosiga o'zgartiraman.")

# 'crill-latin' tugmasi bosilganda matn so'rash funksiyasi
@dp.message(F.text == 'crill-latin')
async def prompt_for_crill_to_latin_text(message: Message):
    user_state[message.from_user.id] = 'crill-latin'  # Holatni saqlaymiz
    await message.answer("Matnni yuboring, uni Lotin alifbosiga o'zgartiraman.")

# 'arab-latin' tugmasi bosilganda matn so'rash funksiyasi
@dp.message(F.text == 'arab-latin')
async def prompt_for_arab_to_latin_text(message: Message):
    user_state[message.from_user.id] = 'arab-latin'  # Holatni saqlaymiz
    await message.answer("Matnni yuboring, uni Lotin alifbosiga o'zgartiraman.")


# 'kores-latin' tugmasi bosilganda matn so'rash funksiyasi
@dp.message(F.text == 'kores-latin')
async def prompt_for_korean_to_latin_text(message: Message):
    user_state[message.from_user.id] = 'kores-latin'  # Holatni saqlaymiz
    await message.answer("Matnni yuboring, uni Lotin alifbosiga o'zgartiraman.")

# Tarjima va natijani jo'natish funksiyasi
@dp.message(F.text)
async def handle_translation(message: Message):
    user_id = message.from_user.id
    # Foydalanuvchi qaysi tarjima jarayonida ekanini aniqlash
    if user_id in user_state:
        if user_state[user_id] == 'latin-crill':
            # Lotindan Kirillga o'zgartirish
            result = latindan_crill(message.text)
            await message.answer(result)
        elif user_state[user_id] == 'latin-arab':
            # Lotindan Arabga o'zgartirish
            result = latindan_arab(message.text)
            await message.answer(result)
        elif user_state[user_id] == 'latin-kores':
            # Lotindan Koreysga o'zgartirish
            result = latindan_kores(message.text)
            await message.answer(result)
        elif user_state[user_id] == 'crill-latin':
            # Kirilldan Lotinga o'zgartirish
            result = crilldan_latin(message.text)
            await message.answer(result)
        elif user_state[user_id] == 'arab-latin':
            # Arabdan Lotinga o'zgartirish
            result = arabdan_latin(message.text)
            await message.answer(result)
        elif user_state[user_id] == 'kores-latin':
            # Koreysdan Lotinga o'zgartirish
            result = koresdan_latin(message.text)
            await message.answer(result)
        
        # Tarjima tugagach, holatni o'chiramiz
        del user_state[user_id]
    else:
        await message.answer("Iltimos, avval tarjima jarayonini tanlang.")





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