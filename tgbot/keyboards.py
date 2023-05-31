from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

kb = [
    [KeyboardButton(text="Найти подружку")],
]
keyboard = ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True)
