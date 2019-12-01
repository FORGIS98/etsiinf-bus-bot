from telegram.ext import Updater
from telegram.ext import CommandHandler

import os
import requests




def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="WELCOME")

def get(update, context):
    req = requests.post("https://openapi.emtmadrid.es/v1/hello/")
    context.bot.send_message(chat_id=update.effective_chat.id, text=req.status_code)

def main():
    updater = Updater(token=os.environ["etsiinfBOT"], use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("get", get))

    updater.start_polling()

    updater.idle()

main()
