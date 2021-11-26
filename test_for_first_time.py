import shelve
import pickle
import os
from pathlib import Path
x = False



def check_if_program_opened_before():
    my_file = Path('C:/Users/{}/AppData/Local/Temp/first_file'.format(os.getlogin()))
    if my_file.is_file():
        print("program has opened before")
        from main import obj_1, appnamedict_shelve, applinkdict_shelve, appnamedict, linksdict

        print(list(obj_1.items()))
    else:
        print("program is run first time")
        with open('C:/Users/{}/AppData/Local/Temp/first_file'.format(os.getlogin()), 'wb') as f:
            from main import obj_1, appnamedict_shelve, applinkdict_shelve, appnamedict, linksdict
            pickle.dump("program opened before", f)

            obj_1["DEL USR DATA"] = False
            obj_1.sync()

            for i in appnamedict:
                print("reuploading default data")
                appnamedict_shelve[i] = appnamedict[i]
            for i in linksdict:
                applinkdict_shelve[i] = linksdict[i]



