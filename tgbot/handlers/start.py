from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from tgbot.services.keyboards import find_keyboard

router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>\n\n"
                         f"Пожалуйста заполни анкету 'О себе' прежде чем искать новые знакомства",
                         reply_markup=find_keyboard)
