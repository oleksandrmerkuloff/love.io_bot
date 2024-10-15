import asyncio


from app.handlers import router
from bot_config import bot, dp


dp.include_router(router)

async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
