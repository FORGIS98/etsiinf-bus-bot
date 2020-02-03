from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

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

    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

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

    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

### Make it look good ###

def start(bot, update):
  update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

def main_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def first_menu(bot, update):
  query = update.callback_query
  bot.edit_message_text(chat_id=query.message.chat_id,
                        message_id=query.message.message_id,
                        text=first_menu_message(),
                        reply_markup=first_menu_keyboard())


### SHOW TO USER ###
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('HELLO', callback_data='m1')],
              [InlineKeyboardButton('HAVE FUN', callback_data='m2')],
              [InlineKeyboardButton('GOOD BYE', callback_data='m3')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

### Messages ###
def menu_message():
  return 'Choose the option in main menu:'

def firstStep_message():
  return 'Choose the submenu in first menu:'


def main():
    updater = Updater(token=os.environ["etsiinfBOT"], use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
    dp.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))

    dp.add_handler(CommandHandler("etsiinf", etsiinf))
    dp.add_handler(CommandHandler("colonia", colonia))

    updater.start_polling()

    updater.idle()

main()
