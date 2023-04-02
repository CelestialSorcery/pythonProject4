import aiogram
from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters import Text
from aiogram.types import ReplyKeyboardRemove,ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import matplotlib
import os
from dotenv import load_dotenv
load_dotenv()
from aiogram.dispatcher import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import StatesGroup, State

token = os.environ.get("TOKEN")
bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)

class FormKvadrat(StatesGroup):
    number = State()
class FormKoren(StatesGroup):
    number = State()
@dp.message_handler(commands=['start'])
async def process_help_command(message: types.Message):
    await message.reply("Приветствую вас, выберите математическое действиe: /kvadrat или /koren")

@dp.message_handler(commands=['kvadrat'])
async def kvadrat_number(message: types.Message):
    await FormKvadrat.number.set()
    await message.answer("Введите число")

@dp.message_handler(state=FormKvadrat.number)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        await message.answer(int(message.text)**2)
        await state.finish()

@dp.message_handler(commands=['koren'])
async def koren_number(message: types.Message):
    await FormKoren.number.set()
    await message.answer("Введите число")

@dp.message_handler(state=FormKoren.number)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['number'] = message.text
        await message.answer(int(message.text)**0.5)
        await state.finish()


# @dp.message_handler(commands=['kvadrat'])
# async def process_help_command(message: types.Message):
#     await message.reply("Пожалуйста введите число")
#     @dp.message_handler()
#     async def echo_message(msg: types.Message):
#         user_answer = int(msg.text.strip())
#         await message.answer(user_answer**2)
#
# @dp.message_handler(commands=['koren'])
# async def process_help_command(message: types.Message):
#     await message.reply("Пожалуйста введите число")
#     @dp.message_handler()
#     async def echo_message(msg: types.Message):
#         user_answer = int(msg.text.strip())
#         await message.answer(user_answer**0.5)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
