from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

import os
import controller as ctr

############################### Bot ############################################
def start(bot, update):
    update.message.reply_text(main_menu_message(), reply_markup=main_menu_keyboard())

def main_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                          message_id=query.message.message_id,
                          text=main_menu_message(),
                          reply_markup=main_menu_keyboard())

def paradaBus_menu(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                            message_id=query.message.message_id,
                            text=paradaBus_menu_message(),
                            reply_markup=paradaBus_menu_keyboard())

def etsiinfResponse(bot, update):
    query = update.callback_query
    bot.edit_message_text(chat_id=query.message.chat_id,
                            message_id=query.message.message_id,
                            text=second_menu_message())
    etsiinfEMTcall()

def first_submenu(bot, update):
    pass

def second_submenu(bot, update):
    pass

############################ Keyboards #########################################
def main_menu_keyboard():
    keyboard = [[InlineKeyboardButton('Paradas Autobus', callback_data='paradaBus')]]
    return InlineKeyboardMarkup(keyboard)

def paradaBus_menu_keyboard():
    keyboard = [[InlineKeyboardButton('ETSIINF', callback_data='etsiinfParada')],
                [InlineKeyboardButton('Colonia Jardin', callback_data='coloniaJardinParada')],
                [InlineKeyboardButton('Atras', callback_data='main')]]
    return InlineKeyboardMarkup(keyboard)

############################# Actions ##########################################

def etsiinfEMTcall(bot, update):
    text = ctr.etsiinf()
    print("Ma text")
    bot.send_message(chat_id=query.message.chat_id, text=text)

############################# Messages #########################################

def main_menu_message():
    return '¿En que puedo ayudarte?'

def paradaBus_menu_message():
    return '¿Donde te encuentras?'

def second_menu_message():
    return 'Time for depart is:'

############################# Handlers #########################################

def main():

    updater = Updater(token=os.environ["etsiinfBOT"], use_context=False)
    
    updater.dispatcher.add_handler(CommandHandler('start', start))
    updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    updater.dispatcher.add_handler(CallbackQueryHandler(paradaBus_menu, pattern='paradaBus'))
    updater.dispatcher.add_handler(CallbackQueryHandler(etsiinfResponse, pattern='etsiinfParada'))
    updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu, pattern='coloniaJardinParada'))
    updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu, pattern='m2_1'))
    
    updater.start_polling()
    # updater.idle()

main()
