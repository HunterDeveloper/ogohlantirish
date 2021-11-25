import sqlite3
class DBUser:
    def __init__(self, db_name):
        self.conn=sqlite3.connect(db_name, check_same_thread=False)
        self.conn.row_factory=sqlite3.Row


        
    def db_exequite(self, sql, commit=False, fetchone=False, fechall=False):
        self.conn=sqlite3.connect('Users.db', check_same_thread=False)
        connection =self.conn
        cursor = connection.cursor()
        data=None
        cursor.execute(sql)
        if commit:
            connection.commit()
        if fetchone:
            data = cursor.fetchone()
        if fechall:
            data = cursor.fetchall()

        connection.close()

        return data

    # Foydalanuvchi ma'lumotlar bazasida bor yoki yo'qligini tekshiradigan funksiya
    def check_user(self, id):
        sql = f"SELECT id FROM User WHERE id={id}"
        res=self.db_exequite(sql,fechall=True)
        if len(res)==0: return True
        else : return False

    # Faydalanuvchilarni qo'shuvchi funksiya
    def add_user(self, id, phone, name, lang):
        sql = f"INSERT INTO User VALUES( {id}, {phone}, '{name}', '{lang}')"
        self.db_exequite(sql,commit=True)

    def edit_lang(self, lang, id):
        sql = f''' UPDATE User
                SET lang='{lang}'
                WHERE id={id};'''
        self.db_exequite(sql, commit=True)

    def edit_phone(self, phone, id):
        sql = f''' UPDATE User
                SET phone='{phone}'
                WHERE id={id};'''
        self.db_exequite(sql, commit=True)
