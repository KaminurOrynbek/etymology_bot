# Etymology Bot

## Description
Etymology Bot is a Telegram bot that challenges users with questions about the origins of words. Users can participate in an etymology quiz and solve anagram puzzles related to word origins.

## Features
- **Etymology Quiz:** Users are given a word and must choose the correct language group it originates from.
- **Anagram Challenge:** Users solve anagrams related to the etymology of words.
- **Real-time Answer Validation:** The bot checks answers and provides immediate feedback.

## Installation

### Prerequisites
- Python 3.8+
- `aiogram` library
- JSON data file (`questions.json`)

### Setup
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/etymology-bot.git
   cd etymology-bot
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Add your bot token to `config.py`:
   ```python
   TOKEN = "YOUR_TELEGRAM_BOT_TOKEN"
   ```
4. Run the bot:
   ```sh
   python bot.py
   ```

## Usage
- **Start the bot:** `/start`
- **Begin an etymology quiz:** `/etymology_quiz`
- **Solve an anagram:** `/etymology_anagram`

## Data Structure
The `questions.json` file contains:
```json
{
  "questions": {
    "футбол": ["Английское", "Немецкое", "Итальянское"],
    "музыка": ["Греческое", "Латинское", "Итальянское"]
  },
  "correct_answers": {
    "футбол": "Английское",
    "музыка": "Греческое"
  },
  "anagrams": {
    "змуыка": "музыка"
  }
}
```


