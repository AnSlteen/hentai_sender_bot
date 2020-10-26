import random
import config
import requests
from aiogram import types, Bot, Dispatcher, executor
from apscheduler.schedulers.asyncio import AsyncIOScheduler

URL = 'https://nekos.life/api/v2/img'

bot = Bot(token=config.bot_token)
dp = Dispatcher(bot=bot)

async def send_posts():
    n = random.choice(config.possible)
    response = requests.get(url=f'{URL}/{n}').json()
    await bot.send_photo(config.CHANNEL_ID, response['url'])

if __name__ == '__main__':
    scheduler = AsyncIOScheduler(timezone='UTC')
    scheduler.add_job(send_posts, 'interval', minutes=5)
    scheduler.start()
    executor.start_polling(dp)
