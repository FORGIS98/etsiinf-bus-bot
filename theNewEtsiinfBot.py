from telegram.ext import Updater
from telegram.ext import CommandHandler

import os

import EMT

def etsiinf(update, context):
    diccio = EMT.getEtsiinf()
    text = ""

    if(diccio == None):
        context.bot.send_message(chat_id=update.effective_chat.id, text="NO MORE BUSES")

    for i in diccio:
        text += i
        text += " -> "
        text += diccio[i]
        text += "\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text="NO MORE BUSES")

def colonia(update, context):
    diccio = EMT.getColonia()
    text = ""

    if(diccio == None):
        context.bot.send_message(chat_id=update.effective_chat.id, text="NO MORE BUSES")

    for i in diccio:
        text += i
        text += " -> "
        text += diccio[i]
        text += "\n"

    context.bot.send_message(chat_id=update.effective_chat.id, text="NO MORE BUSES")

def main():
    updater = Updater(token=os.environ["etsiinfBOT"], use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("etsiinf", etsiinf))
    dp.add_handler(CommandHandler("colonia", colonia))

    updater.start_polling()

    updater.idle()

main()
