import logging

from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tgbot.db.manager import DatabaseManager
from tgbot.db.repository import Repository
from tgbot.handlers import start, friends, interview
from tgbot.middlewares.user_log import UserLogMiddleware
from tgbot.services.scheduler_tasks import job

logging.basicConfig(level=logging.INFO)


async def main():
    db_manager = DatabaseManager(db_url="postgresql+psycopg://postgres:qwerty@friend_finder_postgres/postgres",
                                 echo=True)
    db_repository = Repository(db_manager=db_manager)
    await db_repository.create_all_models()

    bot = Bot(token="5991450214:AAFAjn0ZHqHV88lpjr4r9uTm0aClk1HWcE0", parse_mode="HTML")
    dp = Dispatcher(db_repository=db_repository)
    dp.message.outer_middleware(UserLogMiddleware())
    dp.include_routers(
        start.router,
        interview.router,
        friends.router
    )

    scheduler = AsyncIOScheduler()
    last_search_friend_sec = 14400
    scheduler.add_job(job, "interval", seconds=900, args=[db_repository, bot, last_search_friend_sec])
    scheduler.start()

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
