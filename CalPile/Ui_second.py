# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\PYTHON\CalPile\second.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from CAltools import Tools
import math

class Ui_2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1395, 777)
        self.tools=Tools()
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(131, 32, 391, 16))
        self.label.setStyleSheet("font: 11pt \"AcadEref\";")
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(810, 0, 581, 771))
        self.textBrowser.setObjectName("textBrowser")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(30, 290, 211, 451))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(4)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(2, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(3, 1, item)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(660, 710, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(717, 53, 83, 20))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(657, 53, 54, 16))
        self.label_5.setObjectName("label_5")
        self.comboBox_2 = QtWidgets.QComboBox(Form)
        self.comboBox_2.setGeometry(QtCore.QRect(369, 53, 68, 20))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(443, 53, 54, 16))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(524, 53, 127, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(41, 53, 36, 16))
        self.label_2.setObjectName("label_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(164, 53, 44, 20))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(236, 53, 24, 16))
        self.label_3.setObjectName("label_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(41, 79, 84, 16))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(164, 79, 66, 20))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(236, 79, 48, 16))
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(369, 79, 68, 20))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(443, 79, 66, 16))
        self.label_8.setObjectName("label_8")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(524, 79, 127, 20))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(657, 79, 48, 16))
        self.label_9.setObjectName("label_9")
        self.comboBox_3 = QtWidgets.QComboBox(Form)
        self.comboBox_3.setGeometry(QtCore.QRect(717, 79, 83, 20))
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.label_13 = QtWidgets.QLabel(Form)
        self.label_13.setGeometry(QtCore.QRect(41, 105, 114, 16))
        self.label_13.setObjectName("label_13")
        self.lineEdit_9 = QtWidgets.QLineEdit(Form)
        self.lineEdit_9.setGeometry(QtCore.QRect(164, 105, 66, 20))
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.label_14 = QtWidgets.QLabel(Form)
        self.label_14.setGeometry(QtCore.QRect(236, 105, 90, 16))
        self.label_14.setObjectName("label_14")
        self.lineEdit_10 = QtWidgets.QLineEdit(Form)
        self.lineEdit_10.setGeometry(QtCore.QRect(369, 105, 68, 20))
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.label_15 = QtWidgets.QLabel(Form)
        self.label_15.setGeometry(QtCore.QRect(41, 131, 114, 16))
        self.label_15.setObjectName("label_15")
        self.lineEdit_11 = QtWidgets.QLineEdit(Form)
        self.lineEdit_11.setGeometry(QtCore.QRect(164, 131, 66, 20))
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(236, 131, 90, 16))
        self.label_16.setObjectName("label_16")
        self.lineEdit_12 = QtWidgets.QLineEdit(Form)
        self.lineEdit_12.setGeometry(QtCore.QRect(369, 131, 68, 20))
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.label_17 = QtWidgets.QLabel(Form)
        self.label_17.setGeometry(QtCore.QRect(41, 157, 114, 16))
        self.label_17.setObjectName("label_17")
        self.lineEdit_13 = QtWidgets.QLineEdit(Form)
        self.lineEdit_13.setGeometry(QtCore.QRect(164, 157, 66, 20))
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.label_18 = QtWidgets.QLabel(Form)
        self.label_18.setGeometry(QtCore.QRect(236, 157, 90, 16))
        self.label_18.setObjectName("label_18")
        self.lineEdit_14 = QtWidgets.QLineEdit(Form)
        self.lineEdit_14.setGeometry(QtCore.QRect(369, 157, 68, 20))
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(41, 183, 156, 16))
        self.label_10.setObjectName("label_10")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(203, 183, 93, 20))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(302, 183, 72, 16))
        self.label_11.setObjectName("label_11")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(406, 183, 67, 20))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(479, 183, 84, 16))
        self.label_12.setObjectName("label_12")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(569, 183, 82, 20))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.label_19 = QtWidgets.QLabel(Form)
        self.label_19.setGeometry(QtCore.QRect(269, 209, 36, 16))
        self.label_19.setObjectName("label_19")
        self.lineEdit_15 = QtWidgets.QLineEdit(Form)
        self.lineEdit_15.setGeometry(QtCore.QRect(335, 209, 102, 20))
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.label_20 = QtWidgets.QLabel(Form)
        self.label_20.setGeometry(QtCore.QRect(524, 209, 78, 16))
        self.label_20.setObjectName("label_20")
        self.lineEdit_16 = QtWidgets.QLineEdit(Form)
        self.lineEdit_16.setGeometry(QtCore.QRect(608, 209, 43, 20))
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.label_21 = QtWidgets.QLabel(Form)
        self.label_21.setGeometry(QtCore.QRect(41, 209, 36, 16))
        self.label_21.setObjectName("label_21")
        self.comboBox_4 = QtWidgets.QComboBox(Form)
        self.comboBox_4.setGeometry(QtCore.QRect(86, 209, 62, 20))
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.label_22 = QtWidgets.QLabel(Form)
        self.label_22.setGeometry(QtCore.QRect(443, 105, 96, 16))
        self.label_22.setObjectName("label_22")
        self.label_23 = QtWidgets.QLabel(Form)
        self.label_23.setGeometry(QtCore.QRect(443, 131, 96, 16))
        self.label_23.setObjectName("label_23")
        self.label_24 = QtWidgets.QLabel(Form)
        self.label_24.setGeometry(QtCore.QRect(443, 157, 96, 16))
        self.label_24.setObjectName("label_24")
        self.lineEdit_17 = QtWidgets.QLineEdit(Form)
        self.lineEdit_17.setGeometry(QtCore.QRect(569, 105, 82, 20))
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.lineEdit_18 = QtWidgets.QLineEdit(Form)
        self.lineEdit_18.setGeometry(QtCore.QRect(569, 131, 82, 20))
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.lineEdit_19 = QtWidgets.QLineEdit(Form)
        self.lineEdit_19.setGeometry(QtCore.QRect(569, 157, 82, 20))
        self.lineEdit_19.setObjectName("lineEdit_19")
        self.label_25 = QtWidgets.QLabel(Form)
        self.label_25.setGeometry(QtCore.QRect(657, 209, 101, 16))
        self.label_25.setObjectName("label_25")
        self.lineEdit_20 = QtWidgets.QLineEdit(Form)
        self.lineEdit_20.setGeometry(QtCore.QRect(759, 209, 41, 20))
        self.lineEdit_20.setObjectName("lineEdit_20")
        self.lineEdit_21 = QtWidgets.QLineEdit(Form)
        self.lineEdit_21.setGeometry(QtCore.QRect(610, 240, 43, 20))
        self.lineEdit_21.setObjectName("lineEdit_21")
        self.label_26 = QtWidgets.QLabel(Form)
        self.label_26.setGeometry(QtCore.QRect(526, 240, 78, 16))
        self.label_26.setObjectName("label_26")
        self.lineEdit_22 = QtWidgets.QLineEdit(Form)
        self.lineEdit_22.setGeometry(QtCore.QRect(760, 240, 43, 20))
        self.lineEdit_22.setObjectName("lineEdit_22")
        self.label_27 = QtWidgets.QLabel(Form)
        self.label_27.setGeometry(QtCore.QRect(676, 240, 78, 16))
        self.label_27.setObjectName("label_27")
        self.lineEdit_23 = QtWidgets.QLineEdit(Form)
        self.lineEdit_23.setGeometry(QtCore.QRect(610, 270, 43, 20))
        self.lineEdit_23.setObjectName("lineEdit_23")
        self.label_28 = QtWidgets.QLabel(Form)
        self.label_28.setGeometry(QtCore.QRect(480, 270, 131, 20))
        self.label_28.setObjectName("label_28")

        self.retranslateUi(Form)
        self.lineEdit_15.textChanged['QString'].connect(self.changgetable)
        self.pushButton.clicked.connect(self.Cal)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "位于(或平行于)外力作用面的单排（或多排）低桩承台基础"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "x坐标（mm）"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "y坐标（mm）"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "1500"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "1500"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "-1500"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", "1500"))
        item = self.tableWidget.item(2, 0)
        item.setText(_translate("Form", "-1500"))
        item = self.tableWidget.item(2, 1)
        item.setText(_translate("Form", "-1500"))
        item = self.tableWidget.item(3, 0)
        item.setText(_translate("Form", "1500"))
        item = self.tableWidget.item(3, 1)
        item.setText(_translate("Form", "-1500"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)
        self.pushButton.setText(_translate("Form", "计算"))
        self.lineEdit_2.setText(_translate("Form", "6"))
        self.label_5.setText(_translate("Form", "桩长（m）"))
        self.comboBox_2.setItemText(0, _translate("Form", "HRB400"))
        self.comboBox_2.setItemText(1, _translate("Form", "HRB335"))
        self.comboBox_2.setItemText(2, _translate("Form", "HRB400"))
        self.comboBox_2.setItemText(3, _translate("Form", "HRBF400"))
        self.comboBox_2.setItemText(4, _translate("Form", "RRB400"))
        self.comboBox_2.setItemText(5, _translate("Form", "HRB500"))
        self.comboBox_2.setItemText(6, _translate("Form", "HRBF500"))
        self.label_4.setText(_translate("Form", "桩径（m）"))
        self.lineEdit.setText(_translate("Form", "1.0"))
        self.label_2.setText(_translate("Form", "混凝土"))
        self.comboBox.setItemText(0, _translate("Form", "C35"))
        self.comboBox.setItemText(1, _translate("Form", "C20"))
        self.comboBox.setItemText(2, _translate("Form", "C25"))
        self.comboBox.setItemText(3, _translate("Form", "C30"))
        self.comboBox.setItemText(4, _translate("Form", "C35"))
        self.comboBox.setItemText(5, _translate("Form", "C40"))
        self.comboBox.setItemText(6, _translate("Form", "C45"))
        self.comboBox.setItemText(7, _translate("Form", "C50"))
        self.comboBox.setItemText(8, _translate("Form", "C55"))
        self.comboBox.setItemText(9, _translate("Form", "C60"))
        self.comboBox.setItemText(10, _translate("Form", "C65"))
        self.comboBox.setItemText(11, _translate("Form", "C70"))
        self.comboBox.setItemText(12, _translate("Form", "C75"))
        self.comboBox.setItemText(13, _translate("Form", "C80"))
        self.label_3.setText(_translate("Form", "钢筋"))
        self.label_6.setText(_translate("Form", "钢筋直径（mm）"))
        self.lineEdit_3.setText(_translate("Form", "25"))
        self.label_7.setText(_translate("Form", "钢筋根数"))
        self.lineEdit_4.setText(_translate("Form", "20"))
        self.label_8.setText(_translate("Form", "保护层（m）"))
        self.lineEdit_5.setText(_translate("Form", "0.06"))
        self.label_9.setText(_translate("Form", "支撑类型"))
        self.comboBox_3.setItemText(0, _translate("Form", "非岩石类土中"))
        self.comboBox_3.setItemText(1, _translate("Form", "基岩石表面"))
        self.comboBox_3.setItemText(2, _translate("Form", "嵌固于岩层"))
        self.label_13.setText(_translate("Form", "第一层土m值(MN/m^4)"))
        self.lineEdit_9.setText(_translate("Form", "8"))
        self.label_14.setText(_translate("Form", "第一层土深度(m)"))
        self.lineEdit_10.setText(_translate("Form", "10"))
        self.label_15.setText(_translate("Form", "第二层土m值(MN/m^4)"))
        self.lineEdit_11.setText(_translate("Form", "8"))
        self.label_16.setText(_translate("Form", "第二层土深度(m)"))
        self.lineEdit_12.setText(_translate("Form", "10"))
        self.label_17.setText(_translate("Form", "第三层土m值(MN/m^4)"))
        self.lineEdit_13.setText(_translate("Form", "8"))
        self.label_18.setText(_translate("Form", "第三层土深度(m)"))
        self.lineEdit_14.setText(_translate("Form", "10"))
        self.label_10.setText(_translate("Form", "下压力+承台重（N+G）（kN）"))
        self.lineEdit_6.setText(_translate("Form", "120"))
        self.label_11.setText(_translate("Form", "水平荷载(kN)"))
        self.lineEdit_7.setText(_translate("Form", "100"))
        self.label_12.setText(_translate("Form", "承台弯矩(kN*m)"))
        self.lineEdit_8.setText(_translate("Form", "500"))
        self.label_19.setText(_translate("Form", "桩数目"))
        self.lineEdit_15.setText(_translate("Form", "4"))
        self.label_20.setText(_translate("Form", "承台埋深（m）"))
        self.lineEdit_16.setText(_translate("Form", "1"))
        self.label_21.setText(_translate("Form", "桩类型"))
        self.comboBox_4.setItemText(0, _translate("Form", "摩擦型"))
        self.comboBox_4.setItemText(1, _translate("Form", "摩擦型"))
        self.label_22.setText(_translate("Form", "第一层土内摩擦角"))
        self.label_23.setText(_translate("Form", "第二层土内摩擦角"))
        self.label_24.setText(_translate("Form", "第三层土内摩擦角"))
        self.lineEdit_17.setText(_translate("Form", "15"))
        self.lineEdit_18.setText(_translate("Form", "15"))
        self.lineEdit_19.setText(_translate("Form", "15"))
        self.label_25.setText(_translate("Form", "承台效应系数ηc"))
        self.lineEdit_20.setText(_translate("Form", "1"))
        self.lineEdit_21.setText(_translate("Form", "5"))
        self.label_26.setText(_translate("Form", "承台长L（m）"))
        self.lineEdit_22.setText(_translate("Form", "5"))
        self.label_27.setText(_translate("Form", "承台宽B（m）"))
        self.lineEdit_23.setText(_translate("Form", "0.4"))
        self.label_28.setText(_translate("Form", "承台底部摩擦系数μ"))		
    def changgetable(self,string):
        if string=='':
            pass
        else:
            self.tableRowCount=int(string)
            self.tableWidget.setRowCount(self.tableRowCount)
            for i in range(self.tableRowCount):
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setVerticalHeaderItem(i, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(0, 0, item)
                item = QtWidgets.QTableWidgetItem()
                self.tableWidget.setItem(0, 1, item)
    def GetZhuangXY(self):
        ZhuangXY=[]
        for i in range(self.tableWidget.rowCount()):
            xy={}
            item1= self.tableWidget.item(i, 0)
            item2= self.tableWidget.item(i, 1)
            xy["x"]=float(item1.text())
            xy["y"]=float(item2.text())
            ZhuangXY.append(xy)
        return ZhuangXY

    def Cal(self):
        self.d=float(self.lineEdit.text()) 
        self.hm=2*(self.d+1)
        self.h=float(self.lineEdit_2.text()) 
        self.m=0.0
        m1=float(self.lineEdit_9.text())
        m2=float(self.lineEdit_11.text())
        m3=float(self.lineEdit_13.text())
        h1=float(self.lineEdit_10.text())
        h2=float(self.lineEdit_12.text())
        if self.hm<float(self.lineEdit_10.text()):
            self.m=float(self.lineEdit_9.text())
        elif self.hm<float(self.lineEdit_10.text())+float(self.lineEdit_12.text()):
            h2=self.hm-h1
            self.m=(m1*pow(h1,2)+m2*(2*h1+h2)*h2)/(pow(self.hm,2))
        else:
            h3=self.hm-h1-h2
            self.m=(m1*pow(h1,2)+m2*(2*h1+h2)*h2+m3*(2*h1+2*h2+h3)*h3)/(pow(self.hm,2))  
        self.Gjd=float(self.lineEdit_3.text()) 
        self.Gjn=float(self.lineEdit_4.text()) 
        self.safethink=float(self.lineEdit_5.text()) 
        self.d0=self.d-2*self.safethink -2*8*1e-3  #扣掉两个箍筋直径
        self.pg=(pow(self.Gjd,2)*self.Gjn)/(pow((self.d)*1e3,2))
        self.Ehnt=self.tools.GetHnt(self.comboBox.currentText())['E']
        self.EGj=self.tools.GetGj(self.comboBox_2.currentText())['E']
        self.ae=self.EGj/self.Ehnt
        self.W0=math.pi*self.d*(self.d*self.d+2*(self.ae-1)*self.pg*self.d0*self.d0)/32
        self.I0=self.W0*self.d/2  #《桩基规范用的是扣除保护层后的桩径》
        # self.I0=math.pi*pow(self.d, 4)/64 临时算法
        self.EI=0.85*self.Ehnt*self.I0
        self.b0=0.0
        if self.d>1:
            self.b0=0.9*(self.d+1)
        else:
            self.b0=0.9*(1.5*self.d+0.5)
        self.a=pow(self.m*self.b0/self.EI,0.2)
        self.C0=0
        if self.h>h1+h2:
            if self.h<10:
                self.C0=m3*10
            else:
                self.C0=self.h*m3
        elif self.h>h1:
            if self.h<10:
                self.C0=m2*10
            else:
                self.C0=self.h*m2
        else:
            if self.h<10:
                self.C0=m1*10
            else:
                self.C0=self.h*m1 
        self.Kh=0.0
        self.zhuangtype=''
        if self.comboBox_3.currentText()== "非岩石类土中":
            self.zhuangtype='非岩石类土中'
            if self.h*self.a<2.5:
                self.Kh=self.C0*self.I0/(self.a*self.EI)
            else:
                self.Kh=self.C0*self.I0/(self.a*self.EI)
        elif self.comboBox_3.currentText()== "基岩石表面":
            self.zhuangtype='基岩石表面'
            if self.h*self.a<3.5:
                self.Kh=self.C0*self.I0/(self.a*self.EI)
            else:
                self.Kh=0.0
        else:
            self.zhuangtype='嵌固于基岩'
            self.Kh=0.0
        self.Kh=0.0#表C.0.3-2步骤3
        self.ah=self.h*self.a
        self.delataHH=0
        self.delataHM=0
        self.delataMH=0
        self.delataMM=0
        if self.zhuangtype=='非岩石类土中' or self.zhuangtype=='基岩石表面':
            self.B3D4B4D3=self.GetInserValue(self.ah,type="B3D4-B4D3")
            self.A3B4A4B3=self.GetInserValue(self.ah,type="A3B4-A4B3")
            self.B2D4B4D2=self.GetInserValue(self.ah,type="B2D4-B4D2")
            self.A2B4A4B2=self.GetInserValue(self.ah,type="A2B4-A4B2")
            self.delataHH=1e-3*(self.B3D4B4D3+self.Kh*self.B2D4B4D2)/((self.A3B4A4B3+self.Kh*self.A2B4A4B2)*pow(self.a,3)*self.EI)
            self.A3D4A4D3=self.GetInserValue(self.ah,type="A3D4-A4D3")
            self.A2D4A4D2=self.GetInserValue(self.ah,type="A2D4-A4D2")
            self.delataMH=1e-3*(self.A3D4A4D3+self.Kh*self.A2D4A4D2)/((self.A3B4A4B3+self.Kh*self.A2B4A4B2)*pow(self.a,2)*self.EI)
            self.delataHM=self.delataMH
            self.A3C4A4C3=self.GetInserValue(self.ah,type="A3C4-A4C3")
            self.A2C4A4C2=self.GetInserValue(self.ah,type="A2C4-A4C2")
            self.delataMM=1e-3*(self.A3C4A4C3+self.Kh*self.A2C4A4C2)/((self.A3B4A4B3+self.Kh*self.A2B4A4B2)*pow(self.a,1)*self.EI)
        else:
            self.B2D1B1D2overA2B1A1B2=self.GetInserValue(self.ah,type="B2D1B1D2overA2B1A1B2")
            self.A2D1A1D2overA2B1A1B2=self.GetInserValue(self.ah,type="A2D1A1D2overA2B1A1B2")
            self.A2C1A1C2overA2B1A1B2=self.GetInserValue(self.ah,type="A2C1A1C2overA2B1A1B2")
            self.delataHH=1e-3*self.B2D1B1D2overA2B1A1B2/(pow(self.a,3)*self.EI)
            self.delataMH=1e-3*self.A2D1A1D2overA2B1A1B2/(pow(self.a,2)*self.EI)
            self.delataHM=self.delataMH
            self.delataMM=1e-3*self.A2C1A1C2overA2B1A1B2/(pow(self.a,1)*self.EI)
        self.XiN=0.0
        if self.comboBox_4.currentText()== "端承型":
            self.XiN=1.0
        else:
            self.XiN=0.5
        self.A0=0.0
        if self.comboBox_4.currentText()== "端承型":
            self.A0=self.d*self.d*math.pi/4
        else:
            self.phim=0.0
            if self.h<h1:
                self.phim=float(self.lineEdit_17.text())
            elif self.h<h1+h2:
                self.phim=(float(self.lineEdit_17.text())*h1+float(self.lineEdit_18.text())*(self.h-h1))/self.h
            else:
                self.phim=(float(self.lineEdit_17.text())*h1+float(self.lineEdit_18.text())*h2+float(self.lineEdit_19.text())*(self.h-h1-h2))/self.h
            A01=math.pi*pow(self.h*math.tan(self.phim/720*math.pi)+self.d/2,2)
            print("A01=",A01)
            self.s=math.sqrt(math.pow(float(self.tableWidget.item(0, 0).text())-float(self.tableWidget.item(1, 0).text()),2)+math.pow(float(self.tableWidget.item(0, 1).text())-float(self.tableWidget.item(1, 1).text()),2))
            A02=math.pi/4*pow(self.s*1e-3,2)
            print("self.s=",self.s)
            print("A02=",A02)
            self.A0=min(A01, A02)
            print("self.A0=",self.A0)
        C0A0=self.C0*self.A0*1e3
        EA=self.Ehnt*1e3*self.d*self.d*math.pi/4
        print("EA=",EA)
        # print("C0A0",C0A0,"EA",EA)
        self.RhoNN=1/(self.XiN*self.h/EA+1/C0A0)
        print("self.RhoNN=",self.RhoNN)
        self.RhoHH=self.delataMM/(self.delataHH*self.delataMM-self.delataMH*self.delataMH)
        self.RhoMH=self.delataMH/(self.delataHH*self.delataMM-self.delataMH*self.delataMH)
        self.RhoHM=self.RhoMH
        self.RhoMM=self.delataHH/(self.delataHH*self.delataMM-self.delataMH*self.delataMH)
        self.hn=float(self.lineEdit_16.text())
        self.Cn=m1*self.hn*1e3
        self.etac=float(self.lineEdit_20.text()) 
        self.Cb=m1*self.hn*self.etac
        self.CtL=float(self.lineEdit_21.text())
        self.CtB=float(self.lineEdit_22.text())
        self.F=self.CtL*self.CtB
        self.Ab=self.F-float(self.lineEdit_15.text())*self.d*self.d*math.pi/4
        self.Fc=0.5*self.Cn*self.hn
        self.Sc=self.Cn*self.hn*self.hn/6
        self.Ic=self.Cn*self.hn*self.hn*self.hn/12
        self.ZhuangXY=self.GetZhuangXY()
        ZhuangY=set()
        pai={}
        for Zhuang in self.ZhuangXY:
            if Zhuang["y"] in ZhuangY:
                pai[Zhuang["y"]].append(Zhuang["x"])
                pass
            else:
                pai[Zhuang["y"]]=[]
                pai[Zhuang["y"]].append(Zhuang["x"])
                ZhuangY.add(Zhuang["y"])
        self.KiSumx2=0
        for izhuang in self.ZhuangXY:
            self.KiSumx2+=pow(izhuang['x']*1e-3,2)
        self.SumAx2=self.KiSumx2*self.d*self.d*math.pi/4
        self.Ib=self.CtB*pow(self.CtL,3)/12-self.SumAx2
        self.rVV=float(self.lineEdit_15.text())*self.RhoNN+self.Cb*self.Ab*1e3
        self.mu=float(self.lineEdit_10.text())
        self.rUV=self.mu*self.Cb*self.Ab*1e3
        self.B0=self.CtB+1
        self.rUU=float(self.lineEdit_15.text())*self.RhoHH+self.B0*self.Fc
        self.rbU=-float(self.lineEdit_15.text())*self.RhoMH+self.B0*self.Sc
        self.rUb=self.rbU
        self.rbb=float(self.lineEdit_15.text())*self.RhoMM+self.RhoNN*self.KiSumx2+self.B0*self.Ic+self.Cb*self.Ib
        self.NG=float(self.lineEdit_6.text())
        self.H=float(self.lineEdit_7.text())
        self.M=float(self.lineEdit_8.text())
        self.V=self.NG/self.rVV
        self.U=(self.rbb*self.H-self.rUb*self.M)/(self.rUU*self.rbb-self.rUb*self.rUb)-(self.NG*self.rUV*self.rbb)/(self.rVV*self.rUU*self.rbb-self.rVV*self.rUb*self.rUb)
        self.b=(self.rUU*self.M-self.rUb*self.H)/(self.rUU*self.rbb-self.rUb*self.rUb)-(self.NG*self.rUV*self.rUb)/(self.rVV*self.rUU*self.rbb-self.rVV*self.rUb*self.rUb)
        self.zhuangNeiLi=[]
        indexZhuang=0
        for Zhuang in self.ZhuangXY:
            indexZhuang+=1
            Neili={}
            Neili["Index"]=indexZhuang
            Neili["zuobiao"]=Zhuang
            Neili["Noi"]=(self.V+self.b*Zhuang["x"]*1e-3)*self.RhoNN
            Neili["Hoi"]=self.U*self.RhoHH-self.b*self.RhoHM
            Neili["Moi"]=self.b*self.RhoMM-self.U*self.RhoMH
            self.zhuangNeiLi.append(Neili)
        self.WriteMsg()
    def GetInserValue(self,ay,**kwargs):
        if ay>4:
            ay=4
        arrX=self.tools.GetValueFromXls('E:\\pp.xls',0)
        arrY=[]
        if kwargs['type']=='B3D4-B4D3':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',9)
        elif kwargs['type']=='A3B4-A4B3':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',10)
        elif kwargs['type']=='B2D4-B4D2':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',11)
        elif kwargs['type']=='A2B4-A4B2':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',12)
        elif kwargs['type']=='A3D4-A4D3':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',13)
        elif kwargs['type']=='A2D4-A4D2':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',14)
        elif kwargs['type']=='A3C4-A4C3':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',15)
        elif kwargs['type']=='A2C4-A4C2':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',16)
        elif kwargs['type']=='A3':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',1)
        elif kwargs['type']=='B3':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',2)
        elif kwargs['type']=='C3':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',3)
        elif kwargs['type']=='D3':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',4)
        elif kwargs['type']=='A4':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',5)
        elif kwargs['type']=='B4':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',6)
        elif kwargs['type']=='C4':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',7)
        elif kwargs['type']=='D4':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',8)
        elif kwargs['type']=='B2D1B1D2overA2B1A1B2':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',20)
        elif kwargs['type']=='A2D1A1D2overA2B1A1B2':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',21)
        elif kwargs['type']=='A2C1A1C2overA2B1A1B2':
            arrY=self.tools.GetValueFromXls('E:\\pp.xls',22)
        return self.tools.GetInsrtValue(arrX,arrY,ay)

    def WriteMsg(self):
        self.textBrowser.setText("")
        self.textBrowser.append("注意：①在计算Cb时候，承台效应系数按照0计算的 承台与承台底土摩擦系数也是按0算的")
        self.textBrowser.append("主要影响深度hm=2*（%.2f+1)=%.2f\n"%(self.d,self.hm))
        self.textBrowser.append("配筋率ρg=(π*%.2f*%.2f*%d)/(π*%.2f*%.2f)=%.5f \n"%(self.Gjd,self.Gjd,self.Gjn,self.d*1e3,self.d*1e3,self.pg))
        self.textBrowser.append("钢筋与混凝土弹性模量比=%f/%f=%.4f \n"%(self.EGj,self.Ehnt,self.ae))
        self.textBrowser.append("桩身换算截面受拉边缘的截面模量Wo=π*%.2f*(%.2f*%.2f+2*(%.2f-1)*%.4f*%.2f*%.2f)/32=%.4f \n"%(self.d,self.d,self.d,self.ae,self.pg,self.d0,self.d0,self.W0))
        self.textBrowser.append("桩身换算截面惯性矩Io=%.2f*%.2f/2=%.5f\n"%(self.W0,self.d0,self.I0))
        self.textBrowser.append("桩身混凝土弹性模量Ec：%.5f\n"%(self.Ehnt))
        self.textBrowser.append("桩身抗弯刚度EI=0.85*%.5f*%.5f=%.5f\n"%(self.Ehnt,self.I0,self.EI))
        self.textBrowser.append("桩计算宽度Bo: %.5f\n"%(self.b0))
        self.textBrowser.append("水平变形系数α=pow(%.5f*%.5f/%.5f,0.2)= %.5f\n"%(self.m,self.b0,self.EI,self.a))
        self.textBrowser.append("由《桩规》表C.0.2-4 得到桩底面地基竖向抗力系数 C0=%.5f\n"%(self.C0))
        if self.zhuangtype=='非岩石类土中' or self.zhuangtype=='基岩石表面':
            self.textBrowser.append("由《桩规》表C.0.3-4 得到B3D4-B4D3=%.5f\n"%(self.B3D4B4D3))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到A3B4-A4B3=%.5f\n"%(self.A3B4A4B3))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到B2D4-B4D2=%.5f\n"%(self.B2D4B4D2))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到A2B4-A4B2=%.5f\n"%(self.A2B4A4B2))
            self.textBrowser.append("桩底支撑类型为%s 时候（附录表C.0.3-1第4项公式计算）δHH=%.10f\n"%(self.zhuangtype,self.delataHH))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到A3D4-A4D3=%.5f\n"%(self.A3D4A4D3))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到A2D4-A4D2=%.5f\n"%(self.A2D4A4D2))
            self.textBrowser.append("桩底支撑类型为%s 时候（附录表C.0.3-1第4项公式计算） δMH=δHM=%.10f\n"%(self.zhuangtype,self.delataHM))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到A3C4-A4C3=%.5f\n"%(self.A3C4A4C3))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到A2C4-A4C2=%.5f\n"%(self.A2C4A4C2))
            self.textBrowser.append("桩底支撑类型为%s 时候（附录表C.0.3-1第4项公式计算） δMM=%.10f\n"%(self.zhuangtype,self.delataMM))
        else:
            self.textBrowser.append("由《桩规》表C.0.3-4 得到（B2D1-B1D2）/（A2B1-A1B2）=%.5f\n"%(self.B2D1B1D2overA2B1A1B2))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到（A2D1-A1D2）/（A2B1-A1B2）=%.5f\n"%(self.A2D1A1D2overA2B1A1B2))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到（A2C1-A1C2）/（A2B1-A1B2）=%.5f\n"%(self.A2C1A1C2overA2B1A1B2))
            self.textBrowser.append("桩底支撑类型为%s 时候（附录表C.0.3-1注第2条公式）δHH=%.10f\n"%(self.zhuangtype,self.delataHH))
            self.textBrowser.append("桩底支撑类型为%s 时候（附录表C.0.3-1注第2条公式） δMH=δHM=%.10\n"%(self.zhuangtype,self.delataHM))
            self.textBrowser.append("桩底支撑类型为%s 时候（附录表C.0.3-1注第2条公式） δMM=%.10\n"%(self.zhuangtype,self.delataMM))
        self.textBrowser.append("桩身轴向压力传递系数ξN=%.1f\n"%(self.XiN))
        if self.comboBox_4.currentText()== "端承型":
            self.textBrowser.append("端承型桩按照（附录表C.0.3-2注第2条公式）A0=%.5f\n"%(self.A0))
        else:
            self.textBrowser.append("摩擦型桩按照（附录表C.0.3-2注第2条公式）A0=%.5f\n"%(self.A0))
            self.textBrowser.append("其中 桩周内摩阻角加权值φm=%.5f(°);桩的中心距s=%.5f(m)\n"%(self.phim,self.s*1e-3))
        self.textBrowser.append("发生单位竖向位移时轴向力（附录表C.0.3-2第4项公式）ρNN=%.5f\n"%(self.RhoNN))
        self.textBrowser.append("发生单位水平位移时水平力（附录表C.0.3-2第4项公式）ρHH=%.5f\n"%(self.RhoHH))
        self.textBrowser.append("发生单位水平位移时弯矩（附录表C.0.3-2第4项公式）ρMH=%.5f\n"%(self.RhoMH))
        self.textBrowser.append("发生单位转角时水平力（附录表C.0.3-2第4项公式）ρHM=%.5f\n"%(self.RhoHM))
        self.textBrowser.append("发生单位转角时弯矩（附录表C.0.3-2第4项公式）ρMM=%.5f\n"%(self.RhoMM))
        self.textBrowser.append("--------------------------------------------------------------------\n")
        self.textBrowser.append("根据式 C.0.2-4 承台侧面地基水平抗力系数（目前仅支持承台埋入在第一层土中）Cn=m0*h=%.2f*%.2f=%.2f\n"%(float(self.lineEdit_9.text()),self.h if self.h > 10 else 10,self.Cn))
        self.textBrowser.append("根据《桩规》 表5.2.5 承台效应系数（当前小程序在界面输入）ηc=%.5f\n"%(self.etac))
        self.textBrowser.append("根据式 C.0.2-5 承台底地基土竖向抗力系数Cb=m0*hn*ηc=%.2f*%.2f*%.2f=%.2f\n"%(float(self.lineEdit_9.text()),self.hn,self.etac,self.Cb))
        self.textBrowser.append("根据《桩规》P135 表C.0.3-2 注第3条 承台底面以上侧向水平抗力系数C图像的面积 Fc=Cn*hn/2=%.2f*%.2f/2=%.2f\n"%(self.Cn,self.hn,self.Fc))
        self.textBrowser.append("根据《桩规》P135 表C.0.3-2 注第3条 对于底面的面积矩 Sc=Cn*hn^2/6=%.2f*%.2f^2/6=%.2f\n"%(self.Cn,self.hn,self.Sc))
        self.textBrowser.append("根据《桩规》P135 表C.0.3-2 注第3条 对于底面的惯性矩 Ic=Cn*hn^3/12=%.2f*%.2f^3/12=%.2f\n"%(self.Cn,self.hn,self.Ic))
        self.textBrowser.append("ΣKi * x^2=%.5f\n"%(self.KiSumx2))
        self.textBrowser.append("Ib=IF-ΣAKi * xi^2=%.5f m^4\n"%(self.Ib))
        self.textBrowser.append("--------------------------------------------------------------------\n")
        self.textBrowser.append("发生单位竖向位移时竖向反力（附录表C.0.3-2第5项公式）γVV=%.5f\n"%(self.rVV))
        self.textBrowser.append("发生单位竖向位移时水平反力（附录表C.0.3-2第5项公式）γUV=%.5f\n"%(self.rUV))
        self.textBrowser.append("发生单位水平位移时水平反力（附录表C.0.3-2第5项公式）γUU=%.5f\n"%(self.rUU))
        self.textBrowser.append("发生单位水平位移时反弯矩（附录表C.0.3-2第5项公式）γβU=%.5f\n"%(self.rbU))
        self.textBrowser.append("发生单位水转角时水平反力（附录表C.0.3-2第5项公式）γUβ=%.5f\n"%(self.rUb))
        self.textBrowser.append("发生单位水转角时反弯矩（附录表C.0.3-2第5项公式）γββ=%.5f\n"%(self.rbb))
        self.textBrowser.append("承台竖向位移（L）（附录表C.0.3-2第6项公式）V=%.7f\n"%(self.V))
        self.textBrowser.append("承台水平位移（L）（附录表C.0.3-2第6项公式）U=%.7f\n"%(self.U))
        self.textBrowser.append("承台转角（弧度）（附录表C.0.3-2第6项公式）β=%.7f\n"%(self.b))
        self.textBrowser.append("--------------------------------------------------------------------\n")
        self.textBrowser.append("桩号      x坐标       y坐标        轴向力      水平力      弯矩\n")
        for i in self.zhuangNeiLi:
            self.textBrowser.append("%d     %.5f        %.5f        %.5f        %.5f        %.5f \n"%(i["Index"],i['zuobiao']["x"],i['zuobiao']["y"],i["Noi"],i["Hoi"],i["Moi"]))
        self.textBrowser.append("------------------------------------END-----------------------------\n")
