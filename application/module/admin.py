# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation
from ui.screen_admin import Ui_AdminScreen

import database as db 

# ADMIN SCREEN
class AdminScreen(QMainWindow, Ui_AdminScreen):
    def __init__(self, last_screen, user):
        super(AdminScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = user
        self.frame_left.setGeometry(QtCore.QRect(0, 50, 0, 600))
        self.stackedWidget.setCurrentWidget(self.page_empty)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_exit.clicked.connect(self.exit)
        self.btn_toggle.clicked.connect(self.toggle_menu)
        self.btn_user.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_user)))
        self.btn_user_2.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_user_2)))
        self.btn_song.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_song)))
        self.btn_song_2.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_song_2)))

        self.btn_ban_id.clicked.connect(self.delete_user)
        self.btn_reset_id.clicked.connect(self.reset_user)
        self.btn_online.clicked.connect(self.online_refresh)
        self.btn_search.clicked.connect(self.search_user)
        
        self.btn_add_db.clicked.connect(self.add_song)
        self.btn_search_2.clicked.connect(self.search_song)
        self.btn_delete.clicked.connect(self.delete_song)

        self.show()


    def toggle_menu(self):
        # GET WIDTH & HEIGHT
        width = self.frame_left.width()
        height = self.frame_left.height()

        # SET MAX WIDTH
        if width == 0:
            new_width = 80
            self.btn_toggle.setText('<')
        else:
            new_width = 0
            self.btn_toggle.setText('>')
            self.stackedWidget.setCurrentWidget(self.page_empty)

        # ANIMATION
        self.animation = QPropertyAnimation(self.frame_left, b"size")
        self.animation.setDuration(750)
        self.animation.setStartValue(QtCore.QSize(width, height))
        self.animation.setEndValue(QtCore.QSize(new_width, height))
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()


    def delete_user(self):
        user_id = self.input_ban_id.text()
        if user_id:
            self.input_ban_id.setText('')

            db.delete_user(user_id)


    def reset_user(self):
        user_id = self.input_reset_id.text()
        if user_id:
            self.input_reset_id.setText('')

            db.reset_user_stats(user_id)


    def online_refresh(self):
        self.list_online.clear()

        result = db.get_online()
        for item in result:
            user_id = item[0]
            name = f'{item[1]} {item[2]}'

            item = QtWidgets.QListWidgetItem(f'#{user_id} // {name}')
            self.list_online.addItem(item)


    def search_user(self):
        name = self.input_search.text()
        if name:
            self.input_search.setText('')
            result = db.search_user(name)
            if result is not None:
                user_id = result[0]
                user_name = f'{result[1]} {result[2]}'
                user_email = result[3]
                self.label_search.setPlainText(f'Use button below to find user\'s ID using their username.\nResult: #{user_id} // {user_name} // {user_email}')


    def add_song(self):
        author = self.input_author.text()
        name = self.input_name.text()
        chords = self.input_chords.toPlainText()
        conditions = [author, name, chords]
        
        if all(conditions):
            self.input_author.setText('')
            self.input_name.setText('')
            self.input_chords.setPlainText('')

            db.add_song(self.user.id, author, name, chords)


    def search_song(self):
        name = self.input_search_2.text()
        if name:
            self.input_search_2.setText('')
            self.list_search.clear()

            result = db.search_song(name)
            for item in result:
                song_id = item[0]
                user_id = item[1]
                song_name = f'{item[2]} - {item[3]}'
                times_played = item[5]

                item = QtWidgets.QListWidgetItem(f'#{song_id} // User ID: {user_id} // {song_name}')
                self.list_search.addItem(item)


    def delete_song(self):
        song_id = self.input_delete.text()
        if song_id:
            self.input_delete.setText('')

            db.delete_song(song_id)


    def exit(self):
        self.back.show()
        self.close()