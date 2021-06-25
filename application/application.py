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

# Import database functions
import database as db

# Global variables
counter = 0


# Welcome screen (login/register)
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
            pass
        else:
            user = db.check_login(email, password)
            self.menu = MenuScreen(user)
            self.close()


    def login(self):
        email = self.input_email.text()
        password = self.input_pw.text()

        user = db.check_login(email, password)
        if not user:
            pass
        else:
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