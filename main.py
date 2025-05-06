import logging
import os
from aiogram import Bot, Dispatcher, types, executor
import asyncio
import datetime

API_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Simple analytics example
def get_daily_digest():
    today = datetime.date.today()
    # In production, this would pull from real APIs or analysis functions
    return f'📊 {today} – Новости:'

- 📈 Биткойн на подъеме
- 🇺🇸 ФРС сохраняет ставку
- 📉 Рынки ждут данных по инфляции

💡 Рекомендация: держать позицию в ETH"

@dp.message_handler(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Привет! Это Mills Digest Bot. Используй /today, чтобы получить аналитику.")

@dp.message_handler(commands=["today"])
async def today_digest(message: types.Message):
    digest = get_daily_digest()
    await message.reply(digest)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
