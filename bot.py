import logging
import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from config import settings
from handlers import start, etymology, games, menu

logging.basicConfig(level=logging.INFO)

bot = Bot(token=settings.TOKEN)
dp = Dispatcher()

# Регистрация обработчиков команд
dp.message.register(start.cmd_start, Command("start"))
dp.message.register(etymology.get_etymology, Command("etymology"))
dp.message.register(games.play_etymology_quiz, Command("etymology_quiz"))
dp.message.register(games.play_etymology_anagram, Command("etymology_anagram"))
dp.message.register(menu.show_menu, Command("menu"))
dp.message.register(menu.show_game_menu, Command("game_menu"))
dp.message.register(menu.show_game_menu, Command("game"))

# Регистрация обработчиков ответов
dp.message.register(games.check_etymology_answer, F.text.in_(sum(games.questions.values(), [])))
dp.message.register(games.check_anagram_answer, F.text)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())