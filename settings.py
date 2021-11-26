


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SETTINGS(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(290, 215)
        Dialog.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Dialog.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget = QtWidgets.QWidget(Dialog)
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
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self._label_3 = QtWidgets.QLabel(self.widget_4)
        self._label_3.setMaximumSize(QtCore.QSize(200, 20))
        font = QtGui.QFont()
        font.setPointSize(11)
        self._label_3.setFont(font)
        self._label_3.setStyleSheet("color:rgb(144,144,144);")
        self._label_3.setObjectName("_label_3")
        self.horizontalLayout_3.addWidget(self._label_3)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_5.setMinimumSize(QtCore.QSize(10, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n"
                                    "    background-color:rgb(20,20,20);\n"
                                    "    \n"
                                    "}\n"
                                    "QPushButton{\n"
                                    "    background-color:rgba(0,0,0,0);\n"
                                    "    color:rgb(144,144,144);\n"
                                    "    font:bold;\n"
                                    "    font-size:20px;\n"
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
        self.widget_2.setObjectName("widget_2")
        self.formLayout = QtWidgets.QFormLayout(self.widget_2)
        self.formLayout.setObjectName("formLayout")
        # self._label_4 = QtWidgets.QLabel(self.widget_2)
        # self._label_4.setStyleSheet("color:rgb(144,144,144);")
        # self._label_4.setObjectName("_label_4")
        # self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self._label_4)
        self._label_5 = QtWidgets.QLabel(self.widget_2)
        self._label_5.setStyleSheet("color:rgb(144,144,144);")
        self._label_5.setObjectName("_label_5")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self._label_5)
        # self._label_6 = QtWidgets.QLabel(self.widget_2)
        # self._label_6.setStyleSheet("color:rgb(144,144,144);")
        # self._label_6.setObjectName("_label_6")
        # self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self._label_6)
        # self.checkBox_3 = QtWidgets.QCheckBox(self.widget_2)
        # self.checkBox_3.setObjectName("checkBox_3")
        # self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.checkBox_3)
        self.checkBox_2 = QtWidgets.QCheckBox(self.widget_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBox_2)
        # self.checkBox = QtWidgets.QCheckBox(self.widget_2)
        # self.checkBox.setObjectName("checkBox")
        # self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setStyleSheet("QWidget#widget_3{\n"
                                    "    background-color:rgb(20,20,20);\n"
                                    "    border-bottom-left-radius:8px;\n"
                                    "    border-bottom-right-radius:8px;\n"
                                    "}\n"
                                    "QPushButton{\n"
                                    "    background-color:rgba(0,0,0,0);\n"
                                    "    color:rgb(144,144,144);\n"
                                    "    font:bold;\n"
                                    "    font-size:20px;\n"
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
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self._label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self._label.setFont(font)
        self._label.setStyleSheet("color:rgb(144,144,144);\n"
                                  "font:bold;")
        self._label.setText("")
        self._label.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self._label.setObjectName("_label")
        self.horizontalLayout_2.addWidget(self._label)
        self._pushButton = QtWidgets.QPushButton(self.widget_3)
        self._pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self._pushButton.setObjectName("_pushButton")
        self.horizontalLayout_2.addWidget(self._pushButton)
        # self._pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        # self._pushButton_2.setMaximumSize(QtCore.QSize(30, 40))
        # self._pushButton_2.setObjectName("_pushButton_2")
        # self.horizontalLayout_2.addWidget(self._pushButton_2)
        self._label_2 = QtWidgets.QLabel(self.widget_3)
        self._label_2.setText("")
        self._label_2.setObjectName("_label_2")
        self.horizontalLayout_2.addWidget(self._label_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self._label_3.setText(_translate("Dialog", "Settings"))
        self.pushButton_5.setText(_translate("Dialog", "X"))
        # self._label_4.setText(_translate("Dialog", "DISABLE CHANGES TO HOME"))
        self._label_5.setText(_translate("Dialog", "DELETE USERDATA ON EXIT"))
        # self._label_6.setText(_translate("Dialog", "ENABLE LOCKING APPS"))
        # self.checkBox_3.setText(_translate("Dialog", ""))
        self.checkBox_2.setText(_translate("Dialog", ""))
        # self.checkBox.setText(_translate("Dialog", ""))
        self._pushButton.setText(_translate("Dialog", ""))
        # self._pushButton_2.setText(_translate("Dialog", ""))
