import asyncio

import logging
import sys

from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram import F
from aiogram.utils.formatting import (
   Bold, as_list, as_marked_section
)

from token_data import TOKEN
from weather_handler import router

dp = Dispatcher()
dp.include_router(router)

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
   kb = [
      [
         types.KeyboardButton(text='Команды'),
         types.KeyboardButton(text='Описание бота')
      ],
   ]

   keyboard = types.ReplyKeyboardMarkup(
      keyboard=kb,
      resize_keyboard=True
   )
   await message.answer(f'Привет! С чего начнём?', reply_markup=keyboard)

@dp.message(F.text.lower() == "команды")
async def commands(message: types.Message):
   response = as_list(
      as_marked_section(
         Bold("Команды:"),
         "/weather <город> - прогноз погоды в городе",
         "/forecast <город> - прогноз погоды на 5 дней",
         "/weather_time <город> - прогноз погоды по дате и времени",
         marker="✅ ",
      ),
   )
   await message.answer(**response.as_kwargs())

@dp.message(F.text.lower() == "описание бота")
async def description(message: types.Message):
    await message.answer("Этот бот предоставляет информацию о погоде.")

async def main() -> None:
   bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
   await dp.start_polling(bot)

if __name__ == "__main__":
   logging.basicConfig(level=logging.INFO, stream=sys.stdout)
   asyncio.run(main())

