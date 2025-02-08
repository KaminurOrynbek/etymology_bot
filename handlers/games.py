import json
from aiogram import types
import random
import re

# Load questions and correct answers from JSON file
with open('data/questions.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
    questions = data['questions']
    correct_answers = data['correct_answers']
    anagrams = data['anagrams']

# Активные вопросы для пользователей
active_questions = {}
active_anagrams = {}

# Запуск викторины по этимологии
async def play_etymology_quiz(message: types.Message):
    word, options = random.choice(list(questions.items()))
    active_questions[message.chat.id] = word  # Запоминаем вопрос для пользователя
    
    await message.answer(
        f"Из какой группы языков произошло слово '{word}'?\n"
        "🔹 Напиши один из вариантов: " + ", ".join(options)
    )

# Проверка ответа на этимологическую викторину
async def check_etymology_answer(message: types.Message):
    user_answer = message.text.strip().lower()
    chat_id = message.chat.id

    if chat_id not in active_questions:
        return  # Если вопроса нет, не отвечаем

    word = active_questions[chat_id]  # Получаем текущее слово
    correct_answer = correct_answers[word].lower()
    
    if user_answer == correct_answer:
        await message.answer("✅ Верно! Ты молодец!")
    else:
        await message.answer(f"❌ Неправильно. Правильный ответ: {correct_answer.capitalize()}.")


    del active_questions[chat_id]  # Удаляем активный вопрос
    


# 3️⃣ Этимологические анаграммы
async def play_etymology_anagram(message: types.Message):
    anagram, word = random.choice(list(anagrams.items()))
    active_anagrams[message.chat.id] = word  # Запоминаем анаграмму для пользователя
    
    await message.answer(
        f"Разгадай анаграмму: '{anagram.upper()}'\n"
        "🔹 Отправьте свой ответ в виде ответа на это сообщение!",
        reply_markup=types.ForceReply(selective=True)
    )

# Проверка ответа на анаграмму
async def check_anagram_answer(message: types.Message):
    user_answer = message.text.strip().lower()
    chat_id = message.chat.id

    if chat_id not in active_anagrams:
        return  # Если анаграммы нет, не отвечаем

    word = active_anagrams[chat_id]  # Получаем текущее слово
    correct_answer = correct_answers[word].lower()

    if user_answer == word:
        await message.answer(f"✅ Верно! Это слово {correct_answer} происхождения 🎭")
    else:
        await message.answer(f"❌ Неправильно. Попробуй снова.")

    del active_anagrams[chat_id]  # Удаляем активную анаграмму