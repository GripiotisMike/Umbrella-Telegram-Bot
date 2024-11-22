# Umbrella Telegram Bot

Umbrella Bot is a versatile Telegram bot that provides weather updates, company stock information (Tesla), and casual conversation.

---

## Features

- 🌦️ **Weather Updates**: Informs if it will rain in the next 12 hours.
- 🚀 **Tesla Stock Analysis**: Checks and reports significant changes in Tesla stock prices.
- 💬 **Chat Features**: Responds to casual messages with predefined responses.

---

## Installation

1. Clone the repository

2. Install dependencies (pip install):
- python-telegram-bot
- python-dotenv
- requests

3. Replace your credentials in .env file:
- TELEGRAM_TOKEN=your-telegram-token
- BOT_USERNAME=@your-bot-username
- ALPHA_API_KEY=your-alpha-api-key
- NEWS_API_KEY=your-news-api-key
- WEATHER_API_KEY=your-weather-api-key

4. Run the bot:
- python main.py

---

## Usage
- Use /start to begin interaction.
- Use /help to see available commands.
- Send "Will it rain?" or "Tesla" for respective features.
