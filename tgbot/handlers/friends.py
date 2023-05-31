import random

from aiogram import Router, F, Bot
from aiogram.types import Message

from tgbot.db.repository import Repository
from tgbot.keyboards import keyboard
from tgbot.services.friend_finder import finder
router = Router()


@router.message(F.text == 'Найти подружку')
async def find_friend(message: Message, db_repository: Repository, bot: Bot) -> None:
    friend = await finder(user_id=message.from_user.id, db_repository=db_repository)
    if friend:
        user = await bot.get_chat(chat_id=friend.user_id)
        await message.answer(f"{user.full_name} https://t.me/{user.username}", reply_markup=keyboard)
    else:
        await message.answer("Упппс, вы со всеми знакомы. "
                             "Как только появятся новые пользователи - мы вам сообщим в уведомлении",
                             reply_markup=keyboard)
