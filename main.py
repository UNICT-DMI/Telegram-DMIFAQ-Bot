import logging

from telegram.ext import Updater
from modules.commands import load_commands

from modules.config import load_env

LOGGER = logging.getLogger(__name__)


def main():
    logging.basicConfig(
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        level=logging.INFO)

    updater = Updater(token=load_env("BOT_TOKEN"), use_context=True)

    load_commands(updater.dispatcher)

    LOGGER.info("Polling...")

    updater.start_polling()


if __name__ == "__main__":
    main()
