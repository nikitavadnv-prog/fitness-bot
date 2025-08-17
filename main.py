import sqlite3
from datetime import datetime, timedelta
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes,
    CallbackQueryHandler,
    ConversationHandler,
)
TOKEN = "8318226107:AAGio8GHPu1c9grmuM7L59YDRo50j631Uss"  
GYM_PHOTO_URL = "https://i.imgur.com/5XJkRl9.png"  
