from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from tgbot.services.keyboards import find_keyboard

router = Router()


@router.message(Command(commands=["start"]))
async def command_start_handler(message: Message) -> None:
    """
    This handler receive messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, <b>{message.from_user.full_name}!</b>\n\n"
                         f"Пожалуйста заполни анкету 'О себе' прежде чем искать новые знакомства",
                         reply_markup=find_keyboard)
