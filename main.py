import logging

import uvicorn
from aiogram import Bot, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.fsm_storage.redis import RedisStorage
from aiogram.dispatcher import Dispatcher

from api import app
from config import load_config
from tgbot.bot import on_startup_bot

logging.basicConfig(level=logging.INFO)

config = load_config()
# Throttling manager does not work without storage
if config.tg_bot.use_redis:
    storage = RedisStorage()
else:
    storage = MemoryStorage()
bot = Bot(token=config.tg_bot.token, parse_mode=types.ParseMode.HTML)  # + html стили для текста
dp = Dispatcher(bot=bot, storage=storage)


@app.on_event("startup")
async def on_startup_fastapi():
    await on_startup_bot(dp, config)


@app.post(config.api.webhook_path)
async def bot_webhook(update: dict):
    telegram_update = types.Update(**update)
    Dispatcher.set_current(dp)
    Bot.set_current(bot)
    await dp.process_update(telegram_update)


@app.on_event("shutdown")
async def on_shutdown_fastapi():
    await dp.storage.close()
    await dp.storage.wait_closed()
    session = await bot.get_session()
    await session.close()
    # Remove webhook (not acceptable in some cases)
    # await bot.delete_webhook()


def main():
    uvicorn.run(app, host=config.api.webapp_host, port=config.api.webapp_port)


if __name__ == '__main__':
    main()
