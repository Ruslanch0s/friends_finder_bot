from aiogram import Bot


async def message_manager(**kwargs):
    bot: Bot = kwargs.get('bot')
    session_maker = kwargs.get('db')

# по расписанию
# scheduler.add_job(message_manager, 'interval', seconds=100, next_run_time=datetime.now(),
#                   kwargs={'db': bot['db'], 'bot': bot})
