from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
import gl 

"""
自定义对话框
"""
class MyCheckBox(QtWidgets.QFrame):
    mySignal = pyqtSignal(str,str)

    def __init__(self, parent = None):
        super(MyCheckBox, self).__init__(parent)
        self.initUI()


    def initUI(self):
        self.setGeometry(0, 0, 100*gl.w, 200*gl.h)
        self.fLayout = QtWidgets.QHBoxLayout()
        self.cb = QtWidgets.QCheckBox()
        self.cb.isChecked()
        self.fLayout.addStretch()
        self.fLayout.addWidget(self.cb)
        self.fLayout.addStretch()
        self.setLayout(self.fLayout)
        self.fLayout.setContentsMargins(5,2,5,2)
        self.state=0
        self.num=-1
        self.cb.clicked.connect(lambda:self.chechkedstate())
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
    
    def chechkedstate(self):
        check_state = self.cb.checkState()
        if check_state == QtCore.Qt.Checked:
            self.state=1
        else:
            self.state=0
        self.mySignal.emit(str(self.state),str(self.num))
    #设置状态
    def Setstate(self,iflg):
        if iflg==0:
            self.cb.setChecked(False)
        else:
            self.cb.setChecked(True)
    #从外部传过来的数目
    def getidfromfather(self,num):
        self.num=num
    
    #返回状态
    def GetChecked(self):
        return self.cb.checkState()
 