from aiogram.filters import BaseFilter
from aiogram.types import Message

from tgbot.db.repository import Repository


class ExistInterviewFilter(BaseFilter):  # [1]
    async def __call__(self, message: Message, db_repository: Repository) -> bool:  # [3]
        user = await db_repository.user_repository.get_user_by_id(user_id=message.from_user.id)
        if user.interview:
            print("True")
            return True
        else:
            await message.answer(f"Пожалуйста заполни анкету 'О себе' прежде чем искать новые знакомства")
            return False
