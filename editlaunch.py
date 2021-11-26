import getpass
import os

import main
import testmod
from editapps import *
from editapps import Ui_Edit_apps
import shelve

appnamedict_shelve = testmod.appnamedict_shelve
applinkdict_shelve = testmod.applinkdict_shelve







class moWidget(QtWidgets.QWidget):
    def __init__(self):
        super(moWidget, self).__init__()

    def mousePressEvent(self, event):
        if event.button() == QtCore.Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == QtCore.Qt.LeftButton:
            self.move(event.globalPos() - self.dragPosition)
            event.accept()


class applet(moWidget, Ui_Edit_apps):
    def __init__(self,link,name,app_name_number,app_link_number):
        super(applet, self).__init__()
        self.setupUi(self)
        print("EDIT CLASS:",link,name,app_name_number,app_link_number)

        self.app_name_number = app_name_number
        self.app_link_number = app_link_number




        self.pushButton_5.clicked.connect(self.close)

        self.__textEdit = QtWidgets.QTextEdit(self.widget_2)
        self.__textEdit.setMaximumSize(QtCore.QSize(200, 25))
        self.__textEdit.setObjectName("__textEdit")
        self.gridLayout.addWidget(self.__textEdit, 0, 1, 1, 1)
        self.__textEdit_2 = QtWidgets.QTextEdit(self.widget_2)
        self.__textEdit_2.setMaximumSize(QtCore.QSize(200, 25))
        self.__textEdit_2.setObjectName("__textEdit_2")
        self.gridLayout.addWidget(self.__textEdit_2, 1, 1, 1, 1)

        self.__textEdit.setText(name)
        self.__textEdit_2.setText(link)

        self.pushButton.clicked.connect(self.get_text)



    def get_text(self):
        print("\nAPPLY_LAUNCH::::::::TESTMOD\n")
        testmod.sync()

        appnamedict_shelve[str(self.app_name_number)] = str(self.__textEdit.toPlainText())
        print(str(self.__textEdit_2.toPlainText()),str(self.__textEdit.toPlainText()),"updated")
        appnamedict_shelve.sync()

        applinkdict_shelve[self.app_link_number] = str(self.__textEdit_2.toPlainText())
        applinkdict_shelve.sync()


        testmod.sync()
        print("\nAPPLY_LAUNCH::::::::TESTMOD\n")

        self.close()






# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = applet()
#     Dialog.show()
#     sys.exit(app.exec_())

