# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from ui.screen_about import Ui_AboutScreen

import webbrowser
from social_media import links

# ABOUT SCREEN
class AboutScreen(QMainWindow, Ui_AboutScreen):
    def __init__(self, last_screen, user):
        super(AboutScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = user

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_exit.clicked.connect(self.exit)
        self.btn_fb.clicked.connect(lambda: webbrowser.open(links['fb']))
        self.btn_ig.clicked.connect(lambda: webbrowser.open(links['ig']))
        self.btn_yt.clicked.connect(lambda: webbrowser.open(links['yt']))
        self.btn_in.clicked.connect(lambda: webbrowser.open(links['in']))
        self.btn_git.clicked.connect(lambda: webbrowser.open(links['git']))

        self.show()


    def exit(self):
        self.back.show()
        self.close()