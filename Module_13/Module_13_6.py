from key import key
import asyncio
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

bot = Bot(token=key)
dp = Dispatcher(bot, storage=MemoryStorage())
inline_key_board = InlineKeyboardMarkup(
    inline_keyboard=[

        [InlineKeyboardButton(text='Рассчитать', callback_data='calories'),
        InlineKeyboardButton(text='Формула рассчёта', callback_data='formulas')]
    ],
    resize_keyboard = True)

key_board = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')]
    ],
    resize_keyboard=True)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()



@dp.message_handler(commands=['start'])
async def star(message):
    text = 'Привет! Я бот помогающий твоему здоровью.'
    await message.answer(text=text, reply_markup=key_board)


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer(text='Выберете опцию', reply_markup=inline_key_board)


@dp.message_handler(text='Информация')
async def get_info(message):
    await message.answer('Данный бот высчитывает оптимальное количество калорий для похудения или сохранения нормального веса по формуле Миффлина-Сан Жеора.')


@dp.callback_query_handler(text='formulas')
async def get_formul(call):
    formul = '10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5'
    await call.message.answer(text=formul)
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    text = 'Введите свой возраст.'
    await call.message.answer(text)
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)
    UserState.age = await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()



@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)
    UserState.growth = await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight.set()



@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await state.finish()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(result)


@dp.message_handler()
async def echo_message(message):
    await message.answer(message.text)



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
