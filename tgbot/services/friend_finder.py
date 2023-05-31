import random

from tgbot.db.models import User, Pair
from tgbot.db.repository import Repository


async def finder(user_id: int, db_repository: Repository) -> User | None:
    free_friends_ids = await db_repository.pair_repository.get_free_friends_ids_for_user(user_id=user_id)
    if free_friends_ids:
        random_user_id = random.choice(free_friends_ids)[0]
        await db_repository.pair_repository.create_pair(Pair(user_id_1=user_id, user_id_2=random_user_id))
        await db_repository.user_repository.update_last_connect(user_id=user_id)
        return await db_repository.user_repository.get_user_by_id(random_user_id)
