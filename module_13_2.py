from  aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = 'token'
bot = Bot(token = api)
dp = Dispatcher(bot = bot, storage = MemoryStorage())

@dp.message_handler(commands='start')
async def start_message(message:  types.Message):
    msg= 'Привет! Я бот, помогающий твоему здоровью.'
    await message.answer(msg)
    print(msg)

@dp.message_handler()
async def all_messages(message:  types.Message):
    msg = 'Введите команду /start, чтобы начать общение.'
    print(msg)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates = True)