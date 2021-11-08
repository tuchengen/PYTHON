# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\HotPile\UI\Ui_PileSelect\Select.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QDialog
from UI.Ui_ProductSelect.Ui_PileSelect import Ui_ReGuanSelect
from UI.Ui_ProductSelect.Ui_PileSelectTable import Ui_PileSelectTable
from UI.Ui_ProductSelect.Ui_Initlogo import Ui_Initlogo
import gl 


class Ui_ProductSelect(QWidget):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(1132*gl.w, 898*gl.h)
        self.gridLayout = QtWidgets.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.ProductSelect = ProductSelect()
        self.ProductSelectTable = ProductSelectTable()
        self.ProductSelect.setMaximumSize(QtCore.QSize(550*gl.w, 16777215*gl.h))
        self.LOGO=Ui_Initlogo()
        self.LOGO.setGeometry(QtCore.QRect(0, 0, 1800*gl.w, 1000*gl.h))
        self.LOGO.show()
        self.gridLayout.addWidget(self.ProductSelect, 0, 0, 1, 1)
        self.gridLayout.addWidget(self.LOGO, 0, 1, 1, 1)
        self.ProductSelect.mySignal.connect(self.getShangxuanSignal)
        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
    
    def getShangxuanSignal(self,connect,icode):
        #从热管选型界面发送过来的消息，需解析区分
        dic=eval(connect)
        #热源数目
        if icode==2:
            self.ProductSelectTable.freshenReRanPic(dic["renrannum"])
        #筛选按钮，用来过滤产品列表
        if icode==1:
            if hasattr(self,"LOGO"):
                self.LOGO.close()
                self.gridLayout.addWidget(self.ProductSelectTable, 0, 1, 1, 1)
            #将筛选信息传递到“液赛查看”
            self.ProductSelectTable.GetParaFromFatherFrom(connect)
            # print(connect)
            pass
        

class ProductSelectTable(QWidget, Ui_PileSelectTable):
    def __init__(self):
        super(ProductSelectTable,self).__init__()
        # 子窗口初始化时实现子窗口布局
        self.setupUi(self)
 
        # 设置子窗体最小尺寸
        self.setMinimumWidth(30*gl.w)
        self.setMinimumHeight(30*gl.h)

class ProductSelect(QWidget, Ui_ReGuanSelect):
    def __init__(self):
        super(ProductSelect,self).__init__()
        # 子窗口初始化时实现子窗口布局
        self.setupUi(self)
 
        # 设置子窗体最小尺寸
        self.setMinimumWidth(30*gl.w)
        self.setMinimumHeight(30*gl.h)


