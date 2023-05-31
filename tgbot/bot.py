import asyncio
import logging

from aiogram import Bot, Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from tgbot.db.manager import DatabaseManager
from tgbot.db.repository import Repository
from tgbot.handlers import start, friends
from tgbot.middlewares.user_log import UserLogMiddleware
from tgbot.services.scheduler_tasks import job

logging.basicConfig(level=logging.INFO)


async def main():
    db_manager = DatabaseManager(db_url="postgresql+psycopg://postgres:qwerty@127.0.0.1:6543/postgres", echo=True)
    db_repository = Repository(db_manager=db_manager)
    await db_repository.create_all_models()

    bot = Bot(token="5991450214:AAFAjn0ZHqHV88lpjr4r9uTm0aClk1HWcE0", parse_mode="HTML")
    dp = Dispatcher(db_repository=db_repository)
    dp.message.middleware(UserLogMiddleware())
    dp.include_routers(
        start.router,
        friends.router
    )

    scheduler = AsyncIOScheduler()
    scheduler.add_job(job, "interval", seconds=10, args=[db_repository, bot])
    scheduler.start()

    # Запускаем бота и пропускаем все накопленные входящие
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
