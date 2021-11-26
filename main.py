import os
import webbrowser
from shelve import DbfilenameShelf

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
import sys

import testmod
from baseui import Ui_Dialog
import applaunch1
import editlaunch

import pickle
import shelve

default_appname_dict = shelve.open('C:/Users/{}/AppData/Local/Temp/def_app_name_dict'.format(os.getlogin()),writeback=True)
default_applink_dict = shelve.open('C:/Users/{}/AppData/Local/Temp/def_app_link_dict'.format(os.getlogin()),writeback=True)

appnamedict_shelve = testmod.appnamedict_shelve
applinkdict_shelve = testmod.applinkdict_shelve

obj_1 = shelve.open('C:/Users/{}/AppData/Local/Temp/obj_1'.format(os.getlogin()),writeback=True)

# testmod.sync()

appnamedict = {
    "appname1": "Youtube",
    "appname2": "Twitter",
    "appname3": "Inverse",
    "appname4": "Github",
    "appname5": "StackOF",
    "appname6": "Digitalocean",
    "appname7": "Gmail",
    "appname8": "Drive",
    "appname9": "Meet",
    "appname10": "Classroom",
    "appname11": "Cloud.G",
    "appname12": "AWS"}

linksdict = {
    "applink1": "https://youtube.com",
    "applink2": "https://twitter.com",
    "applink3": "https://inverse.com",
    "applink4": "https://github.com",
    "applink5": "https://stackoverflow.com",
    "applink6": "https://Digitalocean.com",
    "applink7": "https://gmail.com",
    "applink8": "https://drive.google.com",
    "applink9": "https://meet.google.com",
    "applink10": "https://classroom.google.com",
    "applink11": "https://cloud.google.com",
    "applink12": "https://aws.amazon.com",

}

from test_for_first_time import check_if_program_opened_before

check_if_program_opened_before()



# for i in appnamedict:
#     print("reuploading default data")
#     appnamedict_shelve[i] = appnamedict[i]
# for i in linksdict:
#     applinkdict_shelve[i] = linksdict[i]






# print(list(appnamedict_shelve.items()))
# print(list(applinkdict_shelve.items()))

class openapp():


    def start(self, link, name):
        print("\nopening",name,"-->" ,link,"\n")

        print("\nSTART_APP:::::::::TESTMOD\n")
        testmod.sync()

        self.hsfs_2 = QtWidgets.QMainWindow()
        self.djdu_2 = applaunch1.applet(str(link),str(name))
        self.djdu_2.show()

class edit_app():

    def start(self,link,name,app_name_number,app_link_number):
        print("\nEDIT CLASS:::::::TESTMOD\n")
        testmod.sync()

        # print(app_link_number,link,app_name_number,name)
        self.hsfs_2 = QtWidgets.QMainWindow()
        self.djdu_2 = editlaunch.applet(str(link),str(name),str(app_name_number),str(app_link_number))
        self.djdu_2.show()

class opensettings():

    def start(self):
        print("opening settings")
        obj_1.sync()
        print(list(obj_1.items()))
        app_sett = QtWidgets.QMainWindow()
        from settlaunch import applet as sett_applet
        sett = sett_applet()
        sett.show()

settlaunchaobject = opensettings()
settlaunchaobject_lambda = lambda:settlaunchaobject.start()

app1 = openapp()
app2 = openapp()
app3 = openapp()
app4 = openapp()
app5 = openapp()
app6 = openapp()
app7 = openapp()
app8 = openapp()
app9 = openapp()
app10 = openapp()
app11 = openapp()
app12 = openapp()

edit_app1 = edit_app()
edit_app2 = edit_app()
edit_app3 = edit_app()
edit_app4 = edit_app()
edit_app5 = edit_app()
edit_app6 = edit_app()
edit_app7 = edit_app()
edit_app8 = edit_app()
edit_app9 = edit_app()
edit_app10 = edit_app()
edit_app11 = edit_app()
edit_app12 = edit_app()







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


class applet(moWidget, Ui_Dialog):
    def __init__(self):
        super(applet, self).__init__()

        self.setupUi(self)
        self.pushButton_4.setCheckable(True)
        self.pushButton_3.clicked.connect(self.showMinimized)
        self.pushButton_4.clicked.connect(self.winShowMaximized)
        self.pushButton_5.clicked.connect(self.exitall)
        self.pushButton.clicked.connect(settlaunchaobject_lambda)


        _translate = QtCore.QCoreApplication.translate
        self.pushButton_7.setText(_translate("Dialog", appnamedict_shelve["appname1"]))
        self.pushButton_6.setText(_translate("Dialog", appnamedict_shelve["appname2"]))
        self.pushButton_8.setText(_translate("Dialog", appnamedict_shelve["appname3"]))
        self.pushButton_13.setText(_translate("Dialog", appnamedict_shelve["appname4"]))
        self.pushButton_14.setText(_translate("Dialog", appnamedict_shelve["appname5"]))
        self.pushButton_15.setText(_translate("Dialog", appnamedict_shelve["appname6"]))
        self.pushButton_10.setText(_translate("Dialog", appnamedict_shelve["appname7"]))
        self.pushButton_9.setText(_translate("Dialog", appnamedict_shelve["appname8"]))
        self.pushButton_11.setText(_translate("Dialog", appnamedict_shelve["appname9"]))
        self.pushButton_12.setText(_translate("Dialog", appnamedict_shelve["appname10"]))
        self.pushButton_16.setText(_translate("Dialog", appnamedict_shelve["appname11"]))
        self.pushButton_17.setText(_translate("Dialog", appnamedict_shelve["appname12"]))



        self.pushButton_7.clicked.connect(self.open_app1_with_link1)
        self.pushButton_6.clicked.connect(self.open_app2_with_link2)
        self.pushButton_8.clicked.connect(self.open_app3_with_link3)
        self.pushButton_13.clicked.connect(self.open_app4_with_link4)
        self.pushButton_14.clicked.connect(self.open_app5_with_link5)
        self.pushButton_15.clicked.connect(self.open_app6_with_link6)
        self.pushButton_10.clicked.connect(self.open_app7_with_link7)
        self.pushButton_9.clicked.connect(self.open_app8_with_link8)
        self.pushButton_11.clicked.connect(self.open_app9_with_link9)
        self.pushButton_12.clicked.connect(self.open_app10_with_link10)
        self.pushButton_16.clicked.connect(self.open_app11_with_link11)
        self.pushButton_17.clicked.connect(self.open_app12_with_link12)

        self.pushButton_2.setCheckable(True)
        self.pushButton_2.clicked.connect(self.start_blinking)



    def edit_the_app1(self):
        testmod.sync()
        x, y = testmod.initialise(appnumber=1)
        print(x,y)
        edit_app1.start(x,y, "appname1","applink1")
        self.pushButton_7.setText(QtCore.QCoreApplication.translate("Dialog", str(y)))
    def edit_the_app2(self):
        testmod.sync()
        x, y = testmod.initialise(appnumber=2)
        print(x, y)
        edit_app2.start(x, y, "appname2", "applink2")
    def edit_the_app3(self):
        testmod.sync()
        x, y = testmod.initialise(appnumber=3)
        print(x, y)
        edit_app3.start(x, y, "appname3", "applink3")
    def edit_the_app4(self):
        testmod.sync()
        x, y = testmod.initialise(appnumber=4)
        print(x, y)
        edit_app4.start(x, y, "appname4", "applink4")
    def edit_the_app5(self):
        testmod.sync()
        x, y = testmod.initialise(appnumber=5)
        print(x, y)
        edit_app5.start(x, y, "appname5", "applink5")
    def edit_the_app6(self):
        testmod.sync()
        x, y = testmod.initialise(appnumber=6)
        print(x, y)
        edit_app6.start(x, y, "appname6", "applink6")
    def edit_the_app7(self):
        testmod.sync()
        x, y = testmod.initialise(appnumber=7)
        print(x, y)
        edit_app7.start(x, y, "appname7", "applink7")
    def edit_the_app8(self):
        testmod.sync()
        x, y = testmod.initialise(appnumber=8)
        print(x, y)
        edit_app8.start(x, y, "appname8", "applink8")
    def edit_the_app9(self):
        testmod.sync()
        x, y = testmod.initialise(appnumber=9)
        print(x, y)
        edit_app9.start(x, y, "appname9", "applink9")
    def edit_the_app10(self):
        testmod.sync()
        x, y = testmod.initialise(appnumber=10)
        print(x, y)
        edit_app10.start(x, y, "appname10", "applink10")
    def edit_the_app11(self):
        testmod.sync()
        x, y = testmod.initialise(appnumber=11)
        print(x, y)
        edit_app11.start(x, y, "appname11", "applink11")
    def edit_the_app12(self):
        testmod.sync()
        x, y = testmod.initialise(appnumber=12)
        print(x, y)
        edit_app12.start(x, y, "appname12", "applink12")

    def open_app1_with_link1(self):
        # applinkdict_shelve["applink1"] = "google.com"
        testmod.sync()
        x, y = testmod.initialise(appnumber=1)
        print(x,y)
        app1.start(x, y)

    def open_app2_with_link2(self):
        # applinkdict_shelve["applink2"] = "google.com"
        testmod.sync()
        x, y = testmod.initialise(appnumber=2)
        print(x, y)
        app2.start(x, y)

    def open_app3_with_link3(self):
        # applinkdict_shelve["applink3"] = "google.com"
        testmod.sync()
        x, y = testmod.initialise(appnumber=3)
        print(x, y)
        app3.start(x, y)

    def open_app4_with_link4(self):
        # applinkdict_shelve["applink4"] = "google.com"
        testmod.sync()
        appnamedict_shelve.sync()
        x, y = testmod.initialise(appnumber=4)
        print(x, y)
        app4.start(x, y)

    def open_app5_with_link5(self):
        # applinkdict_shelve["applink5"] = "google.com"
        testmod.sync()
        appnamedict_shelve.sync()
        x, y = testmod.initialise(appnumber=5)
        print(x, y)
        app5.start(x, y)

    def open_app6_with_link6(self):
        # applinkdict_shelve["applink6"] = "google.com"
        testmod.sync()
        appnamedict_shelve.sync()
        x, y = testmod.initialise(appnumber=6)
        app6.start(x, y)

    def open_app7_with_link7(self):
        # applinkdict_shelve["applink7"] = "google.com"
        testmod.sync()
        appnamedict_shelve.sync()
        x, y = testmod.initialise(appnumber=7)
        print(x, y)
        app7.start(x, y)

    def open_app8_with_link8(self):
        # applinkdict_shelve["applink8"] = "google.com"
        testmod.sync()
        appnamedict_shelve.sync()
        x, y = testmod.initialise(appnumber=8)
        print(x, y)
        app8.start(x, y)

    def open_app9_with_link9(self):
        # applinkdict_shelve["applink9"] = "google.com"
        testmod.sync()
        appnamedict_shelve.sync()
        x, y = testmod.initialise(appnumber=9)
        print(x, y)
        app9.start(x, y)

    def open_app10_with_link10(self):
        # applinkdict_shelve["applink10"] = "google.com"
        testmod.sync()
        appnamedict_shelve.sync()
        x, y = testmod.initialise(appnumber=10)
        print(x, y)
        app10.start(x, y)

    def open_app11_with_link11(self):
        # applinkdict_shelve["applink11"] = "google.com"
        testmod.sync()
        appnamedict_shelve.sync()
        x, y = testmod.initialise(appnumber=11)
        print(x, y)
        app11.start(x, y)

    def open_app12_with_link12(self):
        # applinkdict_shelve["applink12"] = "google.com"
        testmod.sync()
        appnamedict_shelve.sync()
        x, y = testmod.initialise(appnumber=12)
        print(x, y)
        app12.start(x, y)

    def update_name_on_apps(self):
        testmod.sync()
        _translate = QtCore.QCoreApplication.translate
        self.pushButton_7.setText(_translate("Dialog", appnamedict_shelve["appname1"]))
        self.pushButton_6.setText(_translate("Dialog", appnamedict_shelve["appname2"]))
        self.pushButton_8.setText(_translate("Dialog", appnamedict_shelve["appname3"]))
        self.pushButton_13.setText(_translate("Dialog", appnamedict_shelve["appname4"]))
        self.pushButton_14.setText(_translate("Dialog", appnamedict_shelve["appname5"]))
        self.pushButton_15.setText(_translate("Dialog", appnamedict_shelve["appname6"]))
        self.pushButton_10.setText(_translate("Dialog", appnamedict_shelve["appname7"]))
        self.pushButton_9.setText(_translate("Dialog", appnamedict_shelve["appname8"]))
        self.pushButton_11.setText(_translate("Dialog", appnamedict_shelve["appname9"]))
        self.pushButton_12.setText(_translate("Dialog", appnamedict_shelve["appname10"]))
        self.pushButton_16.setText(_translate("Dialog", appnamedict_shelve["appname11"]))
        self.pushButton_17.setText(_translate("Dialog", appnamedict_shelve["appname12"]))





    def winShowMaximized(self):
        if self.pushButton_4.isChecked():
            self.widget.setStyleSheet(
                "QWidget#widget{background-color: qlineargradient(spread:pad, x1:1, y1:0, x2:0, y2:1, stop:1 rgba(0, 0, 0, 255));}")
            self.showMaximized()
        else:
            self.showNormal()
            self.widget.setStyleSheet(
                "QWidget#widget{background-color: qradialgradient(spread:pad, cx:0.5, cy:0.5, radius:0.5, fx:0.5, fy:0.5, stop:0 rgba(255, 235, 235, 206), stop:0.35 rgba(255, 188, 188, 80), stop:0.4 rgba(255, 162, 162, 80), stop:0.425 rgba(255, 132, 132, 156), stop:0.44 rgba(252, 128, 128, 80), stop:1 rgba(255, 255, 255, 0));}")

    ######################################### edit mode blinking ##################################
    def start_blinking(self):
        print("\nSTART BLINKING::::::::::TESTMOD\n")
        testmod.sync()
        obj_1.sync()


        print(list(obj_1.items()))
        if self.pushButton_2.isChecked():

            if self.pushButton_2.isChecked():
                self.pushButton_2.setText(QtCore.QCoreApplication.translate("Dialog", "X"))
                self.flag = True
                self.timer = QTimer(self, interval=1000)
                self.timer.timeout.connect(self.change_apply)
                self.timer.start()

                self.pushButton_7.disconnect()
                self.pushButton_6.disconnect()
                self.pushButton_8.disconnect()
                self.pushButton_13.disconnect()
                self.pushButton_14.disconnect()
                self.pushButton_15.disconnect()
                self.pushButton_10.disconnect()
                self.pushButton_9.disconnect()
                self.pushButton_11.disconnect()
                self.pushButton_12.disconnect()
                self.pushButton_16.disconnect()
                self.pushButton_17.disconnect()

                self.pushButton_7.clicked.connect(self.edit_the_app1)
                self.pushButton_6.clicked.connect(self.edit_the_app2)
                self.pushButton_8.clicked.connect(self.edit_the_app3)
                self.pushButton_13.clicked.connect(self.edit_the_app4)
                self.pushButton_14.clicked.connect(self.edit_the_app5)
                self.pushButton_15.clicked.connect(self.edit_the_app6)
                self.pushButton_10.clicked.connect(self.edit_the_app7)
                self.pushButton_9.clicked.connect(self.edit_the_app8)
                self.pushButton_11.clicked.connect(self.edit_the_app9)
                self.pushButton_12.clicked.connect(self.edit_the_app10)
                self.pushButton_16.clicked.connect(self.edit_the_app11)
                self.pushButton_17.clicked.connect(self.edit_the_app12)
        else:
            print("\nSTART BLINKING(F)::::::::::TESTMOD\n")
            testmod.sync()
            print("timer started")
            self.timer.stop()
            self.pushButton_2.setText(QtCore.QCoreApplication.translate("Dialog", "✎"))

            self.pushButton_7.disconnect()
            self.pushButton_6.disconnect()
            self.pushButton_8.disconnect()
            self.pushButton_13.disconnect()
            self.pushButton_14.disconnect()
            self.pushButton_15.disconnect()
            self.pushButton_10.disconnect()
            self.pushButton_9.disconnect()
            self.pushButton_11.disconnect()
            self.pushButton_12.disconnect()
            self.pushButton_16.disconnect()
            self.pushButton_17.disconnect()

            self.pushButton_7.clicked.connect(self.open_app1_with_link1)
            self.pushButton_6.clicked.connect(self.open_app2_with_link2)
            self.pushButton_8.clicked.connect(self.open_app3_with_link3)
            self.pushButton_13.clicked.connect(self.open_app4_with_link4)
            self.pushButton_14.clicked.connect(self.open_app5_with_link5)
            self.pushButton_15.clicked.connect(self.open_app6_with_link6)
            self.pushButton_10.clicked.connect(self.open_app7_with_link7)
            self.pushButton_9.clicked.connect(self.open_app8_with_link8)
            self.pushButton_11.clicked.connect(self.open_app9_with_link9)
            self.pushButton_12.clicked.connect(self.open_app10_with_link10)
            self.pushButton_16.clicked.connect(self.open_app11_with_link11)
            self.pushButton_17.clicked.connect(self.open_app12_with_link12)

    def change_apply(self):

        if self.flag:
            self.widget_2.setStyleSheet(
                "QWidget#widget_2{\n""    background-color:rgb(20,20,20);\n""    \n""}\n""QPushButton{\n""    background-color:rgba(200,0,0,0);\n""    color:rgb(144,144,144);\n""    font:bold;\n""    font-size:15px;\n""    font-family:entypo;\n""}\n""QPushButton:hover{\n""    color:rgb(142,176,27);\n""}\n""QPushButton:pressed{\n""    padding-top:5px;\n""    pading-left:5px;\n""    color:rgb(91,88,53);\n""}")

        else:
            self.widget_2.setStyleSheet(
                "QWidget#widget_2{\n""    background-color:rgb(20,20,20);\n""    \n""}\n""QPushButton{\n""    background-color:rgba(0,0,0,0);\n""    color:rgb(144,144,144);\n""    font:bold;\n""    font-size:15px;\n""    font-family:entypo;\n""border :1px solid ;\n""                     border-top-color : grey; \n""                     border-left-color :grey;\n""                     border-right-color :grey;\n""                     border-bottom-color : grey;\n""border-bottom-left-radius:10px;\n""    border-bottom-right-radius:10px;\n""border-top-left-radius:10px;\n""    border-top-right-radius:10px;\n""}\n""QPushButton:hover{\n""    color:rgb(142,176,27);\n""                    \n""\n""}\n""QPushButton:pressed{\n""    padding-top:5px;\n""    pading-left:5px;\n""    color:rgb(91,88,53);\n""}")

        self.flag = not self.flag

    def exitall(self):
        sys.exit()


#################################################################################################################
if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Dialog = applet()
    Dialog.show()
    sys.exit(app.exec_())
