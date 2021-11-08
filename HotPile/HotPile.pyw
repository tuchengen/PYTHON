import sys
import os
import datetime
from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
# from PyQt5 import QtCore
from cryptography.fernet import Fernet
from SysDataBase import Data
import gl


import UI.Ui_Index
import UI.Ui_Error


# print(Data.app_path())
# licence
key=b'GLuQVxaBH_ZJZevNv9_w879VR0cXf9OjMWwTj5sBpZs='
def GetLicence():
    filename=Data.app_path()+"\\licence"
    if os.path.exists(filename):
        pass
    else:
        return b''
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    return f.decrypt(encrypted_data)
    

if __name__ == '__main__':
    flg=1
    byte=GetLicence()
    str=byte.decode('utf-8')
    timeinfo=str.split(',')
    IsGm=0
    # QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    if len(timeinfo)<2:
        flg=-1
    else:
        Authorizationtime=datetime.datetime(int(float(timeinfo[0])), int(float(timeinfo[1])), int(float(timeinfo[2])))
        Activetime=Authorizationtime+datetime.timedelta(hours=int(float(timeinfo[3]))*24)
        deltatime=(Activetime-datetime.datetime.now()).days
        IsGm=int(float(timeinfo[4]))
        if deltatime<0:
            flg=-1
    if flg==-1:
        app = QApplication(sys.argv)
        # font.setPixelSize(pointsize*90/72)
        MainWindow = QMainWindow()
        ui = UI.Ui_Error.Ui_Error()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    else:
        app = QApplication(sys.argv)
        font = QtGui.QFont("宋体")
        pointsize = font.pointSize()
        font.setPixelSize(pointsize*gl.h)
        app.setFont(font)
        MainWindow = QMainWindow()
        ui = UI.Ui_Index.Ui_mainWindow(IsGm)
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
