# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_stats.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StatsScreen(object):
    def setupUi(self, StatsScreen):
        StatsScreen.setObjectName("StatsScreen")
        StatsScreen.resize(490, 650)
        StatsScreen.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(StatsScreen)
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
        self.btn_exit.setGeometry(QtCore.QRect(400, 10, 60, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_exit.setFont(font)
        self.btn_exit.setStyleSheet("")
        self.btn_exit.setObjectName("btn_exit")
        self.label = QtWidgets.QLabel(self.frame_top)
        self.label.setGeometry(QtCore.QRect(20, -24, 100, 100))
        self.label.setStyleSheet("border-image: url(:/images/images/logo.jpg);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_name = QtWidgets.QLabel(self.frame_top)
        self.label_name.setGeometry(QtCore.QRect(20, 13, 300, 50))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_name.setFont(font)
        self.label_name.setStyleSheet("color: rgb(205,205,205);\n"
"background-color: rgba(0,0,0,0);")
        self.label_name.setObjectName("label_name")
        self.frame_main = QtWidgets.QFrame(self.frame)
        self.frame_main.setGeometry(QtCore.QRect(0, 50, 490, 600))
        self.frame_main.setStyleSheet("QFrame#frame_main {\n"
"    border-image: url(:/images/images/bg.jpg);\n"
"}\n"
"QPushButton#btn_reset, #btn_stats, #btn_stats_2, #btn_stats_3, #btn_stats_4 {\n"
"    background-color: rgba(157, 121, 95, 255);\n"
"    color: rgba(255, 255, 255, 210);\n"
"    border-radius: 5px;\n"
"}\n"
"QPushButton#btn_reset:hover, #btn_stats:hover, #btn_stats_2:hover, #btn_stats_3:hover, #btn_stats_4:hover {\n"
"    background-color: rgba(143, 110, 86, 255);\n"
"}\n"
"QPushButton#btn_reset:pressed, #btn_stats:pressed, #btn_stats_2:pressed, #btn_stats_3:pressed, #btn_stats_4:pressed {\n"
"    background-color: rgba(130, 100, 78, 255);\n"
"}")
        self.frame_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_main.setObjectName("frame_main")
        self.label_top = QtWidgets.QLabel(self.frame_main)
        self.label_top.setGeometry(QtCore.QRect(25, 0, 70, 30))
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
        self.label_line_4 = QtWidgets.QLabel(self.frame_main)
        self.label_line_4.setGeometry(QtCore.QRect(22, -23, 70, 60))
        font = QtGui.QFont()
        font.setPointSize(32)
        self.label_line_4.setFont(font)
        self.label_line_4.setStyleSheet("color: rgba(255,255,255,255);")
        self.label_line_4.setObjectName("label_line_4")
        self.label_top_2 = QtWidgets.QLabel(self.frame_main)
        self.label_top_2.setGeometry(QtCore.QRect(87, 5, 280, 20))
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
        self.btn_reset = QtWidgets.QPushButton(self.frame_main)
        self.btn_reset.setGeometry(QtCore.QRect(20, 560, 451, 31))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_reset.setFont(font)
        self.btn_reset.setStyleSheet("")
        self.btn_reset.setObjectName("btn_reset")
        self.label_stats_1 = QtWidgets.QPlainTextEdit(self.frame_main)
        self.label_stats_1.setGeometry(QtCore.QRect(20, 40, 450, 111))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_stats_1.setFont(font)
        self.label_stats_1.setStyleSheet("background-color: rgba(205,205,205,150);\n"
"color: rgb(72,72,73);\n"
"border-radius: 5px;\n"
"border: 2px solid rgba(157, 121, 95, 255);\n"
"padding-bottom: 2px;")
        self.label_stats_1.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.label_stats_1.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.label_stats_1.setReadOnly(True)
        self.label_stats_1.setObjectName("label_stats_1")
        self.btn_stats = QtWidgets.QPushButton(self.frame_main)
        self.btn_stats.setGeometry(QtCore.QRect(350, 50, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stats.setFont(font)
        self.btn_stats.setStyleSheet("")
        self.btn_stats.setObjectName("btn_stats")
        self.label_stats_2 = QtWidgets.QPlainTextEdit(self.frame_main)
        self.label_stats_2.setGeometry(QtCore.QRect(20, 170, 450, 111))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_stats_2.setFont(font)
        self.label_stats_2.setStyleSheet("background-color: rgba(205,205,205,150);\n"
"color: rgb(72,72,73);\n"
"border-radius: 5px;\n"
"border: 2px solid rgba(157, 121, 95, 255);\n"
"padding-bottom: 2px;")
        self.label_stats_2.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.label_stats_2.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.label_stats_2.setReadOnly(True)
        self.label_stats_2.setObjectName("label_stats_2")
        self.label_stats_3 = QtWidgets.QPlainTextEdit(self.frame_main)
        self.label_stats_3.setGeometry(QtCore.QRect(20, 300, 450, 111))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_stats_3.setFont(font)
        self.label_stats_3.setStyleSheet("background-color: rgba(205,205,205,150);\n"
"color: rgb(72,72,73);\n"
"border-radius: 5px;\n"
"border: 2px solid rgba(157, 121, 95, 255);\n"
"padding-bottom: 2px;")
        self.label_stats_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.label_stats_3.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.label_stats_3.setReadOnly(True)
        self.label_stats_3.setObjectName("label_stats_3")
        self.label_stats_4 = QtWidgets.QPlainTextEdit(self.frame_main)
        self.label_stats_4.setGeometry(QtCore.QRect(20, 430, 450, 111))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_stats_4.setFont(font)
        self.label_stats_4.setStyleSheet("background-color: rgba(205,205,205,150);\n"
"color: rgb(72,72,73);\n"
"border-radius: 5px;\n"
"border: 2px solid rgba(157, 121, 95, 255);\n"
"padding-bottom: 2px;")
        self.label_stats_4.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.label_stats_4.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.label_stats_4.setReadOnly(True)
        self.label_stats_4.setObjectName("label_stats_4")
        self.btn_stats_2 = QtWidgets.QPushButton(self.frame_main)
        self.btn_stats_2.setGeometry(QtCore.QRect(350, 180, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stats_2.setFont(font)
        self.btn_stats_2.setStyleSheet("")
        self.btn_stats_2.setObjectName("btn_stats_2")
        self.btn_stats_3 = QtWidgets.QPushButton(self.frame_main)
        self.btn_stats_3.setGeometry(QtCore.QRect(350, 310, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stats_3.setFont(font)
        self.btn_stats_3.setStyleSheet("")
        self.btn_stats_3.setObjectName("btn_stats_3")
        self.btn_stats_4 = QtWidgets.QPushButton(self.frame_main)
        self.btn_stats_4.setGeometry(QtCore.QRect(350, 440, 110, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_stats_4.setFont(font)
        self.btn_stats_4.setStyleSheet("")
        self.btn_stats_4.setObjectName("btn_stats_4")
        self.label_line_4.raise_()
        self.label_top_2.raise_()
        self.label_top.raise_()
        self.btn_reset.raise_()
        self.label_stats_1.raise_()
        self.btn_stats.raise_()
        self.label_stats_2.raise_()
        self.label_stats_3.raise_()
        self.label_stats_4.raise_()
        self.btn_stats_2.raise_()
        self.btn_stats_3.raise_()
        self.btn_stats_4.raise_()
        self.frame_main.raise_()
        self.frame_top.raise_()
        StatsScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(StatsScreen)
        QtCore.QMetaObject.connectSlotsByName(StatsScreen)

    def retranslateUi(self, StatsScreen):
        _translate = QtCore.QCoreApplication.translate
        StatsScreen.setWindowTitle(_translate("StatsScreen", "MainWindow"))
        self.btn_exit.setText(_translate("StatsScreen", "EXIT"))
        self.label_name.setText(_translate("StatsScreen", "GUITAR AIO - Stats"))
        self.label_top.setText(_translate("StatsScreen", "STATS"))
        self.label_line_4.setText(_translate("StatsScreen", "________________"))
        self.label_top_2.setText(_translate("StatsScreen", "- Use this menu to overlook your stats"))
        self.btn_reset.setText(_translate("StatsScreen", "RESET STATS (be careful using this)"))
        self.label_stats_1.setPlainText(_translate("StatsScreen", "Row #1\n"
"Row #2\n"
"Row #3\n"
"Row #4\n"
""))
        self.btn_stats.setText(_translate("StatsScreen", "ALL TIME"))
        self.label_stats_2.setPlainText(_translate("StatsScreen", "Row #1\n"
"Row #2\n"
"Row #3\n"
"Row #4\n"
""))
        self.label_stats_3.setPlainText(_translate("StatsScreen", "Row #1\n"
"Row #2\n"
"Row #3\n"
"Row #4\n"
""))
        self.label_stats_4.setPlainText(_translate("StatsScreen", "Row #1\n"
"Row #2\n"
"Row #3\n"
"Row #4\n"
""))
        self.btn_stats_2.setText(_translate("StatsScreen", "DAILY"))
        self.btn_stats_3.setText(_translate("StatsScreen", "MONTHLY"))
        self.btn_stats_4.setText(_translate("StatsScreen", "YEAR"))
import res_rc
