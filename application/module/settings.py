# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation
from ui.screen_settings import Ui_SettingsScreen

import database as db

# SONGS SCREEN
class SettingsScreen(QMainWindow, Ui_SettingsScreen):
    def __init__(self, last_screen, user):
        super(SettingsScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = user
        self.frame_left.setGeometry(QtCore.QRect(0, 50, 0, 600))
        self.stackedWidget.setCurrentWidget(self.page_empty)
        self.input_first.setPlaceholderText(self.user.first)
        self.input_last.setPlaceholderText(self.user.last)
        self.input_email.setPlaceholderText(self.user.email)
        self.input_pw.setPlaceholderText(self.user.password)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_exit.clicked.connect(self.exit)
        self.btn_toggle.clicked.connect(self.toggle_menu)
        self.btn_acc.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_acc)))
        self.btn_keys.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_keys)))

        self.btn_ch_name.clicked.connect(self.change_name)
        self.btn_ch_email.clicked.connect(self.change_email)
        self.btn_ch_pw.clicked.connect(self.change_pw)

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


    def change_name(self):
        first_name = self.input_first.text()
        last_name = self.input_last.text()
        conditions = [first_name, last_name]

        if all(conditions):
            self.input_first.setText('')
            self.input_last.setText('')

            self.user.first = first_name
            self.user.last = last_name
            self.input_first.setPlaceholderText(self.user.first)
            self.input_last.setPlaceholderText(self.user.last)
            db.change_name(self.user.id, first_name, last_name)


    def change_email(self):
        email = self.input_email.text()
        if email:
            self.input_email.setText('')

            self.user.email = email
            self.input_email.setPlaceholderText(self.user.email)
            self.user.update_sql('email', email)


    def change_pw(self):
        pw = self.input_pw.text()
        if pw:
            self.input_pw.setText('')

            self.user.password = pw
            self.input_pw.setPlaceholderText(self.user.password)
            self.user.update_sql('password', pw)


    def exit(self):
        self.back.show()
        self.close()