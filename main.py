import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession
from aiogram.filters import Command

from config import BOT_TOKEN, PROXY
from handlers.start import first_msg
from middleware import RoleMiddleware

session = AiohttpSession(proxy=PROXY)
bot = Bot(token=BOT_TOKEN, session=session)
dp = Dispatcher()


async def main():
    dp.message.middleware(RoleMiddleware())
    dp.callback_query.middleware(RoleMiddleware())

    dp.message.register(first_msg, Command('start'))

    await dp.start_polling(bot)

if __name__=="__main__":
    asyncio.run(main())