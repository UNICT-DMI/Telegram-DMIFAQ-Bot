from telegram.ext import CommandHandler

from modules.commands.start import start_cmd_handler


def load_commands(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start_cmd_handler))
