# Importing the libraries
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import QPropertyAnimation
from ui.screen_sessions import Ui_SessionsScreen
from module.popup import PopupInfo

import database as db
from datetime import timedelta

# SESSIONS SCREEN
class SessionsScreen(QMainWindow, Ui_SessionsScreen):
    def __init__(self, last_screen, user):
        super(SessionsScreen, self).__init__()
        self.setupUi(self)
        self.back = last_screen
        self.user = user
        self.frame_left.setGeometry(QtCore.QRect(0, 50, 0, 600))
        self.stacked_pages.setCurrentWidget(self.page_add)
        self.update_list()

        # Remove title bar
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        # Events
        self.btn_exit.clicked.connect(self.exit)
        self.btn_toggle.clicked.connect(self.toggle_menu)
        self.btn_list.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_list)))
        self.btn_request.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_request)))
        self.btn_delete.clicked.connect((lambda: self.stackedWidget.setCurrentWidget(self.page_delete)))

        self.btn_request_id.clicked.connect(self.request_session)
        self.btn_delete_id.clicked.connect(self.delete_session)

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


    def update_list(self):
        session_list = db.get_user_sessions(self.user.id)
        self.list_sessions.clear()

        for count, session in enumerate(session_list):
            session_id = session[0]
            length = session[1]
            no_songs = session[2]

            item = QtWidgets.QListWidgetItem(f'{count+1} // ID # {session_id} // {timedelta(seconds=length)} // No. songs: {no_songs}')
            self.list_sessions.addItem(item)


    def request_session(self):
        session_id = self.input_session.plainText()

        if session_id:
            self.input_session.setText('')
            output_text = db.request_session(self.user.id, session_id)
            self.session_info.setPlainText(output_text)


    def delete_session(self):
        session_id = self.input_delete.text()

        if session_id:
            self.input_delete.setText('')
            db.delete_session(session_id)
            self.popup = PopupInfo(self, "You have successfully deleted session from your session list.", 'DELETED')
            self.close()
            self.update_list()


    def exit(self):
        self.back.show()
        self.close()