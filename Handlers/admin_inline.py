from sqlite3.dbapi2 import connect
from Button.reply_btn import *
from const import *
from DB.db_user import DBUser

db=DBUser('Users.db')
def admin_inline(update, context):
    query=update.callback_query
    id=query.message.chat.id
    if query.data=='check':
        
        context.bot.send_message(id)