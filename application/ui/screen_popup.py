# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_popup.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PopupScreen(object):
    def setupUi(self, PopupScreen):
        PopupScreen.setObjectName("PopupScreen")
        PopupScreen.resize(490, 220)
        self.centralwidget = QtWidgets.QWidget(PopupScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 490, 220))
        self.frame.setStyleSheet("QFrame#frame {    \n"
"    background-color: rgb(72,72,73);    \n"
"    border: 5px solid rgb(157, 121, 95);\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_subtitle = QtWidgets.QLabel(self.frame)
        self.label_subtitle.setGeometry(QtCore.QRect(0, 50, 490, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai Light")
        font.setPointSize(14)
        self.label_subtitle.setFont(font)
        self.label_subtitle.setStyleSheet("color: rgb(205,205,205);")
        self.label_subtitle.setAlignment(QtCore.Qt.AlignCenter)
        self.label_subtitle.setObjectName("label_subtitle")
        self.label_title = QtWidgets.QLabel(self.frame)
        self.label_title.setGeometry(QtCore.QRect(0, 15, 490, 41))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(38)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setStyleSheet("color: rgb(157, 121, 95);")
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.btn_back = QtWidgets.QPushButton(self.frame)
        self.btn_back.setGeometry(QtCore.QRect(20, 170, 450, 30))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.btn_back.setFont(font)
        self.btn_back.setStyleSheet("QPushButton#btn_back {\n"
"    background-color: rgb(157, 121, 95);\n"
"    color: rgb(205,205,205);\n"
"    border-radius: 5px;\n"
"}")
        self.btn_back.setObjectName("btn_back")
        self.label_info = QtWidgets.QPlainTextEdit(self.frame)
        self.label_info.setGeometry(QtCore.QRect(20, 80, 450, 100))
        font = QtGui.QFont()
        font.setFamily("Dubai")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_info.setFont(font)
        self.label_info.setStyleSheet("QPlainTextEdit {\n"
"    background-color: rgba(72,72,73,150);\n"
"    color: rgb(205,205,205);\n"
"    border-radius: 5px;\n"
"    border: 2px solid rgb(157, 121, 95);\n"
"}")
        self.label_info.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.label_info.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.label_info.setReadOnly(True)
        self.label_info.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_info.setObjectName("label_info")
        self.label_subtitle.raise_()
        self.label_title.raise_()
        self.label_info.raise_()
        self.btn_back.raise_()
        PopupScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(PopupScreen)
        QtCore.QMetaObject.connectSlotsByName(PopupScreen)

    def retranslateUi(self, PopupScreen):
        _translate = QtCore.QCoreApplication.translate
        PopupScreen.setWindowTitle(_translate("PopupScreen", "MainWindow"))
        self.label_subtitle.setText(_translate("PopupScreen", "SUBTITLE"))
        self.label_title.setText(_translate("PopupScreen", "TITLE"))
        self.btn_back.setText(_translate("PopupScreen", "BACK"))
        self.label_info.setPlainText(_translate("PopupScreen", "Info #1\n"
"Info #2\n"
"Info #3"))
