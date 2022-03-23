from telegram import Update
from telegram.ext import CallbackContext


def start_cmd_handler(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a bot, please talk to me!")
