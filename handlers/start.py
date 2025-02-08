from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def cmd_start(message: types.Message):
    # Создаем клавиатуру с командами
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/etymology")],
            [KeyboardButton(text="/etymology_quiz")],
            [KeyboardButton(text="/etymology_anagram")],
            [KeyboardButton(text="/game_menu")]
        ],
        resize_keyboard=True
    )

    # Отправляем приветственное сообщение с командами
    await message.answer(
        "Привет! Я бот, который поможет тебе изучать этимологию слов! Выбери действие:\n"
        "🔹 /etymology - Узнать этимологию слова\n"
        "🔹 /etymology_quiz - Викторина по этимологии\n"
        "🔹 /etymology_anagram - Этимологические анаграммы\n"
        "🔹 /game_menu - Меню игр",
        reply_markup=keyboard
    )