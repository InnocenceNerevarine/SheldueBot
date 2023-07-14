from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os

load_dotenv()
bot = Bot('TOKEN')
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer(f'{message.from_user.first_name}, добро пожаловать в расписание-бот')


@dp.message_handler()
async def noneanwser(message: types.Message):
    await message.reply('Я тебя не понимаю')

if __name__ == '__main__':
    executor.start_polling(dp)