# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\HotPile\UI\Ui_PileSelect\Select.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QDialog
from Tools import ProductSelect
import xlsxwriter as xw
import os

class Ui_ProductCheck(QWidget):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)
        self.setupUi()
        self.InitData()

    def setupUi(self):
        self.setObjectName("Form")
        self.resize(447, 893)
        self.taleinfo=[]
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(21, 43, 80, 16))
        self.label.setObjectName("label")
        self.name = QtWidgets.QLineEdit(self)
        self.name.setGeometry(QtCore.QRect(120, 81, 150, 20))
        self.name.setObjectName("name")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(21, 81, 80, 16))
        self.label_4.setObjectName("label_4")
        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(120, 40, 150, 20))
        self.comboBox.setObjectName("comboBox")
        self.realL = QtWidgets.QLineEdit(self)
        self.realL.setGeometry(QtCore.QRect(120, 119, 150, 20))
        self.realL.setObjectName("realL")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(21, 119, 80, 16))
        self.label_3.setObjectName("label_3")
        self.realQ = QtWidgets.QLineEdit(self)
        self.realQ.setGeometry(QtCore.QRect(120, 157, 150, 20))
        self.realQ.setText("")
        self.realQ.setObjectName("realQ")
        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(21, 157, 80, 16))
        self.label_7.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_7.setObjectName("label_7")
        self.tempdn = QtWidgets.QLineEdit(self)
        self.tempdn.setGeometry(QtCore.QRect(120, 195, 150, 20))
        self.tempdn.setText("")
        self.tempdn.setObjectName("tempdn")
        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(21, 195, 80, 16))
        self.label_9.setObjectName("label_9")
        self.tempeding = QtWidgets.QLineEdit(self)
        self.tempeding.setGeometry(QtCore.QRect(120, 233, 150, 20))
        self.tempeding.setText("")
        self.tempeding.setObjectName("tempeding")
        self.label_11 = QtWidgets.QLabel(self)
        self.label_11.setGeometry(QtCore.QRect(21, 233, 80, 16))
        self.label_11.setObjectName("label_11")
        self.tempeup = QtWidgets.QLineEdit(self)
        self.tempeup.setGeometry(QtCore.QRect(120, 271, 150, 20))
        self.tempeup.setText("")
        self.tempeup.setObjectName("tempeup")
        self.label_13 = QtWidgets.QLabel(self)
        self.label_13.setGeometry(QtCore.QRect(21, 271, 80, 16))
        self.label_13.setObjectName("label_13")
        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(90, 330, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setGeometry(QtCore.QRect(300, 50, 1500, 800))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)  
        self.tableWidget.setColumnCount(10)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, item)
        self.tableWidget.setObjectName("tableWidget")
        self.ExportButton = QtWidgets.QPushButton(self)
        self.ExportButton.setGeometry(QtCore.QRect(300, 900, 75, 23))
        self.ExportButton.setObjectName("ExportButton")
        self.pushButton.clicked.connect(lambda:self.clickpushButton())
        self.ExportButton.clicked.connect(lambda:self.clickExportButton())

        self.retranslateUi()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "热管管型："))
        self.label_4.setText(_translate("Form", "热管名称："))
        self.label_3.setText(_translate("Form", "实际长度："))
        self.label_7.setText(_translate("Form", "实际充装量："))
        self.label_9.setText(_translate("Form", "低温工况温度："))
        self.label_11.setText(_translate("Form", "额定工作温度："))
        self.label_13.setText(_translate("Form", "高温工作温度："))
        self.pushButton.setText(_translate("Form", "添加并计算"))
        self.ExportButton.setText(_translate("Form", "导出数据"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "序号"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "热管管型"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "热管名称"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "低温工况温度"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Form", "低温液塞长度"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("Form", "高温工况温度"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("Form", "高温液塞长度"))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("Form", "额定工况温度"))
        item = self.tableWidget.horizontalHeaderItem(8)
        item.setText(_translate("Form", "额定液赛长度"))
        item = self.tableWidget.horizontalHeaderItem(9)
        item.setText(_translate("Form", "删除"))
    
    def InitData(self):
        Productlist=ProductSelect.GetProductInfo()
        for i in range(len(Productlist)):
            self.comboBox.addItem("")
            self.comboBox.setItemText(i, Productlist[i]["code"])
        self.name.setText("热管名称1")
        self.realL.setText("0")#实际长度
        self.realQ.setText("0")#实际充装量
        self.tempdn.setText("10")#低温温度
        self.tempeding.setText("20")#额定温度
        self.tempeup.setText("30")#高问温度
    
    def clickpushButton(self):
        oPara=self.CalPara()
        res=ProductSelect.GetCheckData(oPara)
        self.taleinfo.append(res)
        self.RefreashTable()

    def clickExportButton(self):
        fileName_choose, filetype = QtWidgets.QFileDialog.getSaveFileName(self,  
                                    "选取文件",  
                                    os.getcwd(), # 起始路径 
                                    "All Files (*);;Text Files (*.xlsx)")   # 设置文件扩展名过滤,用双分号间隔

        if fileName_choose == "":
            return
        workbook = xw.Workbook(fileName_choose)
        worksheet1 = workbook.add_worksheet("sheet1")
        worksheet1.activate()
        title=["序号","热管管型","热管名称","低温工况温度","低温液赛长度","高温工况温度","高温液赛长度","额定工况温度","额定液赛长度"]
        worksheet1.write_row("A1", title)
        for row_number, row_data in enumerate(self.taleinfo):
            row='A'+str(row_number+2)
            note=[]
            note.append(str(row_number+1))
            note.append(row_data["code"])
            note.append(row_data["name"])
            note.append(row_data["tempdn"])
            note.append(row_data["yesaidn"])
            note.append(row_data["tempup"])
            note.append(row_data["yesaiup"])
            note.append(row_data["tempeding"])
            note.append(row_data["yesaieding"])
            print(note)
            worksheet1.write_row(row, note)
        workbook.close()  # 关闭表




    def CalPara(self):
        oPara={}
        oPara["name"]=self.name.text()
        oPara["code"]=self.comboBox.currentText()
        oPara["realL"]=self.realL.text()
        oPara["realQ"]=self.realQ.text()
        oPara["tempdn"]=self.tempdn.text()
        oPara["tempeding"]=self.tempeding.text()
        oPara["tempup"]=self.tempeup.text()
        return oPara
    
    def RefreashTable(self):
        irow=len(self.taleinfo)
        self.tableWidget.setRowCount(irow)
        for row_number, row_data in enumerate(self.taleinfo):
            self.tableWidget.setItem(row_number, 0, QtWidgets.QTableWidgetItem(str(row_number+1)))
            self.tableWidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_data["code"])))
            self.tableWidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(row_data["name"])))
            self.tableWidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(row_data["tempdn"])))
            self.tableWidget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(row_data["yesaidn"])))
            self.tableWidget.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(row_data["tempup"])))
            self.tableWidget.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(row_data["yesaiup"])))
            self.tableWidget.setItem(row_number, 7, QtWidgets.QTableWidgetItem(str(row_data["tempeding"])))
            self.tableWidget.setItem(row_number, 8, QtWidgets.QTableWidgetItem(str(row_data["yesaieding"])))
            self.tableWidget.setCellWidget(row_number, 9, self.buttonForRow(row_number))
          
    # 列表内添加按钮
    def buttonForRow(self,id):
        widget=QtWidgets.QWidget()
        # 删除
        deleteBtn = QtWidgets.QPushButton('-')
        deleteBtn.setStyleSheet(''' text-align : center;
                                    background-color : LightCoral;
                                    height : 30px;
                                    border-style: outset;
                                    font : 13px; ''')
        deleteBtn.clicked.connect(lambda: self.deleteRow(id))

        hLayout = QtWidgets.QHBoxLayout()
        # hLayout.addWidget(updateBtn)
        hLayout.addWidget(deleteBtn)
        hLayout.setContentsMargins(5,2,5,2)
        widget.setLayout(hLayout)
        return widget
    
    def deleteRow(self,id):
        del self.taleinfo[id]
        self.RefreashTable()


        
        