# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from ui.screen_practice import Ui_PracticeScreen

# PRACTICE SCREEN
class PracticeScreen(QMainWindow, Ui_PracticeScreen):
    def __init__(self, last_screen):
        super(PracticeScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_exit.clicked.connect(self.exit)

        self.show()


    def exit(self):
        self.back.show()
        self.close()