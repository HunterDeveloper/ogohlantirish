from telegram import ReplyKeyboardMarkup, KeyboardButton

ask_phone_uz = ReplyKeyboardMarkup( [ 
    [KeyboardButton("📱 Telefon raqamni jo'natish", request_contact=True) ]
], resize_keyboard=True)
ask_phone_ru = ReplyKeyboardMarkup( [ 
    [KeyboardButton("📱 Отправить номер телефона", request_contact=True) ]
], resize_keyboard=True)
