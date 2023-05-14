from aiogram import Dispatcher

import logging
from config import Config


async def on_startup_notify(dp: Dispatcher, config: Config):
    for admin in config.tg_bot.admin_ids:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
