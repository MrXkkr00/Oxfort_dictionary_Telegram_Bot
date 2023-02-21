"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
from oxfor_dictionary import getDefinitions
from aiogram import Bot, Dispatcher, executor, types
from googletrans import Translator
translater = Translator()

API_TOKEN = '1903749937:AAEI72c2tb3cCE_fyNcvqsFZxhKcP8vkL3s'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Asslomu Alekum \n Men Rasulbek tomonidan yaratildim\nIsmin Jarvir")

@dp.message_handler(commands=[ 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Sizga qanaqadir yordam kerak bo'lsa 99 332 10 38 raqamiga murojat qiling.")


@dp.message_handler()
async def Tarjimon(message: types.Message):
    lang = translater.detect(message.text).lang
    if len(message.text.split()) >1:
        dest = 'uz' if lang =='en' else 'en'
        await message.reply(translater.translate(message.text,dest).text)
    # await bot.send_message(message.chat.id, message.text)
    else:
        word_id=message.text
        lookup=getDefinitions(word_id)
        if lookup :
            await message.reply(getDefinitions(message.text)['definitions'])
            await message.reply_audio(getDefinitions(message.text)['audio'])
        else:
            await message.reply("Bunday so'z topilmadi")





if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)