from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import Command


router = Router()


@router.message(Command('start', prefix='/'))
async def start(message: Message):
    await message.answer(f'Hello {message.from_user.full_name}!')
