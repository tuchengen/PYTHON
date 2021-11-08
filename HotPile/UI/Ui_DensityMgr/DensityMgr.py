# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\HotPile\UI\Ui_ProductMgr\Ui_ProductMgr.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QDialog
from Tools import ProductSelect
import os
import xlrd


class Ui_DensityMgr(QWidget):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)
        self.setupUi()
        self.LoadData()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(1800, 1000)
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(890, 20, 191, 31))
        self.label.setStyleSheet("font: 75 16pt \"Agency FB\";")
        self.label.setObjectName("label")
        self.importFileData = QtWidgets.QPushButton(self)
        self.importFileData.setGeometry(QtCore.QRect(20, 60, 75, 23))
        self.importFileData.setObjectName("importFileData")
        self.clearData = QtWidgets.QPushButton(self)
        self.clearData.setGeometry(QtCore.QRect(110, 60, 75, 23))
        self.clearData.setObjectName("clearData")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(50, 110, 1700, 1000))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        self.tableWidget.verticalHeader().setVisible(False)  
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.importFileData.clicked.connect(lambda:self.importFile())
        self.clearData.clicked.connect(lambda:self.clear())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "温度-密度表"))
        self.importFileData.setText(_translate("Form", "导入"))
        self.clearData.setText(_translate("Form", "清空"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "id"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "温度"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "气体密度"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "液体密度"))
  
    
    def LoadData(self):
        self.productlist=ProductSelect.GetDensityInfo()
        self.tableWidget.setRowCount(len(self.productlist))
        for row_number, row_data in enumerate(self.productlist):
            self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_data["id"])))
            self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data["temperature"])))
            self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(row_data["liquiddensity"])))
            self.tableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(row_data["vapordensity"])))
    
    def clear(self):
        ProductSelect.ClearTable("Density")
        self.LoadData()
        pass

    def importFile(self):
        data=[]
        fileName_choose, filetype = QtWidgets.QFileDialog.getOpenFileName(self,  
                                    "选取文件",  
                                    os.getcwd(), # 起始路径 
                                    "All Files (*);;Text Files (*.xlsx)")   # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            return
        if "Density.xlsx"  in fileName_choose:
            self.clear()
        else:
            return
        #打开文件，获取excel文件的workbook（工作簿）对象
        excel = xlrd.open_workbook(fileName_choose,encoding_override="utf-8")
        #获取sheet对象
        sheet = excel.sheets()[0]
        for each_row in range(sheet.nrows):#循环打印每一行
            if each_row==0:
                continue
            item={}
            item["id"]=int(float(sheet.cell(each_row,0).value))
            item["temperature"]=str(sheet.cell(each_row,1).value)
            item["liquiddensity"]=float(sheet.cell(each_row,2).value)
            item["vapordensity"]=float(sheet.cell(each_row,3).value)
            data.append(item)
        ProductSelect.InsertIntoProduct("Density",data)
        self.LoadData()

        


