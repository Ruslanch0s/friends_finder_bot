from functools import wraps

from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message

from tgbot.db.repository import Repository
from tgbot.services.interview import save_interview
from tgbot.services.keyboards import interview_keyboard, find_keyboard
from tgbot.services.states import WriteInterview

router = Router()


def is_int(func):
    @wraps(func)
    async def wrapper(message: Message, *args, **kwargs):
        if message.text.isdigit():
            await func(message, *args, **kwargs)
        else:
            await message.answer("Введите число", reply_markup=interview_keyboard)

    return wrapper


@router.message(F.text == "Отменить")
async def reset(message: Message, state: FSMContext):
    await state.clear()
    await message.answer("Заполнение анкеты отменено", reply_markup=find_keyboard)


@router.message(F.text == "Рассказать о себе")
async def start_interview(message: Message, state: FSMContext):
    await message.answer("Размер твоего кешбека в NSP, в баллах:", reply_markup=interview_keyboard)
    await state.set_state(WriteInterview.writing_cashback_points)


@router.message(WriteInterview.writing_cashback_points)
@is_int
async def def1(message: Message, state: FSMContext):
    await state.update_data(writing_cashback_points=message.text)
    await message.answer(text="Количество активных клиентов в структуре, чел:")
    await state.set_state(WriteInterview.writing_clients_count)


@router.message(WriteInterview.writing_clients_count)
@is_int
async def def2(message: Message, state: FSMContext):
    await state.update_data(writing_clients_count=message.text)
    await message.answer("ГО твоей структуры в баллах:")
    await state.set_state(WriteInterview.writing_go_points)


@router.message(WriteInterview.writing_go_points)
@is_int
async def def3(message: Message, state: FSMContext):
    await state.update_data(writing_go_points=message.text)
    await message.answer("Статус участия:")
    await state.set_state(WriteInterview.writing_membership_status)


@router.message(WriteInterview.writing_membership_status)
async def def4(message: Message, state: FSMContext):
    await state.update_data(writing_membership_status=message.text)
    await message.answer("С какой деятельностью совмещаете:")
    await state.set_state(WriteInterview.writing_activity)


@router.message(WriteInterview.writing_activity)
async def def5(message: Message, state: FSMContext):
    await state.update_data(writing_activity=message.text)
    await message.answer("Ваш город:")
    await state.set_state(WriteInterview.writing_city)


@router.message(WriteInterview.writing_city)
async def def6(message: Message, state: FSMContext):
    await state.update_data(writing_city=message.text)
    await message.answer("Ваши сильные стороны:")
    await state.set_state(WriteInterview.writing_strengths)


@router.message(WriteInterview.writing_strengths)
async def def7(message: Message, state: FSMContext):
    await state.update_data(writing_strengths=message.text)
    await message.answer("Чего Вам сейчас не хватает:")
    await state.set_state(WriteInterview.writing_shortage)


@router.message(WriteInterview.writing_shortage)
async def finish(message: Message, state: FSMContext, db_repository: Repository):
    await state.update_data(writing_shortage=message.text)
    interview_data = await state.get_data()
    await save_interview(db_repository=db_repository, interview_data=interview_data, user_id=message.from_user.id)
    await state.clear()
    await message.answer("Информация о вас сохранена", reply_markup=find_keyboard)
