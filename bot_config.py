import os
from dotenv import load_dotenv
from aiogram import Dispatcher, Bot


BASE_DIR = os.path.dirname(__file__)
load_dotenv(BASE_DIR + '\\.env')

TOKEN = os.getenv('TOKEN')

dp = Dispatcher()

bot = Bot(token=TOKEN)
