from aiogram.fsm.state import StatesGroup, State


class UserProfileModel(StatesGroup):
    username = State()
    age = State()
    sex = State()
    photo = State()
    description = State()
    city = State()
    to_find = State()
