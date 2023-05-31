# новые импорты!
from datetime import datetime
from typing import Callable, Dict, Any, Awaitable

from aiogram import BaseMiddleware
from aiogram.types import TelegramObject

from tgbot.db.models import User


class UserLogMiddleware(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any],

    ) -> Any:
        message = data.get("event_update").message
        db_repository = data.get("db_repository")
        user_from_db = await db_repository.user_repository.get_user_by_id(user_id=message.from_user.id)
        if not user_from_db:
            user = User(user_id=message.from_user.id, full_name=message.from_user.full_name,
                        last_connect=datetime.now())
            await db_repository.user_repository.create_user(user)

        await handler(event, data)
