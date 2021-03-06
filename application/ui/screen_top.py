# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_top.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_TopScreen(object):
    def setupUi(self, TopScreen):
        TopScreen.setObjectName("TopScreen")
        TopScreen.resize(490, 650)
        TopScreen.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(TopScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 490, 650))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_top = QtWidgets.QFrame(self.frame)
        self.frame_top.setGeometry(QtCore.QRect(0, 0, 490, 50))
        self.frame_top.setStyleSheet("QFrame{\n"
"    background-color: rgb(72,72,73);\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"QPushButton#btn_toggle, #btn_exit {\n"
"    background-color: rgb(157, 121, 95);\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_toggle:hover, #btn_exit:hover {\n"
"    background-color: rgb(143, 110, 86);\n"
"}\n"
"QPushButton#btn_toggle:pressed, #btn_exit:pressed {\n"
"    background-color: rgb(130, 100, 78);\n"
"}\n"
"")
        self.frame_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_top.setObjectName("frame_top")
        self.btn_exit = QtWidgets.QPushButton(self.frame_top)
        self.btn_exit.setGeometry(QtCore.QRect(420, 10, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("")
        self.btn_exit.setObjectName("btn_exit")
        self.btn_toggle = QtWidgets.QPushButton(self.frame_top)
        self.btn_toggle.setGeometry(QtCore.QRect(10, 10, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_toggle.setFont(font)
        self.btn_toggle.setStyleSheet("")
        self.btn_toggle.setObjectName("btn_toggle")
        self.label = QtWidgets.QLabel(self.frame_top)
        self.label.setGeometry(QtCore.QRect(80, -24, 100, 100))
        self.label.setStyleSheet("border-image: url(:/images/images/logo.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_name = QtWidgets.QLabel(self.frame_top)
        self.label_name.setGeometry(QtCore.QRect(80, 13, 231, 50))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("color: rgb(205,205,205);\n"
"background-color: rgba(0,0,0,0);")
        self.label_name.setObjectName("label_name")
        self.frame_left = QtWidgets.QFrame(self.frame)
        self.frame_left.setGeometry(QtCore.QRect(0, 50, 80, 600))
        self.frame_left.setStyleSheet("QFrame{\n"
"    background-color: rgb(72,72,73);\n"
"    border-radius: 0px;\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_overall, #btn_daily, #btn_monthly, #btn_yearly {\n"
"    background-color: rgb(72,72,73);\n"
"    color: rgb(205, 205, 205);\n"
"    border: 0px;\n"
"}\n"
"QPushButton#btn_overall:hover, #btn_daily:hover, #btn_monthly:hover, #btn_yearly:hover {\n"
"    background-color: rgb(157, 121, 95);\n"
"}\n"
"QPushButton#btn_overall:pressed, #btn_daily:pressed, #btn_monthly:pressed, #btn_yearly:pressed{\n"
"    background-color: rgba(130, 100, 78, 255);\n"
"}\n"
"")
        self.frame_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_left.setObjectName("frame_left")
        self.btn_overall = QtWidgets.QPushButton(self.frame_left)
        self.btn_overall.setGeometry(QtCore.QRect(0, 0, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_overall.setFont(font)
        self.btn_overall.setStyleSheet("")
        self.btn_overall.setObjectName("btn_overall")
        self.btn_daily = QtWidgets.QPushButton(self.frame_left)
        self.btn_daily.setGeometry(QtCore.QRect(0, 40, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_daily.setFont(font)
        self.btn_daily.setStyleSheet("")
        self.btn_daily.setObjectName("btn_daily")
        self.btn_monthly = QtWidgets.QPushButton(self.frame_left)
        self.btn_monthly.setGeometry(QtCore.QRect(0, 80, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_monthly.setFont(font)
        self.btn_monthly.setStyleSheet("")
        self.btn_monthly.setObjectName("btn_monthly")
        self.btn_yearly = QtWidgets.QPushButton(self.frame_left)
        self.btn_yearly.setGeometry(QtCore.QRect(0, 120, 80, 40))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_yearly.setFont(font)
        self.btn_yearly.setStyleSheet("")
        self.btn_yearly.setObjectName("btn_yearly")
        self.frame_pages = QtWidgets.QFrame(self.frame)
        self.frame_pages.setGeometry(QtCore.QRect(80, 50, 410, 600))
        self.frame_pages.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_pages.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_pages.setObjectName("frame_pages")
        self.stackedWidget = QtWidgets.QStackedWidget(self.frame_pages)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 410, 600))
        self.stackedWidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.stackedWidget.setStyleSheet("QListWidget {\n"
"    color: rgb(72,72,73);\n"
"    background-color: rgba(205,205,205,150);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgba(157, 121, 95, 255);\n"
"}\n"
"QListWidget::item:hover {\n"
"    color: rgb(205, 205, 205);\n"
"    background-color: rgba(157, 121, 95, 210);\n"
"}\n"
"QListWidget::item:selected {\n"
"    color: rgb(205, 205, 205);\n"
"    background-color: rgba(157, 121, 95, 255);\n"
"}")
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_overall = QtWidgets.QWidget()
        self.page_overall.setObjectName("page_overall")
        self.label_top = QtWidgets.QLabel(self.page_overall)
        self.label_top.setGeometry(QtCore.QRect(10, 2, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_top.setFont(font)
        self.label_top.setStyleSheet("color: rgba(0,0,0,150);\n"
"background-color: rgba(0,0,0,0);")
        self.label_top.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top.setObjectName("label_top")
        self.list_overall = QtWidgets.QListWidget(self.page_overall)
        self.list_overall.setGeometry(QtCore.QRect(10, 40, 390, 550))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.list_overall.setFont(font)
        self.list_overall.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list_overall.setStyleSheet("")
        self.list_overall.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_overall.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_overall.setWordWrap(False)
        self.list_overall.setObjectName("list_overall")
        self.label_line = QtWidgets.QLabel(self.page_overall)
        self.label_line.setGeometry(QtCore.QRect(12, -20, 130, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_line.setFont(font)
        self.label_line.setStyleSheet("color: rgba(255,255,255,255);")
        self.label_line.setObjectName("label_line")
        self.label_top_2 = QtWidgets.QLabel(self.page_overall)
        self.label_top_2.setGeometry(QtCore.QRect(135, 7, 280, 20))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_2.setFont(font)
        self.label_top_2.setStyleSheet("color: rgba(0,0,0,150);\n"
"background-color: rgba(0,0,0,0);")
        self.label_top_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_top_2.setObjectName("label_top_2")
        self.list_overall.raise_()
        self.label_line.raise_()
        self.label_top.raise_()
        self.label_top_2.raise_()
        self.stackedWidget.addWidget(self.page_overall)
        self.page_daily = QtWidgets.QWidget()
        self.page_daily.setObjectName("page_daily")
        self.label_top_3 = QtWidgets.QLabel(self.page_daily)
        self.label_top_3.setGeometry(QtCore.QRect(135, 7, 280, 20))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_3.setFont(font)
        self.label_top_3.setStyleSheet("color: rgba(0,0,0,150);\n"
"background-color: rgba(0,0,0,0);")
        self.label_top_3.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_top_3.setObjectName("label_top_3")
        self.label_top_4 = QtWidgets.QLabel(self.page_daily)
        self.label_top_4.setGeometry(QtCore.QRect(10, 2, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_4.setFont(font)
        self.label_top_4.setStyleSheet("color: rgba(0,0,0,150);\n"
"background-color: rgba(0,0,0,0);")
        self.label_top_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top_4.setObjectName("label_top_4")
        self.list_daily = QtWidgets.QListWidget(self.page_daily)
        self.list_daily.setGeometry(QtCore.QRect(10, 40, 390, 550))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.list_daily.setFont(font)
        self.list_daily.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list_daily.setStyleSheet("QListWidget#list_songs {\n"
"    color: rgb(72,72,73);\n"
"    background-color: rgba(205,205,205,150);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgba(157, 121, 95, 255);\n"
"}\n"
"QListWidget::item:hover {\n"
"    color: rgb(205, 205, 205);\n"
"    background-color: rgba(157, 121, 95, 210);\n"
"}\n"
"QListWidget::item:selected {\n"
"    color: rgb(205, 205, 205);\n"
"    background-color: rgba(157, 121, 95, 255);\n"
"}")
        self.list_daily.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_daily.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_daily.setWordWrap(False)
        self.list_daily.setObjectName("list_daily")
        self.label_line_2 = QtWidgets.QLabel(self.page_daily)
        self.label_line_2.setGeometry(QtCore.QRect(12, -22, 130, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_line_2.setFont(font)
        self.label_line_2.setStyleSheet("color: rgba(255,255,255,255);")
        self.label_line_2.setObjectName("label_line_2")
        self.label_top_3.raise_()
        self.list_daily.raise_()
        self.label_line_2.raise_()
        self.label_top_4.raise_()
        self.stackedWidget.addWidget(self.page_daily)
        self.page_monthly = QtWidgets.QWidget()
        self.page_monthly.setObjectName("page_monthly")
        self.label_line_3 = QtWidgets.QLabel(self.page_monthly)
        self.label_line_3.setGeometry(QtCore.QRect(12, -22, 130, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_line_3.setFont(font)
        self.label_line_3.setStyleSheet("color: rgba(255,255,255,255);")
        self.label_line_3.setObjectName("label_line_3")
        self.list_monthly = QtWidgets.QListWidget(self.page_monthly)
        self.list_monthly.setGeometry(QtCore.QRect(10, 40, 390, 550))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.list_monthly.setFont(font)
        self.list_monthly.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list_monthly.setStyleSheet("QListWidget#list_songs {\n"
"    color: rgb(72,72,73);\n"
"    background-color: rgba(205,205,205,150);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgba(157, 121, 95, 255);\n"
"}\n"
"QListWidget::item:hover {\n"
"    color: rgb(205, 205, 205);\n"
"    background-color: rgba(157, 121, 95, 210);\n"
"}\n"
"QListWidget::item:selected {\n"
"    color: rgb(205, 205, 205);\n"
"    background-color: rgba(157, 121, 95, 255);\n"
"}")
        self.list_monthly.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_monthly.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_monthly.setWordWrap(False)
        self.list_monthly.setObjectName("list_monthly")
        self.label_top_5 = QtWidgets.QLabel(self.page_monthly)
        self.label_top_5.setGeometry(QtCore.QRect(135, 7, 280, 20))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_5.setFont(font)
        self.label_top_5.setStyleSheet("color: rgba(0,0,0,150);\n"
"background-color: rgba(0,0,0,0);")
        self.label_top_5.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_top_5.setObjectName("label_top_5")
        self.label_top_6 = QtWidgets.QLabel(self.page_monthly)
        self.label_top_6.setGeometry(QtCore.QRect(10, 2, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_6.setFont(font)
        self.label_top_6.setStyleSheet("color: rgba(0,0,0,150);\n"
"background-color: rgba(0,0,0,0);")
        self.label_top_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top_6.setObjectName("label_top_6")
        self.stackedWidget.addWidget(self.page_monthly)
        self.page_yearly = QtWidgets.QWidget()
        self.page_yearly.setObjectName("page_yearly")
        self.label_line_4 = QtWidgets.QLabel(self.page_yearly)
        self.label_line_4.setGeometry(QtCore.QRect(12, -22, 130, 61))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_line_4.setFont(font)
        self.label_line_4.setStyleSheet("color: rgba(255,255,255,255);")
        self.label_line_4.setObjectName("label_line_4")
        self.list_yearly = QtWidgets.QListWidget(self.page_yearly)
        self.list_yearly.setGeometry(QtCore.QRect(10, 40, 390, 550))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.list_yearly.setFont(font)
        self.list_yearly.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.list_yearly.setStyleSheet("QListWidget#list_songs {\n"
"    color: rgb(72,72,73);\n"
"    background-color: rgba(205,205,205,150);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgba(157, 121, 95, 255);\n"
"}\n"
"QListWidget::item:hover {\n"
"    color: rgb(205, 205, 205);\n"
"    background-color: rgba(157, 121, 95, 210);\n"
"}\n"
"QListWidget::item:selected {\n"
"    color: rgb(205, 205, 205);\n"
"    background-color: rgba(157, 121, 95, 255);\n"
"}")
        self.list_yearly.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_yearly.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.list_yearly.setWordWrap(False)
        self.list_yearly.setObjectName("list_yearly")
        self.label_top_7 = QtWidgets.QLabel(self.page_yearly)
        self.label_top_7.setGeometry(QtCore.QRect(135, 7, 280, 20))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_7.setFont(font)
        self.label_top_7.setStyleSheet("color: rgba(0,0,0,150);\n"
"background-color: rgba(0,0,0,0);")
        self.label_top_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_top_7.setObjectName("label_top_7")
        self.label_top_8 = QtWidgets.QLabel(self.page_yearly)
        self.label_top_8.setGeometry(QtCore.QRect(10, 2, 130, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_top_8.setFont(font)
        self.label_top_8.setStyleSheet("color: rgba(0,0,0,150);\n"
"background-color: rgba(0,0,0,0);")
        self.label_top_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_top_8.setObjectName("label_top_8")
        self.stackedWidget.addWidget(self.page_yearly)
        self.page_empty = QtWidgets.QWidget()
        self.page_empty.setObjectName("page_empty")
        self.stackedWidget.addWidget(self.page_empty)
        self.frame_bg = QtWidgets.QFrame(self.frame)
        self.frame_bg.setGeometry(QtCore.QRect(0, 0, 490, 650))
        self.frame_bg.setStyleSheet("")
        self.frame_bg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_bg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_bg.setObjectName("frame_bg")
        self.label_bg = QtWidgets.QLabel(self.frame_bg)
        self.label_bg.setGeometry(QtCore.QRect(0, 0, 490, 650))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_bg.setFont(font)
        self.label_bg.setStyleSheet("border-image: url(:/images/images/bg.jpg);")
        self.label_bg.setText("")
        self.label_bg.setObjectName("label_bg")
        self.frame_bg.raise_()
        self.frame_pages.raise_()
        self.frame_top.raise_()
        self.frame_left.raise_()
        TopScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(TopScreen)
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(TopScreen)

    def retranslateUi(self, TopScreen):
        _translate = QtCore.QCoreApplication.translate
        TopScreen.setWindowTitle(_translate("TopScreen", "MainWindow"))
        self.btn_exit.setText(_translate("TopScreen", "EXIT"))
        self.btn_toggle.setText(_translate("TopScreen", " >"))
        self.label_name.setText(_translate("TopScreen", "GUITAR AIO - Top users"))
        self.btn_overall.setText(_translate("TopScreen", "OVERALL"))
        self.btn_daily.setText(_translate("TopScreen", "DAILY"))
        self.btn_monthly.setText(_translate("TopScreen", "MONTHLY"))
        self.btn_yearly.setText(_translate("TopScreen", "YEARLY"))
        self.label_top.setText(_translate("TopScreen", "OVERALL"))
        self.label_line.setText(_translate("TopScreen", "________________"))
        self.label_top_2.setText(_translate("TopScreen", "- users with most practice time"))
        self.label_top_3.setText(_translate("TopScreen", "- users with most practice time today"))
        self.label_top_4.setText(_translate("TopScreen", "DAILY"))
        self.label_line_2.setText(_translate("TopScreen", "________________"))
        self.label_line_3.setText(_translate("TopScreen", "________________"))
        self.label_top_5.setText(_translate("TopScreen", "- users with most practice time this month"))
        self.label_top_6.setText(_translate("TopScreen", "MONTHLY"))
        self.label_line_4.setText(_translate("TopScreen", "________________"))
        self.label_top_7.setText(_translate("TopScreen", "- users with most practice time this year"))
        self.label_top_8.setText(_translate("TopScreen", "YEARLY"))
import res_rc
