import getpass
import os

from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import webbrowser

import main
from settings import Ui_SETTINGS
import shelve
import pickle
USERNAME = os.getlogin()
from main import  obj_1
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


class applet(moWidget, Ui_SETTINGS):
    def __init__(self,):
        super(applet, self).__init__()
        self.setupUi(self)
        self.pushButton_5.clicked.connect(self.close)

        try:
            self.fetch_settings("fetching settings")
        except:
            pass

        self.git_redirect = lambda a:self.myprofile(git=True)
        self.portfol_redirect = lambda a: self.myprofile(git=False)


        self._pushButton.clicked.connect(self.git_redirect)
        # self._pushButton_2.clicked.connect(self.portfol_redirect)
        # self.checkBox_3.stateChanged.connect(self.enable_lock_apps)
        self.checkBox_2.stateChanged.connect(self.delete_user_data)
        # self.checkBox.stateChanged.connect(self.disable_changes_to_home)

    # def enable_lock_apps(self,state):
    #     if state == QtCore.Qt.Checked:
    #         print("checked")
    #         obj_1["ENABLE LOCKING APPS"] =  True
    #         obj_1.sync()
    #         print(list(obj_1.items()))
    #         try:
    #             self.fetch_settings("fetching settings")
    #         except:
    #             pass
    #
    #     else:
    #         print("unchecked")
    #         obj_1["ENABLE LOCKING APPS"] = False
    #         obj_1.sync()
    #         print(list(obj_1.items()))
    #         try:
    #             self.fetch_settings("fetching settings")
    #         except:
    #             pass

    def delete_user_data(self,state):
        if state == QtCore.Qt.Checked:
            print("dud_checked")
            obj_1["DEL USR DATA"] = True
            obj_1.sync()
            print(list(obj_1.items()))
            try:
                self.fetch_settings("fetching settings")
            except:
                pass

        else:
            print("dud_unchecked")
            obj_1["DEL USR DATA"] = False
            obj_1.sync()
            print(list(obj_1.items()))
            try:
                self.fetch_settings("fetching settings")
            except:
                pass

    # def disable_changes_to_home(self,state):
    #     if state == QtCore.Qt.Checked:
    #         print("dcth_checked")
    #         obj_1["DISB CHNG HOME"] = True
    #         obj_1.sync()
    #         print(list(obj_1.items()))
    #         try:
    #
    #             self.fetch_settings("fetching settings")
    #         except:
    #             print("lolnoko")
    #             pass
    #     else:
    #         print("dcth_unchecked")
    #         obj_1["DISB CHNG HOME"] = False
    #         obj_1.sync()
    #         print(list(obj_1.items()))
    #         try:
    #             self.fetch_settings("fetching settings")
    #         except:
    #             pass


    def fetch_settings(self,ko):
        print(ko)


        # self.checkBox_3.setChecked(obj_1["ENABLE LOCKING APPS"])
        self.checkBox_2.setChecked(obj_1["DEL USR DATA"])
        # self.checkBox.setChecked(obj_1["DISB CHNG HOME"])


    def myprofile(self,git):
        if git == True:

            return webbrowser.open_new("https://github.com/Suneba")
        if git == False:
            return webbrowser.open_new("https://dverma.netlify.app")





# if __name__ == "__main__":
#     import sys
#
#     app = QtWidgets.QApplication(sys.argv)
#     Dialog = applet()
#     Dialog.show()
#     sys.exit(app.exec_())

