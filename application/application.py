# 9d795f-ac907c-baa799-cdcdcd

# Importing the libraries
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow

# Importing UI
from ui.screen_loading import Ui_LoadingScreen
from ui.screen_welcome import Ui_WelcomeScreen

# Import the modules
from module.main_menu import MenuScreen
from module.popup import PopupError

# Import database functions
import database as db

# Importing libraries for social media buttons
import webbrowser
from social_media import links

# Global variables
counter = 0
db_user = None

# Welcome screen (login/register)
class WelcomeScreen(QMainWindow, Ui_WelcomeScreen):
    def __init__(self):
        super(WelcomeScreen, self).__init__()
        self.setupUi(self)
        self.input_email.setText('username')
        self.input_pw.setText('123456789')

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.login_form = True
        self.btn_switch.clicked.connect(self.change_form)
        self.btn_register.clicked.connect(self.register)
        self.btn_login.clicked.connect(self.login)

        self.btn_fb.clicked.connect(lambda: webbrowser.open(links['fb']))
        self.btn_fb_2.clicked.connect(lambda: webbrowser.open(links['fb']))
        self.btn_ig.clicked.connect(lambda: webbrowser.open(links['ig']))
        self.btn_ig_2.clicked.connect(lambda: webbrowser.open(links['ig']))
        self.btn_yt.clicked.connect(lambda: webbrowser.open(links['yt']))
        self.btn_yt_2.clicked.connect(lambda: webbrowser.open(links['yt']))
        self.btn_in.clicked.connect(lambda: webbrowser.open(links['in']))
        self.btn_in_2.clicked.connect(lambda: webbrowser.open(links['in']))
        self.btn_git.clicked.connect(lambda: webbrowser.open(links['git']))
        self.btn_git_2.clicked.connect(lambda: webbrowser.open(links['git']))

        self.show()


    def change_form(self):
        if self.login_form:
            self.stacked_pages.setCurrentWidget(self.page_register)
            self.btn_switch.setText('>')

            self.login_form = False
        else:
            self.stacked_pages.setCurrentWidget(self.page_login)
            self.btn_switch.setText('<')

            self.login_form = True


    def register(self):
        first_name = self.input_first.text()
        last_name = self.input_last.text()
        email = self.input_email_2.text()
        password = self.input_pw_2.text()
        confirm_pw = self.input_pw_3.text()

        registered = db.check_register(first_name, last_name, email, password, confirm_pw)
        if not registered:
            self.popup = PopupError(self, 'You entered wrong information.', 'COULD NOT REGISTER')
            self.close()
        else:
            global db_user
            user = db.check_login(email, password)
            db_user = user
            self.menu = MenuScreen(user)
            self.close()


    def login(self):
        email = self.input_email.text()
        password = self.input_pw.text()

        user = db.check_login(email, password)
        if not user:
            self.popup = PopupError(self, 'Wrong username or password.', 'COULD NOT LOGIN')
            self.close()
        else:
            global db_user
            db_user = user
            self.menu = MenuScreen(user)
            self.close()


# Loading screen
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
        self.timer.start(15)

        # Change Texts
        QtCore.QTimer.singleShot(100, lambda: self.label_description.setText("<strong>WELCOME</strong> TO GUITAR <strong>AIO</strong>"))
        QtCore.QTimer.singleShot(200, lambda: self.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(300, lambda: self.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))

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
    app.exec_()
    if db_user is not None:
        db_user.user_quit()
    sys.exit()
