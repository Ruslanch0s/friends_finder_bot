# from aiogram import Bot
import datetime

from aiogram import Bot

from tgbot.db.repository import Repository
from tgbot.services.friend_finder import send_new_friend


async def job(db_repository: Repository, bot: Bot):
    time_diff = datetime.timedelta(seconds=10)
    users_datas_for_sending = await db_repository.user_repository.get_free_users(time_diff=time_diff)
    for user_data in users_datas_for_sending:
        await send_new_friend(user_id=user_data[0], db_repository=db_repository, bot=bot)
