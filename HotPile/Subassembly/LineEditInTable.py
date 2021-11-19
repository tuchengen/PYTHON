from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
import gl

"""
自定义对输入框
"""

class MyLineEdit(QLineEdit):
    # 自定义信号
    mySignal = pyqtSignal(str)

    def __init__(self, _row, _column,_text, _disabled,parent=None,):
        super(MyLineEdit, self).__init__(parent)
        self.row = _row
        self.column = _column
        self.disabled=_disabled
        self.setText(str(_text))
        self.initUI()
    
    def initUI(self):
        self.setGeometry(0, 0, 100*gl.w, 200*gl.h)
        self.fLayout = QtWidgets.QHBoxLayout()
        self.setStyleSheet("border:none")
        if self.disabled==True:
            self.setFocusPolicy(QtCore.Qt.NoFocus)
            self.setStyleSheet("background-color:rgba(211, 211, 211, 160);border:none")
        self.retranslateUi()
        self.setValidator(QDoubleValidator())
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
    
    #重写失焦事件
    def focusOutEvent(self,event):
        oData={}
        oData["row"]=str(self.row)
        oData["column"]=str(self.column)
        oData["text"]=str(self.text())
        self.mySignal.emit(str(oData))
        self.update()
    
