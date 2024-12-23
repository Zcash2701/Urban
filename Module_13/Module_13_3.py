from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio
from key import key

bot = Bot(token=key)
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def star(message):
    text = 'Привет! Я бот помогающий твоему здоровью.'
    await message.answer(text)

@dp.message_handler()
async def star(message):
    text = 'Введите команду /start, чтобы начать общение.'
    await message.answer(text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)