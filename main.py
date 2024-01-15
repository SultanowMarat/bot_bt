import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
import answer
import conf

bot = Bot(token=conf.API_TOKEN)
dp = Dispatcher()


async def on_startup():
    await bot.send_message()

@dp.message(Command("start"))
async def start(message: types.Message):

    await message.answer(text=answer.main_answer)

@dp.message(Command("help"))
async def help(message: types.Message):

    await message.answer(text=answer.main_answer)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
