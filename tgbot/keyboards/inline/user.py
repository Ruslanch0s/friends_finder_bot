from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot.keyboards.inline.callback_dates import choice_callback

back_to_themes_button = InlineKeyboardButton(text="К темам", callback_data='joke')
next_joke_button = InlineKeyboardButton(text="Следующий >", callback_data='next_joke')

choice_theme_keyboard = InlineKeyboardMarkup(row_width=2,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(text="Тема1",
                                                                          callback_data=choice_callback.new(
                                                                              theme_id='1')),  # 'pay:apple:3'
                                                     InlineKeyboardButton(text="Тема2",
                                                                          callback_data=choice_callback.new(
                                                                              theme_id='2')),
                                                 ]
                                             ])

joke_keyboard = InlineKeyboardMarkup(row_width=2,
                                     inline_keyboard=[
                                         [
                                             back_to_themes_button,
                                             next_joke_button,
                                         ]
                                     ])

# async def theme1(callback_query: types.CallbackQuery):
#     await callback_query.message.delete()
#     await callback_query.message.answer('Анекдот темы 1', reply_markup=joke_keyboard)
