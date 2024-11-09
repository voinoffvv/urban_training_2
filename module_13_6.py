# Необходимо дополнить код предыдущей задачи, чтобы при нажатии на кнопку 'Рассчитать' присылалась Inline-клавиатруа.
# Создайте клавиатуру InlineKeyboardMarkup с 2 кнопками InlineKeyboardButton:
#
#     С текстом 'Рассчитать норму калорий' и callback_data='calories'
#     С текстом 'Формулы расчёта' и callback_data='formulas'
#
# Создайте новую функцию main_menu(message), которая:
#
#     Будет обёрнута в декоратор message_handler, срабатывающий при передаче текста 'Рассчитать'.
#     Сама функция будет присылать ранее созданное Inline меню и текст 'Выберите опцию:'
#
# Создайте новую функцию get_formulas(call), которая:
#
#     Будет обёрнута в декоратор callback_query_handler, который будет реагировать на текст 'formulas'.
#     Будет присылать сообщение с формулой Миффлина-Сан Жеора.
#
# Измените функцию set_age и декоратор для неё:
#
#     Декоратор смените на callback_query_handler, который будет реагировать на текст 'calories'.
#     Теперь функция принимает не message, а call. Доступ к сообщению будет следующим - call.message.
#
# По итогу получится следующий алгоритм:
#
#     Вводится команда /start
#     На эту команду присылается обычное меню: 'Рассчитать' и 'Информация'.
#     В ответ на кнопку 'Рассчитать' присылается Inline меню: 'Рассчитать норму калорий' и 'Формулы расчёта'
#     По Inline кнопке 'Формулы расчёта' присылается сообщение с формулой.
#     По Inline кнопке 'Рассчитать норму калорий' начинает работать машина состояний по цепочке.
import aiogram.utils.markdown
from aiogram import Bot, Dispatcher, executor, types
from aiogram.utils import markdown
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

api = 'token'
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())
start_flag = False

kb = ReplyKeyboardMarkup(resize_keyboard=True)
#button1 = KeyboardButton(text='1️⃣ Рассчитать')
button1 = KeyboardButton(text=' Рассчитать')
button2 = KeyboardButton(text='🗺️ Информация')
kb.add(button1)
kb.add(button2)


main_menu1 = InlineKeyboardMarkup()
button11 = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button12 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
main_menu1.add(button11)
main_menu1.add(button12)


class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(text='Рассчитать')
async def main_menu(message: types.Message):
    global start_flag
    if not start_flag:
        await message.answer('Введите команду /start, чтобы начать общение.')
    else:
        await message.answer('Выберите опцию:', reply_markup=main_menu1)



@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.message.answer('для женщин: 10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст (лет):')
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    await state.update_data(age=message.text)

    await message.answer('Введите свой рост в см:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth=message.text)

    await message.answer('Введите свой вес в кг:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight=message.text)

    data = await state.get_data()
    try:
        res = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age'])
        await message.answer(f"Калории для женщин {res - 161} ккал")
        await message.answer(f"Калории для мужчин {res + 5} ккал")
    except:
        await message.answer(f"Введены некорректные данные.")
    await state.finish()


@dp.message_handler(commands='start')
async def start_message(message: types.Message):
    global start_flag
    start_flag = True
    msg = 'Привет! Я бот, помогающий твоему здоровью. Нажмите кнoпку Рассчитать.'
    await message.answer(msg, reply_markup = kb)


@dp.message_handler(text = '🗺️ Информация')
async def send_information(message, state):
 await message.answer('Программа производит расчет суточной нормы калорий по формуле Миффлина-Сан Жеора для мужчин и женщин.')
 await message.answer('Используйте кнопку Рассчитать')


@dp.message_handler()
async def all_messages(message: types.Message):
    global start_flag
    if not start_flag: await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
