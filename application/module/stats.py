# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from ui.screen_stats import Ui_StatsScreen

# STATS SCREEN
class StatsScreen(QMainWindow, Ui_StatsScreen):
    def __init__(self, last_screen):
        super(StatsScreen, self).__init__()
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