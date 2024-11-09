# Задача "Меньше текста, больше кликов":
# Необходимо дополнить код предыдущей задачи, чтобы вопросы о параметрах тела для расчёта калорий выдавались по нажатию кнопки.
##     Измените massage_handler для функции set_age. Теперь этот хэндлер будет реагировать на текст 'Рассчитать', а не на 'Calories'.
#     Создайте клавиатуру ReplyKeyboardMarkup и 2 кнопки KeyboardButton на ней со следующим текстом: 'Рассчитать' и 'Информация'.
#     Сделайте так, чтобы клавиатура подстраивалась под размеры интерфейса устройства при помощи параметра resize_keyboard.
#     Используйте ранее созданную клавиатуру в ответе функции start, используя параметр reply_markup.
## В итоге при команде /start у вас должна присылаться клавиатура с двумя кнопками. При нажатии на кнопку с надписью
# 'Рассчитать' срабатывает функция set_age с которой начинается работа машины состояний для age, growth и weight

from  aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup

api = 'токен'
bot = Bot(token = api)
dp = Dispatcher(bot = bot, storage = MemoryStorage())
start_flag = False

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
kb.add(button1)
kb.add(button2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight  = State()

@dp.message_handler(commands = 'start')
async def start_message(message:  types.Message):
    global start_flag
    start_flag = True

    msg= 'Привет! Я бот, помогающий твоему здоровью. Нажмите кнoпку Рассчитать.'
    await message.answer(msg, reply_markup = kb)

@dp.message_handler(text = 'Рассчитать')
async def set_age(message:  types.Message):
        await message.answer('Введите свой возраст (лет):')
        await UserState.age.set()

@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)

    await message.answer('Введите свой рост в см:')
    await UserState.growth.set()

@dp.message_handler(state = UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)

    await message.answer('Введите свой вес в кг:')
    await UserState.weight.set()

@dp.message_handler(state = UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)

    data = await state.get_data()
    try:
        res = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age'])
        await message.answer(f"Калории для женщин {res - 161} ккал")
        await message.answer(f"Калории для мужчин {res + 5} ккал")
    except:
        await message.answer(f"Введены некорректные данные.")
    await state.finish()

@dp.message_handler()
async def all_messages(message:  types.Message):
    global start_flag
    if not start_flag : await message.answer('Введите команду /start, чтобы начать общение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)