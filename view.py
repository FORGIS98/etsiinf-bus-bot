import logging

import os
import controller

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    keyboard = [[InlineKeyboardButton("Buses ETSIINF", callback_data='1'),
                 InlineKeyboardButton("Buses Colonia", callback_data='2')]]
                # [InlineKeyboardButton("Buses Moncloa", callback_data='3')]]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Escoge una opción:', reply_markup=reply_markup)


def button(update, context):
    query = update.callback_query

    if(query.data == '1'):
        query.edit_message_text(text=controller.etsiinf())
    elif(query.data == '2'):
        query.edit_message_text(text=controller.colonia())

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(token=os.environ["etsiinfBOT"], use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(button))
    updater.dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


main()
