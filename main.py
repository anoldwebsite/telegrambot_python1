from telegram.ext import *  # pip install python-telegram-bot  # https://pypi.org/project/python-telegram-bot/
import responses as res

import os
from dotenv import load_dotenv, find_dotenv  # pip install python-dotenv
from pathlib import Path

path_of_dotenv = os.getcwd() + "/.env"
load_dotenv(Path(path_of_dotenv))

print("Bot started...")


def start_command(update, context):
    update.message.reply_text('Type something random to get started.')


def help_command(update, context):
    update.message.reply_text("If you need help, call your friends or family. I can't help humans. I am a bot.")


def handle_message(update, context):
    text = str(update.message.text)
    response = res.sample_responses(text)
    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def main():
    updater = Updater(os.getenv("API_KEY"), use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()

# To generate contents for .gitignore file
# https://www.toptal.com/developers/gitignore/api/python

