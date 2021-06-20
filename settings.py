from loguru import logger
from aiogram.types import ParseMode
from os import environ

API_TOKEN = environ.get('API_TOKEN')
ADMIN_ID = environ.get('ADMIN_ID').split()
CHANNELS = environ.get('CHANNELS').split()

CAPTION = f"[:::name_of_channel:::](https://t.me/joinchat/:::join_link:::)"

HIDE_SOURCE = True

PM = ParseMode.MARKDOWN

"""Set log settings
loguru.loger.add(*args, **kwargs)
"""
LOG_FILE_NAME = "bot.log"
LOG_MODE = "DEBUG"
MAX_LOG_FILE_SIZE = "10Mb"
COMPRESSION = "zip"

LOG = logger.add(LOG_FILE_NAME, level=LOG_MODE, rotation=MAX_LOG_FILE_SIZE, compression=COMPRESSION)
