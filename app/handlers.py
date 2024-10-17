from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from typing import Dict, Any

from .models import UserProfileModel


router = Router()


@router.message(Command('start', prefix='/'))
async def start(message: Message, state: FSMContext) -> None:
    await state.set_state(UserProfileModel.username)
    await message.answer('Введіть як вас називати.')

@router.message(UserProfileModel.username)
async def process_name(message: Message, state: FSMContext) -> None:
    await state.update_data(username=message.text)
    await state.set_state(UserProfileModel.age)
    await message.answer('Введіть скільки вам років.')

@router.message(UserProfileModel.age)
async def process_age(message: Message, state: FSMContext) -> None:
    await state.update_data(age=message.text)
    await state.set_state(UserProfileModel.sex)
    await message.answer('Введіть вашу стать.')

@router.message(UserProfileModel.sex)
async def process_sex(message: Message, state: FSMContext) -> None:
    await state.update_data(sex=message.text)
    await state.set_state(UserProfileModel.photo)
    await message.answer('Надішліть ваше фото.')

@router.message(UserProfileModel.photo)
async def process_photo(message: Message, state: FSMContext) -> None:
    await state.update_data(photo=message.text)
    await state.set_state(UserProfileModel.description)
    await message.answer('Напишіть текст до вашої анкети.')

@router.message(UserProfileModel.description)
async def process_description(message: Message, state: FSMContext) -> None:
    await state.update_data(description=message.text)
    await state.set_state(UserProfileModel.city)
    await message.answer('Введіть ваше місто.')

@router.message(UserProfileModel.city)
async def process_city(message: Message, state: FSMContext) -> None:
    await state.update_data(city=message.text)
    await state.set_state(UserProfileModel.to_find)
    await message.answer('Введіть стать вашого майбутнього партнера.')

@router.message(UserProfileModel.to_find)
async def process_to_find(message: Message, state: FSMContext) -> None:
    data = await state.update_data(to_find=message.text)
    await state.clear()
    await show_summary(message=message, data=data)


async def show_summary(message: Message, data: Dict[str, Any]):
    user_response = ''
    for info in data.values():
        user_response += info + '\n'
    await message.answer(text=user_response.strip())

# username = State()
#     age = State()
#     sex = State()
#     photo = State()
#     description = State()
#     city = State()
#     to_find = State()