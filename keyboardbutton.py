from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


til_button = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="latin-crill"),
            KeyboardButton(text="crill-latin"),
        ],
        [
            KeyboardButton(text="latin-arab"),
            KeyboardButton(text="arab-latin"),
        ],
        [
            KeyboardButton(text="latin-kores"),
            KeyboardButton(text="kores-latin"),
        ],
        [
            KeyboardButton(text="☎️Admin"),
        ]
        
    ],
   resize_keyboard=True,
)