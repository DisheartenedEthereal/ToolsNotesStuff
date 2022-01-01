"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1735083634:AAHFxDW7weOPvQqEoZKGpk8-wYHUZNVXJk0'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("""👋 Hello! SHIPPERING is a bot that will choose a couple of the day in your chat.

Use /help for more info.""")



@dp.message_handler(commands=['shippering'])
async def send_ship(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("""زوج امروز:
HARKASI_JOZ_ROJHINA + ANYONE = ❤️

زوج جدید امروز انتخاب میشود در 23 ساعت ها 59 دقایق 59 ثانیه ها""")
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
