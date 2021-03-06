

from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(1112, 608)
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
        self.widget_4.setStyleSheet("QWidget#widget_4{\n""    background-color:rgb(20,20,20);\n"" border-top-left-radius:8px;\n""    border-top-right-radius:8px;\n""}\n""QPushButton{\n""    background-color:rgba(0,0,0,0);\n""    color:rgb(144,144,144);\n""    font:bold;\n""    font-size:15px;\n""    font-family:entypo;\n""}\n""QPushButton:hover{\n""    color:rgb(142,176,27);\n""}\n""QPushButton:pressed{\n""    padding-top:5px;\n""    pading-left:5px;\n""    color:rgb(91,88,53);\n""}")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.widget_4)
        self.label_3.setStyleSheet("color:rgb(144,144,144);")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.pushButton_3 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_4.setMinimumSize(QtCore.QSize(30, 0))
        self.pushButton_4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.widget_4)
        self.pushButton_5.setMinimumSize(QtCore.QSize(10, 0))
        self.pushButton_5.setMaximumSize(QtCore.QSize(30, 16777215))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.verticalLayout_2.addWidget(self.widget_4)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_2.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.widget_2.setStyleSheet("QWidget#widget_2{\n""    background-color:rgb(20,20,20);\n""    \n""}\n""QPushButton{\n""    background-color:rgba(0,0,0,0);\n""    color:rgb(144,144,144);\n""    font:bold;\n""    font-size:15px;\n""    font-family:entypo;\n""border :3px solid ;\n""                     border-top-color : grey; \n""                     border-left-color :grey;\n""                     border-right-color :grey;\n""                     border-bottom-color : grey;\n""border-bottom-left-radius:10px;\n""    border-bottom-right-radius:10px;\n""border-top-left-radius:10px;\n""    border-top-right-radius:10px;\n""}\n""QPushButton:hover{\n""    color:rgb(142,176,27);\n""                    \n""\n""}\n""QPushButton:pressed{\n""    padding-top:5px;\n""    pading-left:5px;\n""    color:rgb(91,88,53);\n""}")

        self.widget_2.setObjectName("widget_2")
        self.gridLayout = QtWidgets.QGridLayout(self.widget_2)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_7.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_7.setStyleSheet("color:rgb(255,0,0);\n""")
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 0, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_6.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_6.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_6.setStyleSheet("color:rgb(29,161,242);")
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_8.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_8.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_8.setObjectName("pushButton_8")
        self.gridLayout.addWidget(self.pushButton_8, 0, 2, 1, 1)
        self.pushButton_13 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_13.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_13.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_13.setObjectName("pushButton_13")
        self.gridLayout.addWidget(self.pushButton_13, 0, 3, 1, 1)
        self.pushButton_14 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_14.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_14.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_14.setObjectName("pushButton_14")
        self.gridLayout.addWidget(self.pushButton_14, 0, 4, 1, 1)
        self.pushButton_15 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_15.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_15.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_15.setObjectName("pushButton_15")
        self.gridLayout.addWidget(self.pushButton_15, 0, 5, 1, 1)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_10.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_10.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_10.setObjectName("pushButton_10")
        self.gridLayout.addWidget(self.pushButton_10, 1, 0, 1, 1)
        self.pushButton_9 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_9.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_9.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_9.setObjectName("pushButton_9")
        self.gridLayout.addWidget(self.pushButton_9, 1, 1, 1, 1)
        self.pushButton_11 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_11.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_11.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_11.setObjectName("pushButton_11")
        self.gridLayout.addWidget(self.pushButton_11, 1, 2, 1, 1)
        self.pushButton_12 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_12.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_12.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_12.setObjectName("pushButton_12")
        self.gridLayout.addWidget(self.pushButton_12, 1, 3, 1, 1)
        self.pushButton_16 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_16.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_16.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_16.setObjectName("pushButton_16")
        self.gridLayout.addWidget(self.pushButton_16, 1, 4, 1, 1)
        self.pushButton_17 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_17.setMinimumSize(QtCore.QSize(100, 100))
        self.pushButton_17.setMaximumSize(QtCore.QSize(100, 100))
        self.pushButton_17.setObjectName("pushButton_17")
        self.gridLayout.addWidget(self.pushButton_17, 1, 5, 1, 1)
        self.verticalLayout_2.addWidget(self.widget_2)
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.widget_3.setStyleSheet("QWidget#widget_3{\n""    background-color:rgb(20,20,20);\n""    border-bottom-left-radius:8px;\n""    border-bottom-right-radius:8px;\n""}\n""QPushButton{\n""    background-color:rgba(0,0,0,0);\n""    color:rgb(144,144,144);\n""    font:bold;\n""    font-size:15px;\n""    font-family:entypo;\n""}\n""QPushButton:hover{\n""    color:rgb(142,176,27);\n""}\n""QPushButton:pressed{\n""    padding-top:5px;\n""    pading-left:5px;\n""    color:rgb(91,88,53);\n""}")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color:rgb(144,144,144);\n""font:bold;")
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.pushButton = QtWidgets.QPushButton(self.widget_3)
        self.pushButton.setMaximumSize(QtCore.QSize(30, 30))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.widget_3)
        self.pushButton_2.setMaximumSize(QtCore.QSize(30, 40))
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_2.addWidget(self.pushButton_2)
        self.label_2 = QtWidgets.QLabel(self.widget_3)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.verticalLayout_2.addWidget(self.widget_3)
        self.verticalLayout.addWidget(self.widget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Home"))
        self.label_3.setText(_translate("Dialog", "BETA 1.21.11"))
        self.pushButton_3.setText(_translate("Dialog", "-"))
        self.pushButton_4.setText(_translate("Dialog", "???"))
        self.pushButton_5.setText(_translate("Dialog", "X"))
        self.pushButton_7.setText(_translate("Dialog", "YouTube"))
        self.pushButton_6.setText(_translate("Dialog", "Twitter"))
        self.pushButton_8.setText(_translate("Dialog", "Inverse"))
        self.pushButton_13.setText(_translate("Dialog", "Github"))
        self.pushButton_14.setText(_translate("Dialog", "StackOF"))
        self.pushButton_15.setText(_translate("Dialog", "DigiOcean"))
        self.pushButton_10.setText(_translate("Dialog", "Gmail"))
        self.pushButton_9.setText(_translate("Dialog", "Drive"))
        self.pushButton_11.setText(_translate("Dialog", "Meet"))
        self.pushButton_12.setText(_translate("Dialog", "Classroom"))
        self.pushButton_16.setText(_translate("Dialog", "GCloud"))
        self.pushButton_17.setText(_translate("Dialog", "AWS"))
        self.label.setText(_translate("Dialog", "     "))
        self.pushButton.setText(_translate("Dialog", "???"))
        self.pushButton_2.setText(_translate("Dialog", "???"))
        self.label_2.setText(_translate("Dialog", " "))
