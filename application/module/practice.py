# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation
from ui.screen_practice import Ui_PracticeScreen

# PRACTICE SCREEN
class PracticeScreen(QMainWindow, Ui_PracticeScreen):
    def __init__(self, last_screen):
        super(PracticeScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.widget_left.setGeometry(QtCore.QRect(200, 50, 0, 550))
        self.widget_right.setGeometry(QtCore.QRect(690, 50, 0, 550))

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_exit.clicked.connect(self.exit)

        self.show()

        # ANIMATION
        self.animation = QPropertyAnimation(self.widget_left, b"geometry")
        self.animation.setDuration(2000)
        self.animation.setStartValue(QtCore.QRect(200, 50, 0, 550))
        self.animation.setEndValue(QtCore.QRect(0, 50, 200, 550))
        self.animation.setEasingCurve(QtCore.QEasingCurve.OutBounce)
        self.animation.start()

        self.animation_1 = QPropertyAnimation(self.widget_right, b"geometry")
        self.animation_1.setDuration(2000)
        self.animation_1.setStartValue(QtCore.QRect(690, 50, 0, 550))
        self.animation_1.setEndValue(QtCore.QRect(690, 50, 90, 550))
        self.animation_1.setEasingCurve(QtCore.QEasingCurve.OutBounce)
        self.animation_1.start()



    def exit(self):
        self.back.show()
        self.close()