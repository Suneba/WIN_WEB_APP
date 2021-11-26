# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'app.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWebEngineWidgets import QWebEngineView



class Ui_appdialog(object):
    def setupUi(self, appdialog):
        appdialog.setObjectName("appdialog")
        appdialog.resize(1111, 630)
        appdialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        appdialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.verticalLayout = QtWidgets.QVBoxLayout(appdialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(appdialog)
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_4.setStyleSheet("QWidget#widget_4{\n"
"    background-color:rgb(20,20,20);\n"
"    border-top-left-radius:8px;\n"
"    border-top-right-radius:8px;\n"
"}\n"
"QPushButton{\n"
"    background-color:rgba(0,0,0,0);\n"
"    color:rgb(144,144,144);\n"
"    font:bold;\n"
"    font-size:15px;\n"
"    font-family:entypo;\n"
"}\n"
"QPushButton:hover{\n"
"    color:rgb(142,176,27);\n"
"}\n"
"QPushButton:pressed{\n"
"    padding-top:5px;\n"
"    pading-left:5px;\n"
"    color:rgb(91,88,53);\n"
"}")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_6.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton = QtWidgets.QPushButton(self.widget_4)
        self.pushButton.setMaximumSize(QtCore.QSize(40, 40))
        font = QtGui.QFont()
        font.setFamily("entypo")
        font.setPointSize(-1)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("")
        self.pushButton.setIconSize(QtCore.QSize(33, 50))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_2.setMaximumSize(QtCore.QSize(40, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setStyleSheet("color:rgb(255,0,0)")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.label = QtWidgets.QLabel(self.widget_4)
        self.label.setMaximumSize(QtCore.QSize(15, 15))
        self.label.setStyleSheet("background-color:rgb(255,0,0);\n"
"border-radius:7px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget_4)
        self.label_2.setMaximumSize(QtCore.QSize(75, 30))
        self.label_2.setStyleSheet("color:rgb(255,255,255);")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setStyleSheet("color:rgb(255,0,0)")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_4.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 16777213))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_5.setMinimumSize(QtCore.QSize(10, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.verticalLayout_2.addWidget(self.widget_4)

        self.webEngineView = QWebEngineView(self.widget)
        self.webEngineView.page().setBackgroundColor(QtGui.QColor(45,45,45,255))
        self.webEngineView.setObjectName("webEngineView")
        self.verticalLayout_2.addWidget(self.webEngineView)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(appdialog)
        QtCore.QMetaObject.connectSlotsByName(appdialog)
        #self.pushButton.clicked.connect(appdialog.resize(111, 630))

    def retranslateUi(self, appdialog):
        _translate = QtCore.QCoreApplication.translate
        appdialog.setWindowTitle(_translate("appdialog", "Dialog"))
        self.pushButton_6.setText(_translate("appdialog", "←"))
        self.pushButton.setText(_translate("appdialog", "⌂"))
        self.pushButton_2.setText(_translate("appdialog", "/"))

        self.pushButton_3.setText(_translate("appdialog", "-"))
        self.pushButton_4.setText(_translate("appdialog", ""))
        self.pushButton_5.setText(_translate("appdialog", "X"))
        # self.webEngineView.setText(_translate("appdialog", "TextLabel"))
