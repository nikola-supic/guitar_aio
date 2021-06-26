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
from module.top import TopScreen
from module.settings import SettingsScreen
from module.about import AboutScreen
from module.admin import AdminScreen

# MAIN SCREEN
class MenuScreen(QMainWindow, Ui_MenuScreen):
    def __init__(self, user):
        super(MenuScreen, self).__init__()
        self.setupUi(self)
        self.user = user

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
        self.btn_exit.clicked.connect(self.exit)

        self.show()


    def practice(self):
        self.practice = PracticeScreen(self, self.user)
        self.close()


    def songs(self):
        self.songs = SongsScreen(self, self.user)
        self.close()


    def stats(self):
        self.stats = StatsScreen(self, self.user)
        self.close()


    def sessions(self):
        self.sessions = SessionsScreen(self, self.user)
        self.close()


    def top_users(self):
        self.top = TopScreen(self, self.user)
        self.close()


    def settings(self):
        self.settings = SettingsScreen(self, self.user)
        self.close()


    def about(self):
        self.about = AboutScreen(self, self.user)
        self.close()


    def admin(self):
        self.admin = AdminScreen(self, self.user)
        self.close()


    def exit(self):
        self.user.user_quit()
        sys.exit()

