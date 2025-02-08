from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def game_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/etymology_quiz")],
            [KeyboardButton(text="/etymology_anagram")],
        ],
        resize_keyboard=True
    )
    return keyboard