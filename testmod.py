import shelve
import os

applinkdict_shelve = shelve.open('C:/Users/{}/AppData/Local/Temp/fshelve_2'.format(os.getlogin()), writeback=True)
appnamedict_shelve = shelve.open('C:/Users/{}/AppData/Local/Temp/fshelve'.format(os.getlogin()), writeback=True)
def assign_appnamedict_shelve():
    return shelve.open('C:/Users/{}/AppData/Local/Temp/fshelve'.format(os.getlogin()), writeback=True)
def assign_applinkdict_shelve():
    return shelve.open('C:/Users/{}/AppData/Local/Temp/fshelve_2'.format(os.getlogin()), writeback=True)

def initialise(appnumber):

    y = "appname{}".format(appnumber)
    x = "applink{}".format(appnumber)




    # print(list(applinkdict_shelve.items()))
    # print(list(appnamedict_shelve.items()))


    return applinkdict_shelve[x],appnamedict_shelve[y]

def sync():
    shelve.open('C:/Users/{}/AppData/Local/Temp/fshelve_2'.format(os.getlogin()), writeback=True).sync()
    shelve.open('C:/Users/{}/AppData/Local/Temp/fshelve'.format(os.getlogin()), writeback=True).sync()
    print(list(shelve.open('C:/Users/{}/AppData/Local/Temp/fshelve_2'.format(os.getlogin()), writeback=True).items()))
    print(list(shelve.open('C:/Users/{}/AppData/Local/Temp/fshelve'.format(os.getlogin()), writeback=True).items()))