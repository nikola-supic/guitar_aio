# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation

from ui.screen_sessions import Ui_SessionsScreen

# SESSIONS SCREEN
class SessionsScreen(QMainWindow, Ui_SessionsScreen):
    def __init__(self, last_screen):
        super(SessionsScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.frame_left.setGeometry(QtCore.QRect(0, 50, 0, 600))
        self.stackedWidget.setCurrentWidget(self.page_empty)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_exit.clicked.connect(self.exit)
        self.btn_toggle.clicked.connect(self.toggle_menu)
        self.btn_list.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_list)))
        self.btn_request.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_request)))
        self.btn_delete.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_delete)))

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


    def exit(self):
        self.back.show()
        self.close()