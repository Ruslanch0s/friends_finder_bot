from aiogram.dispatcher.filters.state import StatesGroup, State


class UserStates(StatesGroup):
    Q1 = State()
    Q2 = State()

# await state.reset_state()
# await UserStates.Q1.set()
