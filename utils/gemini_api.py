import requests
import os
import logging
from dotenv import load_dotenv

# Получаем токены
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Проверка API-ключа
if not GEMINI_API_KEY:
    raise ValueError("Ошибка: API-ключ не найден. Проверь .env файл!")

# URL API Gemini
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

def fetch_etymology(word):
    """Функция для получения этимологии слова"""
    payload = {
        "contents": [
            {
                "role": "user",
                "parts": [{"text": f"Расскажи этимологию слова '{word}' на русском языке. Избегай протоформ."}]
            }
        ]
    }

    try:
        response = requests.post(GEMINI_API_URL, json=payload)
        logging.info(f"API Response: {response.status_code} - {response.text}")

        if response.status_code == 200:
            data = response.json()
            candidates = data.get("candidates", [])

            if candidates:
                result = candidates[0]["content"]["parts"][0]["text"].strip()
                
                # Фильтруем ненужные протоформы
                result = remove_protoforms(result)

                return result if result else "Не удалось найти этимологию этого слова."

        elif response.status_code == 401:
            return "Ошибка: Неверный API ключ. Проверьте его в .env."

        elif response.status_code == 404:
            return "Ошибка: API не найден. Проверьте правильность запроса."

        else:
            return f"Ошибка {response.status_code}: {response.text}"

    except requests.exceptions.RequestException as e:
        logging.error(f"Request Exception: {e}")
        return "Ошибка при подключении к API."

def remove_protoforms(text):
    """Фильтрует ненужные протоформы из ответа"""
    lines = text.split("\n")
    clean_lines = [line for line in lines if not any(proto in line for proto in ["Proto-", "*", "meaning"])]
    return "\n".join(clean_lines).strip()
