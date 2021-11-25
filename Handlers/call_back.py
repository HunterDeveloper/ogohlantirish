from sqlite3.dbapi2 import connect
from Button.reply_btn import *
from const import *
from DB.db_user import DBUser

db=DBUser('Users.db')
def inline(update, context):
    query=update.callback_query

    if query.data=='uz':
        context.bot.send_message(query.message.chat.id,"Ro'yxatdan o'tish uchun telefon raqamingizni kiriting\n\nRaqamni +998********* shaklida yuboring.", reply_markup=ask_phone_uz)
        db.edit_lang('uz',query.message.chat.id )
        return STATE_PHONE
    elif query.data=='ru':
        db.edit_lang('ru',query.message.chat.id )
        context.bot.send_message(query.message.chat.id,"Введите свой номер телефона\n\nОтправьте номер в форме +998*********.", reply_markup=ask_phone_ru)
        return STATE_PHONE