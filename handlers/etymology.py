from aiogram import types
from utils.gemini_api import fetch_etymology

async def get_etymology(message: types.Message):
    word = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    if not word:
        await message.reply("Пожалуйста, напишите слово после команды /etymology.")
        return
    
    response = fetch_etymology(word)
    await message.reply(response)