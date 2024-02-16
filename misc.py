import logging
import os
from aiogram import Bot, Dispatcher
from game import Game


bot = Bot(token=os.getenv('6328093163:AAHOKzMvaEHs6znJxCFA9IYaWypdkbnYK-4'))
dp = Dispatcher(bot)
g = Game('crocobot.db')
logging.basicConfig(level=logging.INFO)
