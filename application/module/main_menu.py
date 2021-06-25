# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from ui.screen_menu import Ui_MenuScreen

# Import the modules
from module.practice import PracticeScreen
from module.songs import SongsScreen
from module.stats import StatsScreen
from module.sessions import SessionsScreen
from module.about import AboutScreen


# MAIN SCREEN
class MenuScreen(QMainWindow, Ui_MenuScreen):
    def __init__(self):
        super(MenuScreen, self).__init__()
        self.setupUi(self)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_practice.clicked.connect(self.practice)
        self.btn_songs.clicked.connect(self.songs)
        self.btn_stats.clicked.connect(self.stats)
        self.btn_sessions.clicked.connect(self.sessions)
        self.btn_top.clicked.connect(self.top_users)
        self.btn_settings.clicked.connect(self.settings)
        self.btn_about.clicked.connect(self.about)
        self.btn_admin.clicked.connect(self.admin)
        self.btn_exit.clicked.connect(sys.exit)

        self.show()


    def practice(self):
        self.practice = PracticeScreen(self)
        self.close()


    def songs(self):
        self.songs = SongsScreen(self)
        self.close()


    def stats(self):
        self.stats = StatsScreen(self)
        self.close()


    def sessions(self):
        self.sessions = SessionsScreen(self)
        self.close()


    def top_users(self):
        pass


    def settings(self):
        pass


    def about(self):
        self.about = AboutScreen(self)
        self.close()


    def admin(self):
        pass

