from aiogram.fsm.state import StatesGroup, State


class WriteInterview(StatesGroup):
    writing_cashback_points = State()
    writing_clients_count = State()
    writing_go_points = State()
    writing_membership_status = State()
    writing_activity = State()
    writing_city = State()
    writing_strengths = State()
    writing_shortage = State()
