from tgbot.db.repository import Repository


async def save_interview(user_id: int, db_repository: Repository, interview_data: dict):
    await db_repository.user_repository.update_interview(
        user_id=user_id,
        cashback_points=interview_data.get("writing_cashback_points"),
        clients_count=interview_data.get("writing_clients_count"),
        go_points=interview_data.get("writing_go_points"),
        membership_status=interview_data.get("writing_membership_status"),
        activity=interview_data.get("writing_activity"),
        city=interview_data.get("writing_city"),
        strengths=interview_data.get("writing_strengths"),
        shortage=interview_data.get("writing_shortage")
    )
