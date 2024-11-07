from  aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import sys

api = 'token'
bot = Bot(token = api)
dp = Dispatcher(bot = bot, storage = MemoryStorage())
start_flag = False

@dp.message_handler(commands='start')
async def start_message(message:  types.Message):
    global start_flag
    start_flag = True
    msg= 'Привет! Я бот, помогающий твоему здоровью.'
    await message.answer(msg)
    print(msg)

@dp.message_handler(commands='stop')
async def start_message(message:  types.Message):
    global start_flag
    if start_flag:
        start_flag = False
        msg= 'Бот завершил общение. Пока!'
        await message.answer(msg)
        print(msg)
 #       sys.exit(0)


@dp.message_handler()
async def all_messages(message:  types.Message):
    msg = 'Введите команду /start, чтобы начать общение.'
    global start_flag
    if not start_flag : await message.answer(msg)
    print(msg)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)