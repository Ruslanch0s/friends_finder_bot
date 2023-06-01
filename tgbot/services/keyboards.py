from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

find_buttons = [
    [KeyboardButton(text="Найти подружку")],
    [KeyboardButton(text="Рассказать о себе")]
]
interview_buttons = [
    [KeyboardButton(text="Отменить")]
]

interview_keyboard = ReplyKeyboardMarkup(keyboard=interview_buttons, resize_keyboard=True)
find_keyboard = ReplyKeyboardMarkup(keyboard=find_buttons, resize_keyboard=True)
