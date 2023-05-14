from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import CommandStart
from aiogram.dispatcher import FSMContext

from apscheduler.schedulers.asyncio import AsyncIOScheduler


async def some_task(message):
    await message.answer("dasf")
    print('aaaa')


async def some_useful_message_handler(message: types.Message, scheduler: AsyncIOScheduler):
    await message.answer('yes')
    scheduler.add_job(some_task, 'interval', seconds=3, args=([message]))


def register_user(dp: Dispatcher):
    dp.register_message_handler(some_useful_message_handler, content_types=types.ContentTypes.TEXT)
