# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'e:\Python\CalPile\first.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from CAltools import Tools
import math

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1395, 777)
        self.tools=Tools()
        self.layoutWidget_4 = QtWidgets.QWidget(Form)
        self.layoutWidget_4.setGeometry(QtCore.QRect(72, 263, 691, 22))
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.layoutWidget_4)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.ei_23 = QtWidgets.QLabel(self.layoutWidget_4)
        self.ei_23.setObjectName("ei_23")
        self.gridLayout_5.addWidget(self.ei_23, 0, 0, 1, 1)
        self.pileD_15 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.pileD_15.setObjectName("pileD_15")
        self.gridLayout_5.addWidget(self.pileD_15, 0, 1, 1, 1)
        self.ei_24 = QtWidgets.QLabel(self.layoutWidget_4)
        self.ei_24.setObjectName("ei_24")
        self.gridLayout_5.addWidget(self.ei_24, 0, 2, 1, 1)
        self.pileD_16 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.pileD_16.setObjectName("pileD_16")
        self.gridLayout_5.addWidget(self.pileD_16, 0, 3, 1, 1)
        self.ei_25 = QtWidgets.QLabel(self.layoutWidget_4)
        self.ei_25.setObjectName("ei_25")
        self.gridLayout_5.addWidget(self.ei_25, 0, 4, 1, 1)
        self.pileD_17 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.pileD_17.setObjectName("pileD_17")
        self.gridLayout_5.addWidget(self.pileD_17, 0, 5, 1, 1)
        self.ei_26 = QtWidgets.QLabel(self.layoutWidget_4)
        self.ei_26.setObjectName("ei_26")
        self.gridLayout_5.addWidget(self.ei_26, 0, 6, 1, 1)
        self.pileD_18 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.pileD_18.setObjectName("pileD_18")
        self.gridLayout_5.addWidget(self.pileD_18, 0, 7, 1, 1)
        self.label_16 = QtWidgets.QLabel(Form)
        self.label_16.setGeometry(QtCore.QRect(220, 40, 431, 31))
        self.label_16.setStyleSheet("font: 9pt \"微软雅黑\";\n"
"font: 14pt \"AcadEref\";\n"
"")
        self.label_16.setObjectName("label_16")
        self.cal = QtWidgets.QPushButton(Form)
        self.cal.setGeometry(QtCore.QRect(580, 720, 75, 23))
        self.cal.setObjectName("cal")
        self.pileD_19 = QtWidgets.QLineEdit(Form)
        self.pileD_19.setGeometry(QtCore.QRect(430, 320, 96, 20))
        self.pileD_19.setObjectName("pileD_19")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(790, 40, 571, 701))
        self.textBrowser.setObjectName("textBrowser")
        self.layoutWidget_5 = QtWidgets.QWidget(Form)
        self.layoutWidget_5.setGeometry(QtCore.QRect(70, 90, 701, 131))
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.layoutWidget_5)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.ei_28 = QtWidgets.QLabel(self.layoutWidget_5)
        self.ei_28.setObjectName("ei_28")
        self.gridLayout_6.addWidget(self.ei_28, 0, 0, 1, 1)
        self.comboBox_7 = QtWidgets.QComboBox(self.layoutWidget_5)
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_7, 0, 1, 1, 1)
        self.ei_29 = QtWidgets.QLabel(self.layoutWidget_5)
        self.ei_29.setObjectName("ei_29")
        self.gridLayout_6.addWidget(self.ei_29, 0, 3, 1, 1)
        self.comboBox_8 = QtWidgets.QComboBox(self.layoutWidget_5)
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_8, 0, 4, 1, 2)
        self.ei_30 = QtWidgets.QLabel(self.layoutWidget_5)
        self.ei_30.setObjectName("ei_30")
        self.gridLayout_6.addWidget(self.ei_30, 0, 6, 1, 1)
        self.pileD_20 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.pileD_20.setObjectName("pileD_20")
        self.gridLayout_6.addWidget(self.pileD_20, 0, 7, 1, 1)
        self.ei_31 = QtWidgets.QLabel(self.layoutWidget_5)
        self.ei_31.setObjectName("ei_31")
        self.gridLayout_6.addWidget(self.ei_31, 0, 8, 1, 1)
        self.pileD_21 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.pileD_21.setObjectName("pileD_21")
        self.gridLayout_6.addWidget(self.pileD_21, 0, 9, 1, 1)
        self.alpha_5 = QtWidgets.QLabel(self.layoutWidget_5)
        self.alpha_5.setObjectName("alpha_5")
        self.gridLayout_6.addWidget(self.alpha_5, 1, 0, 1, 1)
        self.gjd_3 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.gjd_3.setObjectName("gjd_3")
        self.gridLayout_6.addWidget(self.gjd_3, 1, 1, 1, 2)
        self.alpha_6 = QtWidgets.QLabel(self.layoutWidget_5)
        self.alpha_6.setObjectName("alpha_6")
        self.gridLayout_6.addWidget(self.alpha_6, 1, 3, 1, 1)
        self.gjn_3 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.gjn_3.setObjectName("gjn_3")
        self.gridLayout_6.addWidget(self.gjn_3, 1, 4, 1, 2)
        self.ei_32 = QtWidgets.QLabel(self.layoutWidget_5)
        self.ei_32.setObjectName("ei_32")
        self.gridLayout_6.addWidget(self.ei_32, 1, 6, 1, 1)
        self.safe_3 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.safe_3.setObjectName("safe_3")
        self.gridLayout_6.addWidget(self.safe_3, 1, 7, 1, 1)
        self.ei_33 = QtWidgets.QLabel(self.layoutWidget_5)
        self.ei_33.setObjectName("ei_33")
        self.gridLayout_6.addWidget(self.ei_33, 1, 8, 1, 1)
        self.comboBox_9 = QtWidgets.QComboBox(self.layoutWidget_5)
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.gridLayout_6.addWidget(self.comboBox_9, 1, 9, 1, 1)
        self.label_17 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_17.setObjectName("label_17")
        self.gridLayout_6.addWidget(self.label_17, 2, 0, 1, 2)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout_6.addWidget(self.lineEdit_13, 2, 2, 1, 2)
        self.label_18 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_18.setObjectName("label_18")
        self.gridLayout_6.addWidget(self.label_18, 2, 4, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout_6.addWidget(self.lineEdit_14, 2, 5, 1, 3)
        self.label_19 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_19.setObjectName("label_19")
        self.gridLayout_6.addWidget(self.label_19, 3, 0, 1, 2)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout_6.addWidget(self.lineEdit_15, 3, 2, 1, 2)
        self.label_20 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_20.setObjectName("label_20")
        self.gridLayout_6.addWidget(self.label_20, 3, 4, 1, 1)
        self.lineEdit_16 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_16.setObjectName("lineEdit_16")
        self.gridLayout_6.addWidget(self.lineEdit_16, 3, 5, 1, 3)
        self.label_21 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_21.setObjectName("label_21")
        self.gridLayout_6.addWidget(self.label_21, 4, 0, 1, 2)
        self.lineEdit_17 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_17.setObjectName("lineEdit_17")
        self.gridLayout_6.addWidget(self.lineEdit_17, 4, 2, 1, 2)
        self.label_22 = QtWidgets.QLabel(self.layoutWidget_5)
        self.label_22.setObjectName("label_22")
        self.gridLayout_6.addWidget(self.label_22, 4, 4, 1, 1)
        self.lineEdit_18 = QtWidgets.QLineEdit(self.layoutWidget_5)
        self.lineEdit_18.setObjectName("lineEdit_18")
        self.gridLayout_6.addWidget(self.lineEdit_18, 4, 5, 1, 3)
        self.exitp = QtWidgets.QPushButton(Form)
        self.exitp.setGeometry(QtCore.QRect(680, 720, 75, 23))
        self.exitp.setObjectName("exitp")
        self.ei_27 = QtWidgets.QLabel(Form)
        self.ei_27.setGeometry(QtCore.QRect(70, 320, 341, 20))
        self.ei_27.setObjectName("ei_27")

        self.retranslateUi(Form)
        self.comboBox_7.setCurrentIndex(1)
        self.comboBox_8.setCurrentIndex(1)
        self.comboBox_9.setCurrentIndex(0)
        self.cal.clicked.connect(self.Cal)
        # self.exitp.clicked.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.ei_23.setText(_translate("Form", "桩端弯矩(kN*m)"))
        self.pileD_15.setText(_translate("Form", "0"))
        self.ei_24.setText(_translate("Form", "桩端水平作用力(kN)"))
        self.pileD_16.setText(_translate("Form", "10"))
        self.ei_25.setText(_translate("Form", "桩悬臂长度(m)"))
        self.pileD_17.setText(_translate("Form", "0"))
        self.ei_26.setText(_translate("Form", "单排桩的桩数"))
        self.pileD_18.setText(_translate("Form", "1"))
        self.label_16.setText(_translate("Form", "单桩基础或垂直于外力作用平面的单排桩基础"))
        self.cal.setText(_translate("Form", "计算"))
        self.pileD_19.setText(_translate("Form", "0"))
        self.ei_28.setText(_translate("Form", "混凝土"))
        self.comboBox_7.setItemText(0, _translate("Form", "C15"))
        self.comboBox_7.setItemText(1, _translate("Form", "C20"))
        self.comboBox_7.setItemText(2, _translate("Form", "C25"))
        self.comboBox_7.setItemText(3, _translate("Form", "C30"))
        self.comboBox_7.setItemText(4, _translate("Form", "C35"))
        self.comboBox_7.setItemText(5, _translate("Form", "C40"))
        self.comboBox_7.setItemText(6, _translate("Form", "C45"))
        self.comboBox_7.setItemText(7, _translate("Form", "C50"))
        self.comboBox_7.setItemText(8, _translate("Form", "C55"))
        self.comboBox_7.setItemText(9, _translate("Form", "C60"))
        self.comboBox_7.setItemText(10, _translate("Form", "C65"))
        self.comboBox_7.setItemText(11, _translate("Form", "C70"))
        self.comboBox_7.setItemText(12, _translate("Form", "C75"))
        self.comboBox_7.setItemText(13, _translate("Form", "C80"))
        self.ei_29.setText(_translate("Form", "钢筋"))
        self.comboBox_8.setItemText(0, _translate("Form", "HPB300"))
        self.comboBox_8.setItemText(1, _translate("Form", "HRB335"))
        self.comboBox_8.setItemText(2, _translate("Form", "HRB400"))
        self.comboBox_8.setItemText(3, _translate("Form", "HRBF400"))
        self.comboBox_8.setItemText(4, _translate("Form", "RRB400"))
        self.comboBox_8.setItemText(5, _translate("Form", "HRB500"))
        self.comboBox_8.setItemText(6, _translate("Form", "HRBF500"))
        self.ei_30.setText(_translate("Form", "桩径（m）"))
        self.pileD_20.setText(_translate("Form", "2"))
        self.ei_31.setText(_translate("Form", "桩长（m）"))
        self.pileD_21.setText(_translate("Form", "8"))
        self.alpha_5.setText(_translate("Form", "钢筋直径（mm）"))
        self.gjd_3.setText(_translate("Form", "25"))
        self.alpha_6.setText(_translate("Form", "钢筋根数"))
        self.gjn_3.setText(_translate("Form", "16"))
        self.ei_32.setText(_translate("Form", "保护层（m）"))
        self.safe_3.setText(_translate("Form", "0.06"))
        self.ei_33.setText(_translate("Form", "支撑类型"))
        self.comboBox_9.setItemText(0, _translate("Form", "非岩石类土中"))
        self.comboBox_9.setItemText(1, _translate("Form", "基岩石表面"))
        self.comboBox_9.setItemText(2, _translate("Form", "嵌固于基岩"))
        self.label_17.setText(_translate("Form", "第1层土m值（MN/m^4）"))
        self.lineEdit_13.setText(_translate("Form", "8"))
        self.label_18.setText(_translate("Form", "第1层土深度（m）"))
        self.lineEdit_14.setText(_translate("Form", "10"))
        self.label_19.setText(_translate("Form", "第2层土m值（MN/m^4）"))
        self.lineEdit_15.setText(_translate("Form", "8"))
        self.label_20.setText(_translate("Form", "第2层土深度（m）"))
        self.lineEdit_16.setText(_translate("Form", "10"))
        self.label_21.setText(_translate("Form", "第3层土m值（MN/m^4）"))
        self.lineEdit_17.setText(_translate("Form", "8"))
        self.label_22.setText(_translate("Form", "第3层土深度（m）"))
        self.lineEdit_18.setText(_translate("Form", "10"))
        self.exitp.setText(_translate("Form", "退出"))
        self.ei_27.setText(_translate("Form", "附录表C.0.3-1第6项求地面以下任一深度的桩身内力的深度y(m)"))

    def Cal(self):
        self.d=float(self.pileD_20.text()) 
        self.hm=2*(self.d+1)
        self.h=float(self.pileD_21.text()) 
        self.m=0.0
        m1=float(self.lineEdit_13.text())
        m2=float(self.lineEdit_15.text())
        m3=float(self.lineEdit_17.text())
        h1=float(self.lineEdit_14.text())
        h2=float(self.lineEdit_16.text())
        h2=float(self.lineEdit_18.text())
        if self.hm<float(self.lineEdit_14.text()):
            self.m=float(self.lineEdit_13.text())
        elif self.hm<float(self.lineEdit_14.text())+float(self.lineEdit_16.text()):
            h2=self.hm-h1
            self.m=(m1*pow(h1,2)+m2*(2*h1+h2)*h2)/(pow(hm,2))
        else:
            h3=self.hm-h1-h2
            self.m=(m1*pow(h1,2)+m2*(2*h1+h2)*h2+m3*(2*h1+2*h2+h3)*h3)/(pow(hm,2))         
        self.Gjd=float(self.gjd_3.text()) 
        self.Gjn=float(self.gjn_3.text()) 
        self.safethink=float(self.safe_3.text()) 
        self.d0=self.d-2*self.safethink 
        self.pg=(pow(self.Gjd,2)*self.Gjn)/(pow((self.d)*1e3,2))
        self.Ehnt=self.tools.GetHnt(self.comboBox_7.currentText())['E']
        self.EGj=self.tools.GetGj(self.comboBox_8.currentText())['E']
        self.ae=self.EGj/self.Ehnt
        self.W0=math.pi*self.d*(self.d*self.d+2*(self.ae-1)*self.pg*self.d0*self.d0)/32
        self.I0=self.W0*self.d0/2
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
        if self.comboBox_9.currentText()== "非岩石类土中":
            self.zhuangtype='非岩石类土中'
            if self.h*self.a<2.5:
                self.Kh=self.C0*self.I0/(self.a*self.EI)
            else:
                self.Kh=self.C0*self.I0/(self.a*self.EI)
        elif self.comboBox_9.currentText()== "基岩石表面":
            self.zhuangtype='基岩石表面'
            if self.h*self.a<3.5:
                self.Kh=self.C0*self.I0/(self.a*self.EI)
            else:
                self.Kh=0.0
        else:
            self.zhuangtype='嵌固于基岩'
            self.Kh=0.0
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
            self.delataHH=(self.B3D4B4D3+self.Kh*self.B2D4B4D2)/((self.A3B4A4B3+self.Kh*self.A2B4A4B2)*pow(self.a,3)*self.EI)
            self.A3D4A4D3=self.GetInserValue(self.ah,type="A3D4-A4D3")
            self.A2D4A4D2=self.GetInserValue(self.ah,type="A2D4-A4D2")
            self.delataMH=(self.A3D4A4D3+self.Kh*self.A2D4A4D2)/((self.A3B4A4B3+self.Kh*self.A2B4A4B2)*pow(self.a,2)*self.EI)
            self.delataHM=self.delataMH
            self.A3C4A4C3=self.GetInserValue(self.ah,type="A3C4-A4C3")
            self.A2C4A4C2=self.GetInserValue(self.ah,type="A2C4-A4C2")
            self.delataMM=(self.A3C4A4C3+self.Kh*self.A2C4A4C2)/((self.A3B4A4B3+self.Kh*self.A2B4A4B2)*pow(self.a,1)*self.EI)
        else:
            self.B2D1B1D2overA2B1A1B2=self.GetInserValue(self.ah,type="B2D1B1D2overA2B1A1B2")
            self.A2D1A1D2overA2B1A1B2=self.GetInserValue(self.ah,type="A2D1A1D2overA2B1A1B2")
            self.A2C1A1C2overA2B1A1B2=self.GetInserValue(self.ah,type="A2C1A1C2overA2B1A1B2")
            self.delataHH=self.B2D1B1D2overA2B1A1B2/(pow(self.a,3)*self.EI)
            self.delataMH=self.A2D1A1D2overA2B1A1B2/(pow(self.a,2)*self.EI)
            self.delataHM=self.delataMH
            self.delataMM=self.A2C1A1C2overA2B1A1B2/(pow(self.a,1)*self.EI)

        self.M=float(self.pileD_15.text())
        self.H=float(self.pileD_16.text())
        self.l0=float(self.pileD_17.text())
        self.n=float(self.pileD_18.text())
        self.M0=self.M/self.n+self.H*self.l0/self.n
        self.H0=self.H/self.n

        self.x0=self.H0*self.delataHH+self.M0*self.delataHM
        self.phi0=-self.H0*self.delataMH-self.M0*self.delataMM

        self.y=float(self.pileD_19.text())
        self.ay=self.a*self.y
        self.A3=self.GetInserValue(self.ay,type="A3")
        self.B3=self.GetInserValue(self.ay,type="B3")
        self.C3=self.GetInserValue(self.ay,type="C3")
        self.D3=self.GetInserValue(self.ay,type="D3")
        self.A4=self.GetInserValue(self.ay,type="A4")
        self.B4=self.GetInserValue(self.ay,type="B4")
        self.C4=self.GetInserValue(self.ay,type="C4")
        self.D4=self.GetInserValue(self.ay,type="D4")
        self.My=pow(self.a,2)*self.EI*(self.x0*self.A3+self.phi0*self.B3/self.a+self.M0*self.C3/(pow(self.a,2)*self.EI)+self.H0*self.D3/(pow(self.a,3)*self.EI))
        self.Hy=pow(self.a,3)*self.EI*(self.x0*self.A4+self.phi0*self.B4/self.a+self.M0*self.C4/(pow(self.a,2)*self.EI)+self.H0*self.D4/(pow(self.a,3)*self.EI))

        self.deltaWeiYi=self.x0-self.phi0*self.l0+self.H*pow(self.l0,3)/(3*self.n*self.EI)+self.M*pow(self.l0,2)/(2*self.n*self.EI)
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
        self.textBrowser.append("主要影响深度hm=2*（%.2f+1)=%.2f\n"%(self.d,self.hm))
        self.textBrowser.append("配筋率ρg=(π*%.2f*%.2f*%d)/(π*%.2f*%.2f)=%.5f \n"%(self.Gjd,self.Gjd,self.Gjn,self.d*1e3,self.d*1e3,self.pg))
        self.textBrowser.append("钢筋与混凝土弹性模量比=%f/%f=%.4f \n"%(self.EGj,self.Ehnt,self.ae))
        self.textBrowser.append("桩身换算截面受拉边缘的截面模量Wo=π*%.2f*(%.2f*%.2f+2*(%.2f-1)*%.4f*%.2f*%.2f)/32=%.4f \n"%(self.d,self.d,self.d,self.ae,self.pg,self.d0,self.d0,self.W0))
        self.textBrowser.append("桩身换算截面惯性矩Io=%.2f*%.2f/2=%.5f\n"%(self.W0,self.d0,self.I0))
        self.textBrowser.append("桩身混凝土弹性模量Ec：%.5f\n"%(self.Ehnt))
        self.textBrowser.append("桩身抗弯刚度EI=0.85*%.5f*%.5f\n"%(self.Ehnt,self.EI))
        self.textBrowser.append("桩计算宽度Bo: %.5f\n"%(self.b0))
        self.textBrowser.append("水平变形系数α=pow(%.5f*%.5f/%.5f,0.2)= %.5f\n"%(self.m,self.b0,self.EI,self.a))
        self.textBrowser.append("桩底面地基土竖向抗力系数C0=%.5f\n"%(self.C0))
        self.textBrowser.append("系数Kh=%.5f\n"%(self.Kh))
        self.textBrowser.append("αh=%.5f\n"%(self.ah))
        if self.zhuangtype=='非岩石类土中' or self.zhuangtype=='基岩石表面':
            self.textBrowser.append("由《桩规》表C.0.3-4 得到B3D4-B4D3=%.5f\n"%(self.B3D4B4D3))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到A3B4-A4B3=%.5f\n"%(self.A3B4A4B3))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到B2D4-B4D2=%.5f\n"%(self.B2D4B4D2))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到A2B4-A4B2=%.5f\n"%(self.A2B4A4B2))
            self.textBrowser.append("桩底支撑类型为%s 时候（附录表C.0.3-1第4项公式计算）δHH=%.5f\n"%(self.zhuangtype,self.delataHH))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到A3D4-A4D3=%.5f\n"%(self.A3D4A4D3))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到A2D4-A4D2=%.5f\n"%(self.A2D4A4D2))
            self.textBrowser.append("桩底支撑类型为%s 时候（附录表C.0.3-1第4项公式计算） δMH=δHM=%.5f\n"%(self.zhuangtype,self.delataHM))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到A3C4-A4C3=%.5f\n"%(self.A3C4A4C3))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到A2C4-A4C2=%.5f\n"%(self.A2C4A4C2))
            self.textBrowser.append("桩底支撑类型为%s 时候（附录表C.0.3-1第4项公式计算） δMM=%.5f\n"%(self.zhuangtype,self.delataMM))
        else:
            self.textBrowser.append("由《桩规》表C.0.3-4 得到（B2D1-B1D2）/（A2B1-A1B2）=%.5f\n"%(self.B2D1B1D2overA2B1A1B2))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到（A2D1-A1D2）/（A2B1-A1B2）=%.5f\n"%(self.A2D1A1D2overA2B1A1B2))
            self.textBrowser.append("由《桩规》表C.0.3-4 得到（A2C1-A1C2）/（A2B1-A1B2）=%.5f\n"%(self.A2C1A1C2overA2B1A1B2))
            self.textBrowser.append("桩底支撑类型为%s 时候（附录表C.0.3-1注第2条公式）δHH=%.5f\n"%(self.zhuangtype,self.delataHH))
            self.textBrowser.append("桩底支撑类型为%s 时候（附录表C.0.3-1注第2条公式） δMH=δHM=%.5f\n"%(self.zhuangtype,self.delataHM))
            self.textBrowser.append("桩底支撑类型为%s 时候（附录表C.0.3-1注第2条公式） δMM=%.5f\n"%(self.zhuangtype,self.delataMM))
        self.textBrowser.append("地面处桩水平位移x0=%.5f\n"%(self.x0))
        self.textBrowser.append("地面处桩转角φ0=%.5f\n"%(self.phi0))
        self.textBrowser.append("地面下深度y=%.5f\n"%(self.y))
        self.textBrowser.append("由《桩规》表C.0.3-4 得到A3、B3、C3、D3=%.5f  %.5f  %.5f  %.5f \n"%(self.A3,self.B3,self.C3,self.D3))
        self.textBrowser.append("由《桩规》表C.0.3-4 得到A4、B4、C4、D4=%.5f  %.5f  %.5f  %.5f \n"%(self.A4,self.B4,self.C4,self.D4))
        self.textBrowser.append("地面下深度y处桩内力（弯矩）=%.5f\n"%(self.My))
        self.textBrowser.append("地面下深度y处桩内力（水平力）=%.5f\n"%(self.Hy))
        self.textBrowser.append("桩顶水平位移Δ=%.5f\n"%(self.deltaWeiYi))
        self.textBrowser.append("《桩规》表C.0.3-4第8项未计算！ \n")
