from Button.inline_btn import *
from const import *
from DB.db_user import DBUser
from Button.reply_btn import *
db=DBUser('Users.db')

def start(up, ct):
    if db.check_user(up.message.from_user.id):
        up.message.reply_text('''Assalomu alaykum. Registratsiyadan o'tish uchun quyidagi tugmani bosing.\nEslatib o'taman bu bot faqat CHANGE IT ACADEMY xodimlari uchun !!! ''', reply_markup=ask_phone_uz)
        db.add_user(up.message.from_user.id,0,' ', ' ')
        return STATE_PHONE
    else:
        ct.bot.send_message(up.message.from_user.id, 'Assalomu alaykum. Sizda 2 ta ogohlantirish bor', reply_markup=foods )

def phone_text(up, ct):
    
    

    db.edit_phone(up.message.text, up.message.from_user.id)
    print(up)

def phone_contact(up, ct):
    db.edit_phone(up.message.contact.phone_number, up.message.from_user.id)