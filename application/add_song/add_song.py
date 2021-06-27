"""
DOCSTRING: Simple script to add songs to db manually.

"""
import os
import mysql.connector


mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='',
    database='guitar_aio'
    )
mycursor = mydb.cursor()


def get_songs():
    """
    DOCSTRING: function to get .txt files

    """
    songs_list = []
    os.chdir('new_songs')
    files = [f for f in os.listdir('.') if os.path.isfile(f)]
    for txt in files:
        if txt.endswith('.txt'):
            songs_list.append(txt)
    return songs_list


def add_songs(user_id, files, check_name):
    """
    DOCSTRING: function to insert song in db

    """
    for song in files:
        filename = song

        song = song.strip('.txt')
        song = song.split(' - ')
        song_author = song[0].title()
        song_name = song[1].capitalize()

        if check_name:
            answer = input(f'Author: {song_author} // Name: {song_name} // y/n? ')
            while answer not in ('y', 'n'):
                answer = input(f'Author: {song_author} // Name: {song_name} // y/n? ')

            if answer != 'y':
                song_author = input('[>] Enter song author: ')
                song_name = input('[>] Enter song name: ')

        chords = ''
        with open(filename, 'r', encoding='utf8') as file:
            chords = file.read()

        sql = "INSERT INTO songs (user_id, author, name, chords) VALUES (%s, %s, %s, %s)"
        val = (user_id, song_author, song_name, chords)
        mycursor.execute(sql, val)
        song_id = mycursor.lastrowid
        mydb.commit()

        sql = "INSERT INTO user_songs (user_id, song_id) VALUES (%s, %s)"
        val = (user_id, song_id, )
        mycursor.execute(sql, val)
        mydb.commit()



if __name__ == '__main__':
    input_user = int(input('[ > ] Enter user ID: '))
    song_list = get_songs()
    add_songs(input_user, song_list, False)
