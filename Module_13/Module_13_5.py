from key import key
import asyncio
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

bot = Bot(token=key)
dp = Dispatcher(bot, storage=MemoryStorage())

key_board = ReplyKeyboardMarkup(resize_keyboard=True)
button_calc = KeyboardButton(text='Рассчитать')
button_info = KeyboardButton(text='О боте')
key_board.insert(button_calc)
key_board.insert(button_info)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'])
async def star(message):
    text = 'Привет! Я бот помогающий твоему здоровью.'
    await message.answer(text=text, reply_markup=key_board)

@dp.message_handler(text='О боте')
async def get_info(message):
    await message.answer('Данный бот высчитывает оптимальное количество калорий для похудения или сохранения нормального веса по формуле Миффлина-Сан Жеора.')


@dp.message_handler(text='Рассчитать')
async def set_age(message):
    """
    Функцию set_age(message):
    1) Оберните её в message_handler, который реагирует на текстовое сообщение 'Calories'.
    2) Эта функция должна выводить в Telegram-бот сообщение 'Введите свой возраст:'.
    3) После ожидать ввода возраста в атрибут UserState.age при помощи метода set.
    """
    text = 'Введите свой возраст.'
    await message.answer(text)
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    """
    Функцию set_growth(message, state):
    1) Оберните её в message_handler, который реагирует на переданное состояние UserState.age.
    2) Эта функция должна обновлять данные в состоянии age на message.text (написанное пользователем сообщение). Используйте метод update_data.
    3) Далее должна выводить в Telegram-бот сообщение 'Введите свой рост:'.
    4) После ожидать ввода роста в атрибут UserState.growth при помощи метода set.
    """
    await state.update_data(age=message.text)
    UserState.age = await state.get_data()
    await message.answer('Введите свой рост:')
    await UserState.growth.set()



@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    """
    Функцию set_weight(message, state):
    1) Оберните её в message_handler, который реагирует на переданное состояние UserState.growth.
    2) Эта функция должна обновлять данные в состоянии growth на message.text (написанное пользователем сообщение). Используйте метод update_data.
    3) Далее должна выводить в Telegram-бот сообщение 'Введите свой вес:'.
    4) После ожидать ввода роста в атрибут UserState.weight при помощи метода set.
    """
    await state.update_data(growth=message.text)
    UserState.growth = await state.get_data()
    await message.answer('Введите свой вес:')
    await UserState.weight.set()



@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    """
    Функцию send_calories(message, state):
    1) Оберните её в message_handler, который реагирует на переданное состояние UserState.weight.
    2) Эта функция должна обновлять данные в состоянии weight на message.text (написанное пользователем сообщение). Используйте метод update_data.
    3) Далее в функции запомните в переменную data все ранее введённые состояния при помощи state.get_data().
    4) Используйте упрощённую формулу Миффлина - Сан Жеора для подсчёта нормы калорий (для женщин или мужчин - на ваше усмотрение). Данные для формулы берите из ранее объявленной переменной data по ключам age, growth и weight соответственно.
    5) Результат вычисления по формуле отправьте ответом пользователю в Telegram-бот.
    6) Финишируйте машину состояний методом finish().
    """
    await state.update_data(weight=message.text)
    data = await state.get_data()
    await state.finish()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age']) + 5
    await message.answer(result)



@dp.message_handler()
async def all_massages(message):
    await message.answer(text= 'Введите команду /start, чтобы начать общение.')



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
