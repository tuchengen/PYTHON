from PyQt5.QtWidgets import QApplication, QWidget, QDialog, QPushButton, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtGui, QtWidgets
"""
自定义对话框
"""
class MyDialog(QDialog):

    # 自定义信号
    mySignal = pyqtSignal(str)

    def __init__(self, parent = None):
        super(MyDialog, self).__init__(parent)
        self.initUI()


    def initUI(self):
        self.setGeometry(1200, 100, 400, 300)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(20, 30, 100, 20))
        self.label.setObjectName("label")
        self.tempup = QtWidgets.QLineEdit(self)
        self.tempup.setGeometry(QtCore.QRect(120, 30, 100, 20))
        self.tempup.setObjectName("tempup")
        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(230, 30, 20, 20))
        self.label_2.setObjectName("label_2")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(230, 70, 20, 20))
        self.label_5.setObjectName("label_5")
        self.tempdn = QtWidgets.QLineEdit(self)
        self.tempdn.setGeometry(QtCore.QRect(120, 70, 100, 20))
        self.tempdn.setObjectName("tempdn")
        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(20, 70, 100, 20))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(20, 110, 100, 20))
        self.label_7.setObjectName("label_7")
        self.iempjiange = QtWidgets.QLineEdit(self)
        self.iempjiange.setGeometry(QtCore.QRect(120, 110, 100, 20))
        self.iempjiange.setObjectName("iempjiange")
        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(230, 110, 20, 20))
        self.label_8.setObjectName("label_8")
        self.confirm = QtWidgets.QPushButton(self)
        self.confirm.setGeometry(QtCore.QRect(190, 190, 75, 23))
        self.confirm.setObjectName("confirm")
        self.cancle = QtWidgets.QPushButton(self)
        self.cancle.setGeometry(QtCore.QRect(290, 190, 75, 23))
        self.cancle.setObjectName("cancle")
        self.confirm.clicked.connect(lambda:self.confirmfun(self))
        self.cancle.clicked.connect(lambda:self.close())
        #原设计的充装温度用控制信息中额定温度替换
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(230, 70, 20, 20))
        self.label_3.setObjectName("label_3")
        self.label_3.hide()
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(20, 70, 100, 20))
        self.label_4.setObjectName("label_4")
        self.label_4.hide()
        self.tempeding = QtWidgets.QLineEdit(self)
        self.tempeding.setGeometry(QtCore.QRect(120, 70, 100, 20))
        self.tempeding.setObjectName("tempeding")
        self.tempeding.hide()
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)
    
    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "设置"))
        self.label.setText(_translate("self", "充装温度上限："))
        self.tempup.setText(_translate("self", "10"))
        self.label_2.setText(_translate("self", "℃"))
        self.label_3.setText(_translate("self", "℃"))
        self.label_4.setText(_translate("self", "额定充装温度："))
        self.tempeding.setText(_translate("self", "0"))
        self.label_5.setText(_translate("self", "℃"))
        self.tempdn.setText(_translate("self", "-10"))
        self.label_6.setText(_translate("self", "充装温度下限："))
        self.label_7.setText(_translate("self", "温度间隔："))
        self.iempjiange.setText(_translate("self", "5"))
        self.label_8.setText(_translate("self", "℃"))
        self.confirm.setText(_translate("self", "确定"))
        self.cancle.setText(_translate("self", "取消"))
    
    def SetProductID(self,productid):
        self.productid=productid
    
    #当前充装温度用的是控制参数的额定温度
    def SetChongZhuangTemp(self,tempeding):
        self.tempeding.setText(str(tempeding))
        self.tempup.setText(str(float(tempeding)+10.0))
        self.tempdn.setText(str(float(tempeding)-10.0))

    def confirmfun(self,_Dialog):
        oData={}
        oData["tempup"]=str(self.tempup.text())
        oData["tempeding"]=str(self.tempeding.text())
        oData["tempdn"]=str(self.tempdn.text())
        oData["iempjiange"]=str(self.iempjiange.text())
        oData["productid"]=str(self.productid)
        self.mySignal.emit(str(oData))
        _Dialog.close()
