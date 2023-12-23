from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message


router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer('hello')
    # if not IsAdmin():
    #     await message.answer('Привет, админ', reply_markup=replay.admin_start)
    # else:
    #     await message.answer('Привет', reply_markup=replay.user_start)


@router.message(Command('help'))
async def help_handler(message: Message):
    await message.answer(text='Какая-то помощь')
