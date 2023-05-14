import logging

import tzlocal
from aiogram import Dispatcher
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import Config
from db.database import create_db_session
from tgbot.handlers.echo import register_echo
from tgbot.handlers.user import register_user
from tgbot.middlewares.antiflood import ThrottlingMiddleware
from tgbot.middlewares.db import DbMiddleware
from tgbot.middlewares.scheduler import SchedulerMiddleware
from tgbot.services.notify_admins import on_startup_notify

logger = logging.getLogger(__name__)


def register_all_middlewares(dp, config, scheduler):
    dp.setup_middleware(DbMiddleware())
    dp.setup_middleware(ThrottlingMiddleware(config=config))
    dp.setup_middleware(SchedulerMiddleware(scheduler=scheduler))


def register_all_filters(dp):
    # dp.filters_factory.bind(AdminFilter)
    pass


def register_all_handlers(dp):
    # register_deeplink(dp)
    register_user(dp)
    register_echo(dp)


# Создаем функцию, в которой будет происходить запуск наших тасков.
def set_scheduled_jobs(scheduler, bot, config, *args, **kwargs):
    # Добавляем задачи на выполнение (async/sync)
    # scheduler.add_job(send_message_to_admin, "interval", seconds=5, args=(bot, config))
    # scheduler.add_job(some_other_regular_task, "interval", seconds=100)
    # можно брать scheduler сразу из миделварей в хендлерах!!!!!!!!!!!
    pass


async def registrate_modules(dp: Dispatcher, config: Config):
    dp.bot['config'] = config
    dp.bot['db'] = await create_db_session(config)

    scheduler = AsyncIOScheduler(timezone=str(tzlocal.get_localzone()))
    set_scheduled_jobs(scheduler, dp.bot, config)

    register_all_middlewares(dp, config, scheduler)
    register_all_handlers(dp)

    scheduler.start()

    await on_startup_notify(dp, config)


async def on_startup_bot(dp: Dispatcher, config: Config):
    await registrate_modules(dp, config)
    webhook_info = await dp.bot.get_webhook_info()

    if config.tg_bot.skip_updates:
        await dp.skip_updates()

    webhook_url = f'{config.api.webhook_host}{config.api.webhook_path}'
    if webhook_info.url != webhook_url:
        await dp.bot.set_webhook(
            url=webhook_url,
        )
