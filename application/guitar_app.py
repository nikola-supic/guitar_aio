# 9d795f-ac907c-baa799-cdcdcd

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation

# LOADING SCREEN
from ui.screen_loading import Ui_LoadingScreen
# WELCOME SCREEN
from ui.screen_welcome import Ui_WelcomeScreen
# MAIN SCREEN
from ui.screen_menu import Ui_MenuScreen
# PRACTICE SCREEN
from ui.screen_practice import Ui_PracticeScreen
# SONGS SCREEN
from ui.screen_songs import Ui_SongsScreen
# STATS SCREEN
from ui.screen_stats import Ui_StatsScreen
# SESSIONS SCREEN
from ui.screen_sessions import Ui_SessionsScreen

# GLOBAL VARIABLES
counter = 0

# PRACTICE SCREEN
class PracticeScreen(QMainWindow, Ui_PracticeScreen):
    def __init__(self):
        super(PracticeScreen, self).__init__()
        self.setupUi(self)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events

        self.show()

# SONGS SCREEN
class SongsScreen(QMainWindow, Ui_SongsScreen):
    def __init__(self):
        super(SongsScreen, self).__init__()
        self.setupUi(self)
        self.frame_left.setGeometry(QtCore.QRect(0, 50, 0, 600))
        self.stackedWidget.setCurrentWidget(self.page_empty)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_toggle.clicked.connect(self.toggle_menu)
        self.btn_list.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_list)))
        self.btn_add.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_add)))
        self.btn_delete.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_delete)))
        self.btn_export.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_export)))

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

# STATS SCREEN
class StatsScreen(QMainWindow, Ui_StatsScreen):
    def __init__(self):
        super(StatsScreen, self).__init__()
        self.setupUi(self)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events

        self.show()

# SESSIONS SCREEN
class SessionsScreen(QMainWindow, Ui_SessionsScreen):
    def __init__(self):
        super(SessionsScreen, self).__init__()
        self.setupUi(self)
        self.frame_left.setGeometry(QtCore.QRect(0, 50, 0, 600))
        self.stacked_pages.setCurrentWidget(self.page_empty)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
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

        self.show()

    def practice(self):
        self.practice = PracticeScreen()
        self.close()

    def songs(self):
        self.songs = SongsScreen()
        self.close()

    def stats(self):
        self.stats = StatsScreen()
        self.close()

    def sessions(self):
        self.sessions = SessionsScreen()
        self.close()

# WELCOME SCREEN
class WelcomeScreen(QMainWindow, Ui_WelcomeScreen):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        self.setupUi(self)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.login_form = True
        self.btn_switch.clicked.connect(self.change_form)
        self.btn_register.clicked.connect(self.register)
        self.btn_login.clicked.connect(self.login)

        self.show()

    def change_form(self):
        if self.login_form:
            self.stacked_pages.setCurrentWidget(self.page_register)
            self.btn_switch.setText('<')

            self.login_form = False
        else:
            self.stacked_pages.setCurrentWidget(self.page_login)
            self.btn_switch.setText('>')

            self.login_form = True

    def register(self):
        self.menu = MenuScreen()
        self.close()

    def login(self):
        self.menu = MenuScreen()
        self.close()


# LOADING SCREEN
class LoadingScreen(QMainWindow, Ui_LoadingScreen):
    def __init__(self):
        super(LoadingScreen, self).__init__()
        self.setupUi(self)

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Loading timer
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(20)

        # Change Texts
        QtCore.QTimer.singleShot(1000, lambda: self.label_description.setText("<strong>WELCOME</strong> TO GUITAR <strong>AIO</strong>"))
        QtCore.QTimer.singleShot(2000, lambda: self.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))

        self.show()

    def progress(self):
        global counter
        self.progressBar.setValue(counter)

        # Close loading screen and open welcome screen
        if counter > 100:
            self.timer.stop()
            self.welcome = WelcomeScreen()
            self.close()

        counter += 1

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = LoadingScreen()
    sys.exit(app.exec_())