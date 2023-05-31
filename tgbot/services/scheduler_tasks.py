# from aiogram import Bot
from aiogram import Bot

from tgbot.db.repository import Repository
import datetime
from tgbot.services.friend_finder import finder
from tgbot.keyboards import keyboard

#
# async def message_manager(**kwargs):
#     bot: Bot = kwargs.get('bot')
#     session_maker = kwargs.get('db')

# по расписанию
# scheduler.add_job(message_manager, 'interval', seconds=100, next_run_time=datetime.now(),
#                   kwargs={'db': bot['db'], 'bot': bot})


async def job(db_repository: Repository, bot: Bot):
    time_diff = datetime.timedelta(seconds=10)
    users_datas_for_sending = await db_repository.user_repository.get_free_users(time_diff=time_diff)
    for user_data in users_datas_for_sending:
        friend = await finder(user_id=user_data[0], db_repository=db_repository)
        if friend:
            user = await bot.get_chat(chat_id=friend.user_id)
            await bot.send_message(chat_id=user_data[0], text=f"Мы нашли тебе нового друга. \n{user.full_name} https://t.me/{user.username}",
                                   reply_markup=keyboard)
