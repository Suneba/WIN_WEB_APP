import os

from PyQt5 import QtCore, QtGui, QtWidgets,QtWebEngine,QtWebEngineWidgets
import pyperclip

import testmod
from appui import Ui_appdialog
import shelve
QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)

print("\nAPPLAUNCH_UP::::::::TESTMOD\n")
testmod.sync()

from main import obj_1
obj_1.sync()




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


class applet(moWidget, Ui_appdialog):
    def __init__(self,link,name):
        super(applet, self).__init__()
        self.setupUi(self)
        print(name,link)



        self.pushButton_4.setCheckable(True)
        self.pushButton_3.clicked.connect(self.showMinimized)
        self.pushButton_4.clicked.connect(self.winShowMaximized)
        self.pushButton_5.clicked.connect(self.closeall)
        self.pushButton_2.clicked.connect(self.geturl)
        self.pushButton_6.clicked.connect(self.webEngineView.back)
        self.pushButton.clicked.connect(self.loadurl)
        self.label_2.setText(QtCore.QCoreApplication.translate("appdialog",name))
        self.url = QtCore.QUrl.fromUserInput(link)



        self.url = QtCore.QUrl.fromUserInput(link)

        if self.url.isValid():
            self.webEngineView.load(self.url)

            if obj_1["DEL USR DATA"] == True:
                self.webEngineView.page().profile().cookieStore().deleteAllCookies()
            else:
                pass





    def winShowMaximized(self):
        if self.pushButton_4.isChecked():
            self.widget.setStyleSheet(
                "QWidget#widget{background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:1 rgba(0, 0, 0, 255));}")
            self.showMaximized()
        else:
            self.showNormal()
            self.widget.setStyleSheet(
                "QWidget#widget{background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));}")

    def loadurl(self):
        if self.url.isValid():
            self.webEngineView.load(self.url)

    def geturl(self):
        x = (str(self.webEngineView.url()))
        pyperclip.copy(x[19:-2])

    def closeall(self):
        print("\nAPPLAUNCH_CLOSE_ALL::::::::::::TESTMOD\n")
        testmod.sync()
        self.webEngineView.close()
        self.close()



    # if __name__ == "__main__":
    #     import sys
    #
    #     app = QtWidgets.QApplication(sys.argv)
    #     Dialog = applet()
    #     Dialog.show()
    #     sys.exit(app.exec_())



