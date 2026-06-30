from aiogram import Bot, Dispatcher, Router
from config import  token
import asyncio
from handlers.user import router
bot  = Bot(token)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    print("Бот запустися")
    asyncio.run(main())