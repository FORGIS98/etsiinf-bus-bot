# 
# CODE FROM: https://github.com/python-telegram-bot/python-telegram-bot/blob/master/examples/inlinekeyboard2.py
#

import controller
import logging
import os


from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
        Updater,
        CommandHandler,
        CallbackQueryHandler,
        ConversationHandler,
        CallbackContext,
        )

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

# Stages
FIRST, SECOND = range(2)
# Callback data
ETSIINF, ALUCHE, COLONIA, MONCLOA = range(4)


def start(update: Update, context: CallbackContext) -> int:
    user = update.message.from_user
    logger.info("%s ha usado el Bot :3", user.first_name)
    keyboard = [
            [
                InlineKeyboardButton("ETSIINF", callback_data=str(ETSIINF)),
                InlineKeyboardButton("ALUCHE", callback_data=str(ALUCHE)),
                ],
            [
                InlineKeyboardButton("COLONIA", callback_data=str(COLONIA)),
                InlineKeyboardButton("MONCLOA", callback_data=str(MONCLOA)),
                ]
            ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("¿Donde te encuentras?", reply_markup=reply_markup)
    return FIRST


def start_over(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    keyboard = [
            [
                InlineKeyboardButton("ETSIINF", callback_data=str(ETSIINF)),
                InlineKeyboardButton("ALUCHE", callback_data=str(ALUCHE)),
                ],
            [
                InlineKeyboardButton("COLONIA", callback_data=str(COLONIA)),
                InlineKeyboardButton("MONCLOA", callback_data=str(MONCLOA)),
                ]
            ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text("¿Donde te encuentras?", reply_markup=reply_markup)
    return FIRST


def etsiinf(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(
            text = controller.busInfo("etsiinf")
            )
    return FIRST


def aluche(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(
            text = controller.busInfo("aluche")
            )
    return FIRST


def colonia(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(
            text = controller.busInfo("colonia")
            )
    return FIRST


def moncloa(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(
            text = controller.busInfo("moncloa")
            )
    return FIRST


def end(update: Update, context: CallbackContext) -> int:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Hasta la próxima :D")
    return ConversationHandler.END


def main() -> None:
    updater = Updater(os.environ["etsiinfBOT"])

    dispatcher = updater.dispatcher
    conv_handler = ConversationHandler(
            entry_points=[CommandHandler('start', start)],
            states={
                FIRST: [
                    CallbackQueryHandler(etsiinf, pattern='^' + str(ETSIINF) + '$'),
                    CallbackQueryHandler(aluche, pattern='^' + str(ALUCHE) + '$'),
                    CallbackQueryHandler(colonia, pattern='^' + str(COLONIA) + '$'),
                    CallbackQueryHandler(moncloa, pattern='^' + str(MONCLOA) + '$'),
                    ]
                },
            fallbacks=[CommandHandler('start', start)],
            )

    dispatcher.add_handler(conv_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()

