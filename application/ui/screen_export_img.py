# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_export_img.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ExportScreen(object):
    def setupUi(self, ExportScreen):
        ExportScreen.setObjectName("ExportScreen")
        ExportScreen.resize(490, 650)
        ExportScreen.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(ExportScreen)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(0, 0, 490, 650))
        self.frame.setStyleSheet("background-color: rgb(72,72,73);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.input_chords = QtWidgets.QTextEdit(self.centralwidget)
        self.input_chords.setGeometry(QtCore.QRect(0, 0, 490, 650))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.input_chords.setFont(font)
        self.input_chords.setStyleSheet("QTextEdit {\n"
"    background-color: rgb(72,72,73);\n"
"    color: rgb(205,205,205);\n"
"    border-radius: 0px;\n"
"    border: none;\n"
"    padding-left: 2px;\n"
"}")
        self.input_chords.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_chords.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_chords.setReadOnly(True)
        self.input_chords.setTextInteractionFlags(QtCore.Qt.TextSelectableByMouse)
        self.input_chords.setObjectName("input_chords")
        ExportScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(ExportScreen)
        QtCore.QMetaObject.connectSlotsByName(ExportScreen)

    def retranslateUi(self, ExportScreen):
        _translate = QtCore.QCoreApplication.translate
        ExportScreen.setWindowTitle(_translate("ExportScreen", "MainWindow"))
        self.input_chords.setPlaceholderText(_translate("ExportScreen", "Chords"))
import res_rc
