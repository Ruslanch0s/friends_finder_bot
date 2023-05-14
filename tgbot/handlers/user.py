from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher import FSMContext


async def start(message: types.Message):
    await message.answer('Привет! Это библиотека анекдотов.')
    await message.answer('Выберите тему анекдотов')


def register_user(dp: Dispatcher):
    dp.register_message_handler(start, CommandStart(), state='*')
    # dp.register_callback_query_handler(view_name, choice_callback.filter(theme_id=['2']), state='*')
