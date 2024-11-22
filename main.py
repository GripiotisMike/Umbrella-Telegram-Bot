import requests
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")
BOT_USERNAME = os.getenv("BOT_USERNAME")
ALPHA_API_KEY = os.getenv("ALPHA_API_KEY")
NEWS_API_KEY = os.getenv("NEWS_API_KEY")
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
COMPANY_NAME = "Tesla"
today = "your_date_here"  # Replace or dynamically generate the date as needed

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I am an Umbrella!")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, I am an Umbrella!")

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello, this is something new!")

def handle_response(text: str) -> str:
    # Updated code as per your logic, referencing environment variables.
    # Example:
    processed = text.lower()
    if "hello" in processed:
        return "Hi there"
    if "tesla" in processed:
        alpha_endpoint = "https://www.alphavantage.co/query"
        alpha_param = {
            "function": "TIME_SERIES_DAILY",
            "symbol": "TSLA",
            "apikey": ALPHA_API_KEY
        }
        # API calls, logic, and conditions go here.
        return "Response for Tesla"
    # Other conditions
    return "I don't get it."

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    response = handle_response(text)
    await update.message.reply_text(response)

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"Update {update} caused error {context.error}")

if __name__ == "__main__":
    print("Starting bot...")
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    app.add_handler(MessageHandler(filters.TEXT, handle_message))
    app.add_error_handler(error)

    print("Polling...")
    app.run_polling(poll_interval=3)
