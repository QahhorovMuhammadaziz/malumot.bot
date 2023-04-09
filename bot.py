# MALUMOT BERUVCHI BOT
import wikipedia

import logging

from aiogram import Bot, Dispatcher, executor, types

logger = logging.getLogger(__name__)

API_TOKEN = '6168389704:AAF4eQm54chE8jZT95mrFlD3VmHP4lb3EA8'


# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Wikipedia Botiga Xush kelibsiz")


@dp.message_handler()
async def sendWiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)

    except Exception as error:
        logger.error(error)
        await message.answer("Bu mavzuga oid maqola topilmadi")
        
        
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
