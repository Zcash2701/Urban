from key import *
import asyncio
from aiogram.dispatcher import FSMContext
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from crud_functions import *

all_products = get_all_product()

bot = Bot(token=key)
dp = Dispatcher(bot, storage=MemoryStorage())
inline_key_board = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Рассчитать', callback_data='calories'),
        InlineKeyboardButton(text='Формула рассчёта', callback_data='formulas')]
    ],
    resize_keyboard=True)

inline_key_board_Products = InlineKeyboardMarkup(
        inline_keyboard=[
                        [InlineKeyboardButton(text='Продукт 1', callback_data='product_buying'),
                         InlineKeyboardButton(text='Продукт 2', callback_data='product_buying'),
                         InlineKeyboardButton(text='Продукт 3', callback_data='product_buying'),
                         InlineKeyboardButton(text='Продукт 4', callback_data='product_buying')
                         ]
                        ],
    resize_keyboard=True)
registration_board = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Зарегистрироваться')]
    ],
    resize_keyboard=True
)

key_board = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Рассчитать'), KeyboardButton(text='Информация')],
        [KeyboardButton(text='Купить')]
    ],
    resize_keyboard=True)




class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

class RegistrationState(StatesGroup):
    email = State()
    age = State()
    balance = State()



@dp.message_handler(commands=['start'])
async def star(message):
    '''
    username в телеге сам по себе уникальный, на сколько я знаю)
    Я если прям надо, я перепишу согласно прям тз в дз) но мне лично, так больше нравится)
    '''

    username = message.from_user.username
    if not is_included(username):
        text = 'Привет! Я бот помогающий твоему здоровью.'
        await message.answer(text=text, reply_markup=registration_board)
    else:
        text = 'Ты уже зарегистрирован, давай работать дальше.'
        await message.answer(text=text, reply_markup=key_board)



@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer(text='Выберете опцию', reply_markup=inline_key_board)


@dp.message_handler(text='Информация')
async def get_info(message):
    await message.answer('Данный бот высчитывает оптимальное количество калорий для похудения или сохранения нормального веса по формуле Миффлина-Сан Жеора.')


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    for product in all_products:
        with open(product[4], 'rb') as foto:
            text = f"Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}"
            await message.answer(text)
            await message.answer_photo(foto)
    await message.answer(text='Выберете продукт для покупки:', reply_markup=inline_key_board_Products)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer(text='Вы успешно приобрели товар')
    await call.answer()


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


@dp.message_handler(text='Зарегистрироваться')
async def registration(message):
    text = 'Введите ваш email:'
    await message.answer(text=text)
    await RegistrationState.email.set()


@dp.message_handler(state=RegistrationState.email)
async def update_data_email(message, state):
    await state.update_data(email=message.text)
    data = await state.get_data()
    await message.answer(text='Введите ваш возраст:')
    await RegistrationState.age.set()

@dp.message_handler(state=RegistrationState.age)
async def update_data_email(message, state):
    await state.update_data(age=message.text)
    data = await state.get_data()
    await message.answer(text='Регистрация завершена!\nДоброй пожаловать! :)', reply_markup=key_board)
    await state.finish()
    username = message.from_user.username
    email = data['email']
    age = data['age']
    add_user(username, email, age)




@dp.message_handler()
async def all_massages(message):
    await message.answer(text= 'Введите команду /start, чтобы начать общение.')




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
