from aiogram import Bot, Dispatcher

from config.config import Config, load_config

config: Config = load_config(".env")
bot: Bot = Bot(token=config.tg_bot.token, parse_mode="HTML")
dp: Dispatcher = Dispatcher()
