"""
Created on Sat Jun 26 00:01:00 2021

@author: Sule
@name: database.py
@description: ->
    DOCSTRING:
"""
#!/usr/bin/env python3

from datetime import datetime, timedelta
import mysql.connector

try:
    mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        passwd='',
        database='guitar_aio'
        )
    mycursor = mydb.cursor(buffered=True)
    print('[ + ] Successfully connected to database.')
except mysql.connector.errors.InterfaceError: 
    print('[ - ] Can not connect to database.')

# stats-related functions
class UserStats():
    """
    DOCSTRING:

    """
    def __init__(self, result):
        self.user_id = result[0]
        self.overall = [result[1], result[2], result[3], result[4]]
        self.daily = [result[5], result[6], result[7], result[8]]
        self.monthly = [result[9], result[10], result[11], result[12]]
        self.yearly = [result[13], result[14], result[15], result[16]]


    def reset(self):
        self.overall = [None, 0, 0, 0]
        self.daily = [None, 0, 0, 0]
        self.monthly = [None, 0, 0, 0]
        self.yearly = [None, 0, 0, 0]


def reset_user_stats(user_id):
    sql = "UPDATE stats SET all_last=0, all_time=0, all_sessions=0, all_songs=0 WHERE user_id=%s"
    val = (user_id, )
    mycursor.execute(sql, val)
    mydb.commit() 

    sql = "UPDATE stats SET day_last=0, day_time=0, day_sessions=0, day_songs=0 WHERE user_id=%s"
    val = (user_id, )
    mycursor.execute(sql, val)
    mydb.commit() 

    sql = "UPDATE stats SET month_last=0, month_time=0, month_sessions=0, month_songs=0 WHERE user_id=%s"
    val = (user_id, )
    mycursor.execute(sql, val)
    mydb.commit() 

    sql = "UPDATE stats SET year_last=0, year_time=0, year_sessions=0, year_songs=0 WHERE user_id=%s"
    val = (user_id, )
    mycursor.execute(sql, val)
    mydb.commit()


def get_top_overall():
    mycursor.execute("SELECT user_id, all_time, all_sessions, all_songs FROM stats ORDER BY all_time DESC, all_sessions ASC LIMIT 100")
    result = mycursor.fetchall()
    return result


def get_top_daily():
    mycursor.execute("SELECT user_id, day_time, day_sessions, day_songs FROM stats ORDER BY day_time DESC, day_sessions ASC LIMIT 100")
    result = mycursor.fetchall()
    return result


def get_top_monthly():
    mycursor.execute("SELECT user_id, month_time, month_sessions, month_songs FROM stats ORDER BY month_time DESC, month_sessions ASC LIMIT 100")
    result = mycursor.fetchall()
    return result


def get_top_yearly():
    mycursor.execute("SELECT user_id, year_time, year_sessions, year_songs FROM stats ORDER BY year_time DESC, year_sessions ASC LIMIT 100")
    result = mycursor.fetchall()
    return result



# user-related functions
class User():
    """
    DOCSTRING:

    """
    def __init__(self, result):
        self.id = result[0]
        self.first = result[1]
        self.last = result[2]
        self.email = result[3]
        self.password = result[4]
        self.admin = result[5]
        self.register_date = result[6]
        self.online = True # 7
        self.last_online = datetime.now() # 8

        sql = "UPDATE users SET last_online=%s, online=1 WHERE id=%s"
        val = (self.last_online, self.id, )
        mycursor.execute(sql, val)
        mydb.commit()

        sql = "SELECT * FROM stats WHERE user_id=%s"
        val = (self.id, )
        mycursor.execute(sql, val)
        result = mycursor.fetchone()
        self.stats = UserStats(result)


    def user_quit(self):
        self.last_online = datetime.now()
        self.online = False

        sql = "UPDATE users SET last_online=%s, online=0 WHERE id=%s"
        val = (self.last_online, self.id, )

        mycursor.execute(sql, val)
        mydb.commit()


    def update_sql(self, column, value):
        sql = f"UPDATE users SET {column}=%s WHERE id=%s"
        val = (value, self.id, )
        mycursor.execute(sql, val)
        mydb.commit()


def check_login(email, password):
    sql = "SELECT * FROM users WHERE email=%s AND password=%s"
    val = (email, password, )

    mycursor.execute(sql, val)
    result = mycursor.fetchone()

    if result is not None:
        return User(result)
    return None


def check_register(first_name, last_name, email, password, confirm_pw):
    if len(first_name) < 4:
        return False
    if len(last_name) < 4:
        return False
    if len(email) < 4:
        return False
    if len(password) < 8 or len(password) > 24:
        return False
    if password != confirm_pw:
        return False

    try:
        time = datetime.now()
        sql = "INSERT INTO users (first_name, last_name, email, password, register_date) VALUES (%s, %s, %s, %s, %s)"
        val = (first_name, last_name, email, password, time, )

        mycursor.execute(sql, val)
        mydb.commit()

        mycursor.execute("INSERT INTO stats (all_time) VALUES (0)")
        mydb.commit()

        return True
    except Exception as e:
        print(e)
    return False


def search_user(user_name):
    sql = "SELECT id, first_name, last_name, email FROM users WHERE email LIKE %s"
    val = (user_name, )

    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return result


def change_name(user_id, first_name, last_name):
    sql = "UPDATE users SET first_name = %s, last_name = %s WHERE id = %s"
    val = (first_name, last_name, user_id, )

    mycursor.execute(sql, val)
    mydb.commit()


def delete_user(user_id):
    sql = "DELETE FROM users WHERE id = %s"
    val = (user_id, )

    mycursor.execute(sql, val)
    mydb.commit()


def get_online():
    mycursor.execute("SELECT id, first_name, last_name FROM users WHERE online=1")
    result = mycursor.fetchall()
    return result


def get_name(user_id):
    sql = "SELECT first_name, last_name FROM users WHERE id = %s"
    val = (user_id, )

    mycursor.execute(sql, val)
    result = mycursor.fetchone()
    return f'{result[0]} {result[1]}'

        
# song-related functions
def add_song(user_id, author, name, chords):
    sql = "INSERT INTO songs (user_id, author, name, chords) VALUES (%s, %s, %s, %s)"
    val = (user_id, author, name, chords, )

    mycursor.execute(sql, val)
    mydb.commit()


def search_song(song_name):
    sql = "SELECT * FROM songs WHERE name LIKE %s"
    val = (song_name, )

    mycursor.execute(sql, val)
    result = mycursor.fetchall()
    return result


def delete_song(song_id):
    sql = "DELETE FROM songs WHERE id = %s"
    val = (song_id, )

    mycursor.execute(sql, val)
    mydb.commit()