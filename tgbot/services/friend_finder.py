import random

from aiogram import Bot

from tgbot.db.models import User, Pair
from tgbot.db.repository import Repository
from tgbot.services.keyboards import find_keyboard


async def get_random_free_friend_for_user(user_id: int, db_repository: Repository) -> User | None:
    free_friends_ids = await db_repository.pair_repository.get_free_friends_ids_for_user(user_id=user_id)
    if free_friends_ids:
        random_user_id = random.choice(free_friends_ids)[0]
        await db_repository.pair_repository.create_pair(Pair(user_id_1=user_id, user_id_2=random_user_id))
        await db_repository.user_repository.update_last_connect(user_id=user_id)
        return await db_repository.user_repository.get_user_by_id(random_user_id)


async def send_new_friend(user_id: int, db_repository: Repository, bot: Bot):
    new_friend = await get_random_free_friend_for_user(user_id=user_id, db_repository=db_repository)
    if new_friend:
        user = await bot.get_chat(chat_id=new_friend.user_id)
        await bot.send_message(chat_id=user_id,
                               text=f"Мы нашли тебе нового друга. \n{user.full_name} https://t.me/{user.username}",
                               reply_markup=find_keyboard)
