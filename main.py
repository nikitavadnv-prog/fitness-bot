import os
from flask import Flask, request
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)
import logging

TOKEN = "8318226107:AAGio8GHPu1c9grmuM7L59YDRo50j631Uss"  
GYM_PHOTO_URL = "https://i.imgur.com/5XJkRl9.png"  

app = Flask(__name__)
application = Application.builder().token(TOKEN).build()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Добро пожаловать!")

application.add_handler(CommandHandler("start", start))

@app.route("/")
def index():
    return "Bot is running!"

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.get_json(force=True)
    update = Update.de_json(data, application.bot)
    application.update_queue.put(update)
    return "ok"

if __name__ == "__main__":
    # Устанавливаем webhook для Telegram
    application.bot.set_webhook(url=f"{WEBHOOK_URL}/webhook")
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))





