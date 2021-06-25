# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from ui.screen_about import Ui_AboutScreen

# ABOUT SCREEN
class AboutScreen(QMainWindow, Ui_AboutScreen):
    def __init__(self, last_screen):
        super(AboutScreen, self).__init__()
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