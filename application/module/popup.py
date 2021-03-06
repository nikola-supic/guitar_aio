# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from ui.screen_popup import Ui_PopupScreen

# PRACTICE SCREEN
class PopupScreen(QMainWindow, Ui_PopupScreen):
    def __init__(self, last_screen, title, info, subtitle = '', button_text = 'BACK', custom_colors = False, color='157, 121, 95', bg='72,72,73', text='205,205,205'):
        super(PopupScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        self.label_title.setText(title)
        self.label_subtitle.setText(subtitle)
        self.label_info.setPlainText(info)
        self.btn_back.setText(button_text)

        if custom_colors: 
            self.frame.setStyleSheet(
                "QFrame#frame {\n"
                f"background-color: rgb({bg});\n"
                f"border: 5px solid rgb({color});\n"
                "}")

            self.label_title.setStyleSheet(f"color: rgb({color});")
            self.label_subtitle.setStyleSheet(f"color: rgb({text});")

            self.btn_back.setStyleSheet(
                "QPushButton#btn_back {\n"
                f"background-color: rgb({color});\n"
                f"color: rgb({text});\n"
                "border-radius: 5px;\n"
                "}")

            self.label_info.setStyleSheet(
                "QPlainTextEdit {\n"
                f"background-color: rgba({bg},150);\n"
                f"color: rgb({text});\n"
                "border-radius: 5px;\n"
                f"border: 2px solid rgb({color});\n"
                "}")

        # Events
        self.btn_back.clicked.connect(self.exit)

        self.show()


    def exit(self):
        self.back.show()
        self.close()


def PopupError(last_screen, info, subtitle=''):
    return PopupScreen(last_screen, 'ERROR!', info, subtitle=subtitle, custom_colors=True, color='204, 18, 18', bg='99,5,5')


def PopupWarning(last_screen, info, subtitle=''):
    return PopupScreen(last_screen, 'WARNING!', info, subtitle=subtitle, custom_colors=True, color='49, 18, 204', bg='12,3,56')


def PopupInfo(last_screen, info, subtitle=''):
    return PopupScreen(last_screen, 'INFO!', info, subtitle=subtitle, custom_colors=True, color='17, 191, 64', bg='4, 69, 22')
