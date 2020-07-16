import logging

import telebot

import settings
from commands import *


logger = logging.getLogger(__file__)
logger.setLevel(logging.INFO)


try:
    bot = telebot.AsyncTeleBot(settings.TELEGRAM_TOKEN)
except Exception as exc:
    logger.exception(str(exc))


def start_bot():
    pass


if __name__ == '__main__':
    start_bot()
