from telegram import InlineKeyboardButton, InlineKeyboardMarkup

ask_language = InlineKeyboardMarkup( [ 
    [ InlineKeyboardButton('Uz', callback_data='uz'), InlineKeyboardButton('Ru', callback_data='ru')]
])

foods = InlineKeyboardMarkup([ 
    [ InlineKeyboardButton('๐ฏ Lavash', callback_data='lavash'), InlineKeyboardButton('๐ฑ Set', callback_data='set')],
    [ InlineKeyboardButton('๐ฏ Lavash', callback_data='lavash'), InlineKeyboardButton('๐ฑ Set', callback_data='set')],
    [ InlineKeyboardButton('๐ฏ Lavash', callback_data='lavash'), InlineKeyboardButton('๐ฑ Set', callback_data='set')],
    [ InlineKeyboardButton('๐ฏ Lavash', callback_data='lavash'), InlineKeyboardButton('๐ฑ Set', callback_data='set')],
    [ InlineKeyboardButton('๐ฏ Lavash', callback_data='lavash'), InlineKeyboardButton('๐ฑ Set', callback_data='set')],
    [ InlineKeyboardButton('๐ฏ Lavash', callback_data='lavash'), InlineKeyboardButton('๐ฑ Set', callback_data='set')],
    [ InlineKeyboardButton('๐ฏ Lavash', callback_data='lavash'), InlineKeyboardButton('๐ฑ Set', callback_data='set')],
    [InlineKeyboardButton('๐งพ Buyurtmalar tarixi', callback_data='buyurtmalar_tarixi')],
    [InlineKeyboardButton("๐ Savatchaga o'tish", callback_data='savat')],
    [ InlineKeyboardButton('Karyera', callback_data='karyera'), InlineKeyboardButton("Til o'zgartirish", callback_data='change_lang')]
])