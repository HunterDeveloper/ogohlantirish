from telegram.botcommand import BotCommand
from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler, MessageHandler, Filters
from telegram import InlineKeyboardMarkup, InlineKeyboardButton
from Handlers.reseption import start, phone_text, phone_contact
from Handlers.call_back import inline
from const import *

def main():
    updater = Updater(TOKEN)
    dp= updater.dispatcher
    dp.bot.set_my_commands([ 
        BotCommand('start', 'Foydalanishni boshlash'),
        BotCommand('help', 'Qoidalar xaqida'),
        BotCommand('term', 'Foydalanish shartlari'),
        BotCommand('support', 'Biz bilan aloqa')
    ])
    conv_hand=ConversationHandler( 
        entry_points=[CommandHandler('start', start)],
        states={
            STATE_LANGUAGE:[ 
                CallbackQueryHandler(inline)

            ],
            STATE_PHONE: [ 
                MessageHandler(Filters.text, phone_text),
                MessageHandler(Filters.contact, phone_contact),
                CommandHandler('start', start)
            ]
        },
        fallbacks=[CommandHandler('start', start)]
    )
    dp.add_handler(conv_hand)
    updater.start_polling()
    updater.idle()

main()