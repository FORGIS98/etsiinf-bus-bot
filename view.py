import logging

import os
import controller

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)


def start(update, context):
    update.message.reply_text('WELCOME, THIS IS A WORK IN PROGRESS BOT')


def transporte(update, context)
    keyboard = [[InlineKeyboardButton("ETSIINF", callback_data='etsiinf'),
                 InlineKeyboardButton("Colonia Jardín", callback_data='colonia jardin')],
                [InlineKeyboardButton("Aluche", callback_data='aluche'),
                 InlineKeyboardButton("Moncloa", callback_data='moncloa')],
                [InlineKeyboardButton("Boadilla", callback_data='boadilla'),
                 InlineKeyboardButton("Pozuelo", callback_data='pozuelo')]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Donde te encuentras en este momento:', reply_markup=reply_markup)

def etsiinf(update, context):



def button(update, context):
    query = update.callback_query

    if(query.data == 'etsiinf'):
        query.edit_message_text(text=controller.etsiinf())
    elif(query.data == 'colonia jardin'):
        query.edit_message_text(text=controller.colonia())


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(token=os.environ["etsiinfBOT"], use_context=True)

    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CommandHandler('transporte', transporte))
    updater.dispatcher.add_handler(CallbackQueryHandler(etsiinf, pattern='etsiinf'))

    updater.dispatcher.add_error_handler(error)

    updater.start_polling()

    updater.idle()


main()
