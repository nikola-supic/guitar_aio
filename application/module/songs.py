# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation
from ui.screen_songs import Ui_SongsScreen
from ui.screen_export_img import Ui_ExportScreen
from module.popup import PopupInfo

import database as db
import pyscreenshot as ss

# SONGS SCREEN
class SongsScreen(QMainWindow, Ui_SongsScreen):
    def __init__(self, last_screen, user):
        super(SongsScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = user
        self.frame_left.setGeometry(QtCore.QRect(0, 50, 0, 600))
        self.stackedWidget.setCurrentWidget(self.page_empty)
        self.update_list()

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_exit.clicked.connect(self.exit)
        self.btn_toggle.clicked.connect(self.toggle_menu)
        self.btn_list.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_list)))
        self.btn_add.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_add)))
        self.btn_delete.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_delete)))
        self.btn_export.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_export)))
        self.btn_search.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_search)))

        self.btn_create.clicked.connect(self.add_song)
        self.btn_delete_id.clicked.connect(self.delete_song)
        self.btn_export_txt.clicked.connect(self.export_txt)
        self.btn_export_img.clicked.connect(self.export_img)
        self.btn_search_2.clicked.connect(self.search_song)
        self.list_search.itemDoubleClicked.connect(self.add_user_song)

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


    def update_list(self):
        song_list = db.get_user_songs(self.user.id)
        self.list_songs.clear()

        for count, song in enumerate(song_list):
            song_id = song[0]
            song_name = db.get_song_name(song_id)
            item = QtWidgets.QListWidgetItem(f'{count+1} // ID # {song_id} // {song_name}')
            self.list_songs.addItem(item)


    def add_song(self):
        author = self.input_author.text()
        name = self.input_name.text()
        chords = self.input_chords.toPlainText()
        conditions = [author, name, chords]
        
        if all(conditions):
            self.input_author.setText('')
            self.input_name.setText('')
            self.input_chords.setPlainText('')

            song_id = db.add_song(self.user.id, author, name, chords)
            db.add_user_song(self.user.id, song_id)
            self.popup = PopupInfo(self, "You have successfully added new song to your playlist.", 'ADDED')
            self.close()
            self.update_list()


    def delete_song(self):
        song_id = self.input_delete.text()

        if song_id:
            self.input_delete.setText('')
            db.delete_user_song(self.user.id, song_id)
            self.popup = PopupInfo(self, "You have successfully deleted song from your playlist.", 'DELETED')
            self.close()
            self.update_list()


    def export_txt(self):
        song_list = db.get_user_songs(self.user.id)
        for song_id in song_list:
            song = db.get_song(song_id[0])
            song.export_txt()

        self.popup = PopupInfo(self, f"You have successfully exported {len(song_list)} songs from DB to text files.", 'EXPORTED')
        self.close()


    def export_img(self):
        self.close()
        self.export_screen = ExportScreen(self, self.user)


    def search_song(self):
        name = self.input_search.text()
        if name:
            self.input_search.setText('')
            self.list_search.clear()

            result = db.search_song(name)
            for item in result:
                song_id = item[0]
                user_name = db.get_name(item[1])
                song_name = f'{item[2]} - {item[3]}'

                item = QtWidgets.QListWidgetItem(f'#{song_id} // {user_name} // {song_name}')
                self.list_search.addItem(item)


    def add_user_song(self):
        selected = self.list_search.selectedItems()
        song_id = selected[0].text()[1:]
        song_id = song_id.split()[0]

        if not db.already_in_playlist(self.user.id, song_id):
            db.add_user_song(self.user.id, song_id)
            self.popup = PopupInfo(self, "You have successfully added song to your playlist.", 'ADDED')
            self.close()
            self.update_list()
        else:
            self.popup = PopupInfo(self, "This song is already on your playlist.", 'ADDED')
            self.close()



    def exit(self):
        self.back.show()
        self.close()


# EXPORT SCREEN
class ExportScreen(QMainWindow, Ui_ExportScreen):
    def __init__(self, last_screen, user):
        super(ExportScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = user
        self.song_list = db.get_user_songs(self.user.id)
        self.counter = 0

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Setup first song
        song_id = self.song_list[0]
        song = db.get_song(song_id[0])
        self.input_chords.setPlainText(song.chords)

        # Start timer
        self.show()
        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.export_img)
        self.timer.start(500)


    def export_img(self):
        x1 = self.pos().x()
        y1 = self.pos().y()
        x2 = x1 + self.width()
        y2 = y1 + self.height()

        song_id = self.song_list[self.counter]
        song = db.get_song(song_id[0])
        img = ss.grab(bbox=(x1, y1, x2, y2))
        img.save(f'songs_ss/{song.author} - {song.name}.png')

        self.counter += 1
        if self.counter == len(self.song_list):
            self.timer.stop()
            self.back.show()
            self.close()
        else:
            song_id = self.song_list[self.counter]
            song = db.get_song(song_id[0])
            self.input_chords.setPlainText(song.chords)
