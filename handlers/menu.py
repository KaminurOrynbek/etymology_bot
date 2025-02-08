from aiogram import types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from keyboards.main_menu import main_menu
from keyboards.game_menu import game_menu

async def show_menu(message: types.Message):
    markup = main_menu()
    markup.add(KeyboardButton("/game_menu"))  # Добавляем кнопку для меню игр
    await message.answer("Выберите действие:", reply_markup=markup)

async def show_game_menu(message: types.Message):
    await message.answer("Выберите игру:", reply_markup=game_menu())