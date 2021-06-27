# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from ui.screen_stats import Ui_StatsScreen

import database as db

# STATS SCREEN
class StatsScreen(QMainWindow, Ui_StatsScreen):
    def __init__(self, last_screen, user):
        super(StatsScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = user
        self.update_stats()

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_exit.clicked.connect(self.exit)
        self.btn_reset.clicked.connect(self.reset)

        self.show()


    def reset(self):
        db.reset_user_stats(self.user.id)
        self.user.stats.reset()
        self.update_stats()


    def update_stats(self):
        overall = self.user.stats.overall
        daily = self.user.stats.daily
        monthly = self.user.stats.monthly
        yearly = self.user.stats.yearly
        self.label_stats_1.setPlainText(f'Last time: {overall[0]}\nPractice time: {overall[1]}\nNo. sessions: {overall[2]}\nNo. songs: {overall[3]}')
        self.label_stats_2.setPlainText(f'Last time: {daily[0]}\nPractice time: {daily[1]}\nNo. sessions: {daily[2]}\nNo. songs: {daily[3]}')
        self.label_stats_3.setPlainText(f'Last time: {monthly[0]}\nPractice time: {monthly[1]}\nNo. sessions: {monthly[2]}\nNo. songs: {monthly[3]}')
        self.label_stats_4.setPlainText(f'Last time: {yearly[0]}\nPractice time: {yearly[1]}\nNo. sessions: {yearly[2]}\nNo. songs: {yearly[3]}')


    def exit(self):
        self.back.show()
        self.close()