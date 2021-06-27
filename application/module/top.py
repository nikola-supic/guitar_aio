# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation
from ui.screen_top import Ui_TopScreen

import database as db

# SONGS SCREEN
class TopScreen(QMainWindow, Ui_TopScreen):
    def __init__(self, last_screen, user):
        super(TopScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = user
        self.frame_left.setGeometry(QtCore.QRect(0, 50, 0, 600))
        self.stackedWidget.setCurrentWidget(self.page_empty)

        self.update_top_users()

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_exit.clicked.connect(self.exit)
        self.btn_toggle.clicked.connect(self.toggle_menu)
        self.btn_overall.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_overall)))
        self.btn_daily.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_daily)))
        self.btn_monthly.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_monthly)))
        self.btn_yearly.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_yearly)))

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


    def update_top_users(self):
        # Updating top users (overall)
        result = db.get_top_overall()
        for user in result:
            user_id = user[0]
            name = db.get_name(user_id)
            time = user[1]
            no_sessions = user[2]
            no_songs = user[3]

            item = QtWidgets.QListWidgetItem(f'#{user_id} - {name} - Time: {time} - No. sessions: {no_sessions} ({no_songs})')
            self.list_overall.addItem(item)

        # Updating top users (daily)
        result = db.get_top_daily()
        for user in result:
            user_id = user[0]
            name = db.get_name(user_id)
            time = user[1]
            no_sessions = user[2]
            no_songs = user[3]

            item = QtWidgets.QListWidgetItem(f'#{user_id} - {name} - Time: {time} - No. sessions: {no_sessions} ({no_songs})')
            self.list_daily.addItem(item)

        # Updating top users (monthly)
        result = db.get_top_monthly()
        for user in result:
            user_id = user[0]
            name = db.get_name(user_id)
            time = user[1]
            no_sessions = user[2]
            no_songs = user[3]

            item = QtWidgets.QListWidgetItem(f'#{user_id} - {name} - Time: {time} - No. sessions: {no_sessions} ({no_songs})')
            self.list_monthly.addItem(item)

        # Updating top users (yearly)
        result = db.get_top_yearly()
        for user in result:
            user_id = user[0]
            name = db.get_name(user_id)
            time = user[1]
            no_sessions = user[2]
            no_songs = user[3]

            item = QtWidgets.QListWidgetItem(f'#{user_id} - {name} - Time: {time} - No. sessions: {no_sessions} ({no_songs})')
            self.list_yearly.addItem(item)


    def exit(self):
        self.back.show()
        self.close()