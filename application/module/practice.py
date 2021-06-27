# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QSequentialAnimationGroup
from ui.screen_practice import Ui_PracticeScreen
from module.popup import PopupInfo, PopupWarning

import database as db
from random import shuffle
from datetime import datetime, timedelta

# PRACTICE SCREEN
class PracticeScreen(QMainWindow, Ui_PracticeScreen):
    def __init__(self, last_screen, user):
        super(PracticeScreen, self).__init__()

        # Practice variables
        self.song_list = []
        for song in db.get_user_songs(user.id):
            self.song_list.append(song[0])
        self.shuffled_list = self.song_list
        self.practice_reset()
        
        # UI init
        self.setupUi(self)
        self.back = last_screen
        self.user = user
        self.widget_left.setGeometry(QtCore.QRect(200, 50, 0, 550))
        self.widget_right.setGeometry(QtCore.QRect(690, 50, 0, 550))
        self.update_list()
        self.clear_song()
        self.click_time = get_time() + 2

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_exit.clicked.connect(self.exit)
        self.list_songs.itemDoubleClicked.connect(self.choose_song)
        self.btn_start.clicked.connect(self.start)
        self.btn_pause.clicked.connect(self.pause)
        self.btn_finish.clicked.connect(self.finish)
        self.btn_next.clicked.connect(self.next)

        self.show()
        self.label_time.hide()
        self.label_songs.hide()

        # Opening animation
        self.anim_1 = QPropertyAnimation(self.widget_left, b"geometry")
        self.anim_1.setDuration(2000)
        self.anim_1.setStartValue(QtCore.QRect(200, 50, 0, 550))
        self.anim_1.setEndValue(QtCore.QRect(0, 50, 200, 550))
        self.anim_1.setEasingCurve(QtCore.QEasingCurve.OutBounce)
        self.anim_1.start()

        self.anim_2 = QPropertyAnimation(self.widget_right, b"geometry")
        self.anim_2.setDuration(2000)
        self.anim_2.setStartValue(QtCore.QRect(690, 50, 0, 550))
        self.anim_2.setEndValue(QtCore.QRect(690, 50, 90, 550))
        self.anim_2.setEasingCurve(QtCore.QEasingCurve.OutBounce)
        self.anim_2.start()

        self.anim_group = QParallelAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()


    def update_list(self):
        self.list_songs.clear()

        for song_id in self.song_list:
            song_name = db.get_song_name(song_id)
            item = QtWidgets.QListWidgetItem(song_name)
            self.list_songs.addItem(item)


    def choose_song(self):
        if self.practice:
            self.popup = PopupWarning(self, 'You have to finish your practice first.', 'CHOOSE SONG')
            self.close()
        else:
            selected = self.list_songs.currentRow()
            song_id = self.song_list[selected]

            self.update_song(song_id)


    def clear_song(self):
        self.label_author.setText('')
        self.label_name.setText('')
        self.text_chords.setPlainText('')
       

    def update_song(self, song_id):
        song = db.get_song(song_id)
        self.label_author.setText(song.author.upper())
        self.label_name.setText(song.name.upper())
        self.text_chords.setPlainText(song.chords)


    def practice_reset(self):
        self.generator = None
        self.current_song = None
        self.current_song_time = 0
        self.practice = False
        self.practice_time = 0
        self.practice_list = []
        self.practice_time_list = []
        self.paused = False
        self.timer = None


    def practice_timer(self):
        self.practice_time += 1
        self.current_song_time += 1
        self.label_time.setText(f'{timedelta(seconds=self.practice_time)}')


    def remove_short_songs(self):
        temp_list = []
        temp_time_list = []

        for song_id, song_time in zip(self.practice_list, self.practice_time_list):
            if song_time > 10:
                temp_list.append(song_id)
                temp_time_list.append(song_time)

        self.practice_time = sum(temp_time_list)
        self.practice_list = temp_list
        self.practice_time_list = temp_time_list


    def start(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1
        self.button_anim(self.btn_start)

        if self.practice:
            if self.paused:
                self.paused = False
                self.timer.start()
            else:
                self.popup = PopupWarning(self, 'You had already started your practice.', 'START')
                self.close()
        else:
            shuffle(self.shuffled_list)
            self.generator = generate_song(self.shuffled_list)
            song_id = next(self.generator)

            self.current_song = song_id
            self.current_song_time = 0
            self.practice = True
            self.practice_time = 0
            self.practice_list = [song_id]
            self.practice_time_list = []
            self.timer = QtCore.QTimer(self)
            self.timer.timeout.connect(self.practice_timer)
            self.timer.start(1000)

            self.update_song(song_id)
            self.label_time.show()
            self.label_songs.show()
            self.label_songs.setText(f'{len(self.practice_list)}')


    def pause(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1
        self.button_anim(self.btn_pause)

        if not self.practice:
            self.popup = PopupWarning(self, 'You have to start your practice first.', 'PAUSE')
            self.close()
        else:
            if self.paused:
                self.popup = PopupWarning(self, 'You have already paused your practice.\nUse play button to start it again.', 'PAUSE')
                self.close()
            else:
                self.paused = True
                self.timer.stop()

                self.popup = PopupInfo(self, 'You paused your practice timer.', 'PAUSE')
                self.close()


    def finish(self, auto_finish = False):
        if not auto_finish:
            if self.click_time > get_time():
                return False
            self.click_time = get_time()+1
            self.button_anim(self.btn_finish)

        if not self.practice:
            self.popup = PopupWarning(self, 'You have to start your practice first.', 'FINISH')
            self.close()
        else:
            self.practice_time_list.append(self.current_song_time)
            self.remove_short_songs()

            if len(self.practice_list) > 0:
                output_text = ''
                for count, (song_id, song_time) in enumerate(zip(self.practice_list, self.practice_time_list)):
                    song_name = db.get_song_name(song_id)
                    output_text += f'[{count+1} // #{song_id}] {song_name} // {timedelta(seconds=song_time)}\n'

                avg_time = self.practice_time / len(self.practice_list)
                output_text += f'\nTOTAL PRACTICE TIME: {timedelta(seconds=self.practice_time)}\n'
                output_text += f'NO. SONGS PRACTICED: {len(self.practice_list)}\n'
                output_text += f'AVERAGE SONG TIME: {timedelta(seconds=avg_time)}'

                self.label_author.setText('PRACTICE FINISHED!')
                self.label_name.setText('SESSION INFO')
                self.text_chords.setPlainText(output_text)

                # add session to db

                # update user stats
                self.user.stats.update(self.practice_time, len(self.practice_list))
            else:
                self.label_author.setText('')
                self.label_name.setText('')
                self.text_chords.setPlainText('')


            # reset practice variables
            if not self.paused:
                self.timer.stop()
            self.practice_reset()
            self.label_time.hide()
            self.label_songs.hide()


    def next(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1
        self.button_anim(self.btn_next)

        if not self.practice:
            self.popup = PopupWarning(self, 'You have to start your practice first.', 'NEXT')
            self.close()
        else:
            try:
                song_id = next(self.generator)
                self.practice_time_list.append(self.current_song_time)
                self.practice_list.append(song_id)
                self.current_song_time = 0

                self.update_song(song_id)
                self.label_songs.setText(f'{len(self.practice_list)}')

            except StopIteration:
                self.finish(True)


    def button_anim(self, btn):
        x = btn.pos().x()
        y = btn.pos().y()
        width = btn.width()
        height = btn.height()

        self.anim_1 = QPropertyAnimation(btn, b"geometry")
        self.anim_1.setDuration(150)
        self.anim_1.setStartValue(QtCore.QRect(x, y, width, height))
        self.anim_1.setEndValue(QtCore.QRect(x-10, y-10, width+20, height+20))
        self.anim_1.setEasingCurve(QtCore.QEasingCurve.Linear)

        self.anim_2 = QPropertyAnimation(btn, b"geometry")
        self.anim_2.setDuration(150)
        self.anim_2.setStartValue(QtCore.QRect(x-10, y-10, width+20, height+20))
        self.anim_2.setEndValue(QtCore.QRect(x, y, width, height))
        self.anim_2.setEasingCurve(QtCore.QEasingCurve.Linear)

        self.anim_group = QSequentialAnimationGroup()
        self.anim_group.addAnimation(self.anim_1)
        self.anim_group.addAnimation(self.anim_2)
        self.anim_group.start()


    def exit(self):
        if self.click_time > get_time():
            return False
        self.click_time = get_time()+1

        if self.practice:
            self.popup = PopupWarning(self, 'You have to finish your practice first.', 'EXIT')
            self.close()
        else:
            self.back.show()
            self.close()


def generate_song(songs_list):
    for item in songs_list:
        yield item


def get_time():
    return datetime.now().timestamp()