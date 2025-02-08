from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/etymology")],  # Этимология слов
            [KeyboardButton(text="/etymology_quiz")],  # Викторина по этимологии
            [KeyboardButton(text="/related_words")],  # Найти родственное слово
            [KeyboardButton(text="/etymology_anagram")],  # Этимологические анаграммы
            [KeyboardButton(text="/true_false")],  # Правда или ложь
            [KeyboardButton(text="/menu")],  # Главное меню
            [KeyboardButton(text="/game_menu")]  # Меню игр
        ],
        resize_keyboard=True
    )
    return keyboard