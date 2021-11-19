# -*- coding: utf-8 -*-

# self implementation generated from reading ui file 'd:\PYTHON\HotPile\UI\Ui_XiangxiPinggu\XiangxiPinggu.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget,QDialog
from Subassembly import LineEditInTable
from Tools import ProductSelect,ErYuanZhuangZhi,Common
import gl 
import math


class Ui_XiangxiPinggu(QWidget):
    def __init__(self, parent = None):
        super(QWidget, self).__init__(parent)
        self.tableData=[['','','','','','','']]
        self.type=-1 #
        self.setupUi()

    def setupUi(self):
        self.setObjectName("self")
        self.resize(1800*gl.w, 1000*gl.h)
        self.DaoTong_PingGu = QtWidgets.QPushButton(self)
        self.DaoTong_PingGu.setGeometry(QtCore.QRect(60*gl.w, 90*gl.h, 100*gl.w, 30*gl.h))
        self.DaoTong_PingGu.setObjectName("DaoTong_PingGu")
        self.ZhengFa_PingGu = QtWidgets.QPushButton(self)
        self.ZhengFa_PingGu.setGeometry(QtCore.QRect(60*gl.w, 150*gl.h, 100*gl.w, 30*gl.h))
        self.ZhengFa_PingGu.setObjectName("ZhengFa_PingGu")
        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(360*gl.w, 90*gl.h, 70*gl.w, 25*gl.h))
        self.label_3.setObjectName("label_3")
        self.ChuanreGongzhi = QtWidgets.QComboBox(self)
        self.ChuanreGongzhi.setGeometry(QtCore.QRect(460*gl.w, 90*gl.h, 70*gl.w, 25*gl.h))
        self.ChuanreGongzhi.setObjectName("ChuanreGongzhi")
        self.ChuanreGongzhi.addItem("")
        self.ChuanreGongzhi.addItem("")
        self.ChuanreGongzhi.addItem("")
        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(600*gl.w, 90*gl.h, 70*gl.w, 25*gl.h))
        self.label_4.setObjectName("label_4")
        self.KongzhiQiti = QtWidgets.QComboBox(self)
        self.KongzhiQiti.setGeometry(QtCore.QRect(700*gl.w, 90*gl.h, 70*gl.w, 25*gl.h))
        self.KongzhiQiti.setObjectName("KongzhiQiti")
        self.KongzhiQiti.addItem("")
        self.KongzhiQiti.addItem("")
        self.KongzhiQiti.addItem("")
        self.KongzhiQiti.addItem("")
        self.GuanXin = QtWidgets.QComboBox(self)
        self.GuanXin.setGeometry(QtCore.QRect(920*gl.w, 90*gl.h, 70*gl.w, 25*gl.h))
        self.GuanXin.setObjectName("GuanXin")
        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(820*gl.w, 90*gl.h, 70*gl.w, 25*gl.h))
        self.label_5.setObjectName("label_5")
        self.tableWidget = QtWidgets.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.hide()
        self.retranslateUi(self)
        self.InitData()
        self.BindingEvents()
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("self", "Form"))
        self.DaoTong_PingGu.setText(_translate("self", "导通比例评估"))
        self.ZhengFa_PingGu.setText(_translate("self", "蒸发段温度评估"))
        self.label_3.setText(_translate("self", "传热工质："))
        self.ChuanreGongzhi.setItemText(0, _translate("self", "NH3"))
        self.ChuanreGongzhi.setItemText(1, _translate("self", "乙烷"))
        self.ChuanreGongzhi.setItemText(2, _translate("self", "丙烯"))
        self.label_4.setText(_translate("self", "控制气体："))
        self.KongzhiQiti.setItemText(0, _translate("self", "N2"))
        self.KongzhiQiti.setItemText(1, _translate("self", "Ne"))
        self.KongzhiQiti.setItemText(2, _translate("self", "H2"))
        self.KongzhiQiti.setItemText(3, _translate("self", "He"))
        self.label_5.setText(_translate("self", "管型："))
    
    def InitData(self):
        Productlist=ProductSelect.GetProductInfo()
        for i in range(len(Productlist)):
            self.GuanXin.addItem("")
            self.GuanXin.setItemText(i, Productlist[i]["code"])
        self.data={
            "title_DaoTong":['储气室温度(℃)','冷凝阻塞段温度(℃)','蒸发段温度(℃)','物质的量(mol)','储气室容积(ml)','Vr/Vc','导通比例(%)'],
            "title_ZhengFa":['储气室温度(℃)','冷凝阻塞段温度(℃)','导通比例(%)','物质的量(mol)','储气室容积(ml)','Vr/Vc','蒸发段温度(℃)'],
        }
 
    
    #绑定事件
    def BindingEvents(self):
        self.DaoTong_PingGu.clicked.connect(self.ClickDaoTongPingGu)
        self.ZhengFa_PingGu.clicked.connect(self.ZhengFaPingGu)
    
    def ClickDaoTongPingGu(self):
        self.DaoTong_PingGu.setStyleSheet(
            "color:rgb(0,0,255)"
        )
        self.ZhengFa_PingGu.setStyleSheet(
            "color:rgb(0,0,0)"
        )
        if self.tableWidget.isHidden():
            self.tableWidget.show()
        self.type=1
        self.Refresh()
        self.showTable(self.type)
      

    def ZhengFaPingGu(self):
        self.ZhengFa_PingGu.setStyleSheet(
            "color:rgb(0,0,255)"
        )
        self.DaoTong_PingGu.setStyleSheet(
            "color:rgb(0,0,0)"
        )
        if self.tableWidget.isHidden():
            self.tableWidget.show()
        self.type=2
        self.Refresh()
        self.showTable(self.type)
 
    
    def showTable(self,itype):
        self.tableWidget.verticalHeader().setVisible(False) 
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        tableData=self.makedata(itype)
        self.tableWidget.setColumnCount(len(tableData["title"]))
        self.tableWidget.setRowCount(len(tableData["data"])+1)
        totalw=0
        totalh=0
        w=120
        h=35
        for index in range(len(tableData["title"])):
            self.tableWidget.setColumnWidth(index, w*gl.w);
            totalw=totalw+w
        for index2 in range(len(tableData["data"])):
            self.tableWidget.setRowHeight(index2, h*gl.h);
            totalh=totalh+h
        self.tableWidget.setGeometry(QtCore.QRect(360*gl.w, 150*gl.h, (totalw+5)*gl.w,(totalh+40)*gl.h))
        for index1 in range(len(tableData["title"])):
            cellitem=QtWidgets.QTableWidgetItem(str(tableData["title"][index1]))
            if index1==len(tableData["title"])-1:
                cellitem.setBackground(QtGui.QColor(211, 211, 211, 160))
            self.tableWidget.setItem(0, index1, cellitem)
        for index3 in range(len(tableData["data"])):
            for index4 in range(len(tableData["data"][index3])): 
                allowed=False
                if index4==len(tableData["data"][index3])-1:
                    allowed=True
                item=LineEditInTable.MyLineEdit(index3,index4,str(tableData["data"][index3][index4]),allowed)
                item.mySignal.connect(self.GetLineEdit)
                self.tableWidget.setCellWidget(index3+1,index4,item)
        # self.setStyleSheet()


    #根据输入参数生成数据
    def makedata(self,itype):
        res={}
        res["title"]=self.data["title_DaoTong"] if itype==1 else self.data["title_ZhengFa"]
        res["data"]=self.tableData
        return res
    
    
    #刷新数据
    def refresh(self,val1,val2):
        print(val1,val2)
        self.tableWidget.cellChanged()
        pass

    #接受信号函数
    def GetLineEdit(self,connect):
        data=eval(connect)
        row=Common.ToInt(data["row"])
        column=Common.ToInt(data["column"])
        value=0
        if len(data["text"])==0:
            value=""
        else:
            value=float(data["text"])
        #防错
        if row>len(self.tableData)-1:
            return
        if column>len(self.tableData[row])-1:
            return
        self.tableData[row][column]=value
        if self.type==1:
            F=ErYuanZhuangZhi.CToK(Common.ToDouble(self.tableData[row][0]))
            G=ErYuanZhuangZhi.CToK(Common.ToDouble(self.tableData[row][1]))
            H=ErYuanZhuangZhi.CToK(Common.ToDouble(self.tableData[row][2]))
            K=Common.ToDouble(self.tableData[row][3])
            M=Common.ToDouble(self.tableData[row][4])
            N=Common.ToDouble(self.tableData[row][5])
            self.tableData[row][-1]=ErYuanZhuangZhi.CalQ(F,G,H,K,M,N)
            self.FormatData()
        if self.type==2:
            F=ErYuanZhuangZhi.CToK(Common.ToDouble(self.tableData[row][0]))
            G=ErYuanZhuangZhi.CToK(Common.ToDouble(self.tableData[row][1]))
            Q=Common.ToDouble(self.tableData[row][3])
            K=Common.ToDouble(self.tableData[row][3])
            M=Common.ToDouble(self.tableData[row][4])
            N=Common.ToDouble(self.tableData[row][5])
            self.tableData[row][-1]=ErYuanZhuangZhi.Calh(F,G,Q,K,M,N)
            self.FormatData()
        #处理最后一列填数,判断是否需要增一行并处理
        if column==5:
            self.IsAddRow()
        self.showTable(self.type)
    
    #分析表格数据，当存在某一行设计数据（除去最后一列）全部为0时删除该行数据，同时保留最后一行数据为默认空数据
    def FormatData(self):
        tabledata=self.tableData
        for index  in range(len(self.tableData)):
            iflg=0
            for index1 in range(len(self.tableData[index])-1): 
                if Common.ToDouble(self.tableData[index][index1])!=0:
                    iflg=1
                    break
            if iflg==0 and index!=len(self.tableData)-1:
                self.tableData.remove(self.tableData[index])
                break
        
    
    def IsAddRow(self):
        countrow=len(self.tableData)
        #判断最后一行是否都为0
        ilastflg=0
        for index3 in range(len(self.tableData[countrow-1])-1): 
                if Common.ToDouble(self.tableData[countrow-1][index3])!=0 and Common.ToDouble(self.tableData[countrow-1][index3])!=math.nan:
                    ilastflg=1
                    break
        if ilastflg==1:
            self.tableData.append(['','','','','','',''])
    
    def Refresh(self):
        if self.type==1:
            for index in range(len(self.tableData)-1):
                F=ErYuanZhuangZhi.CToK(Common.ToDouble(self.tableData[index][0]))
                G=ErYuanZhuangZhi.CToK(Common.ToDouble(self.tableData[index][1]))
                H=ErYuanZhuangZhi.CToK(Common.ToDouble(self.tableData[index][2]))
                K=Common.ToDouble(self.tableData[index][3])
                M=Common.ToDouble(self.tableData[index][4])
                N=Common.ToDouble(self.tableData[index][5])
                self.tableData[index][-1]=ErYuanZhuangZhi.CalQ(F,G,H,K,M,N)
        elif self.type==2:
            for index2 in range(len(self.tableData)-1):
                F=ErYuanZhuangZhi.CToK(Common.ToDouble(self.tableData[index2][0]))
                G=ErYuanZhuangZhi.CToK(Common.ToDouble(self.tableData[index2][1]))
                Q=Common.ToDouble(self.tableData[index2][2])
                K=Common.ToDouble(self.tableData[index2][3])
                M=Common.ToDouble(self.tableData[index2][4])
                N=Common.ToDouble(self.tableData[index2][5])
                self.tableData[index2][-1]=ErYuanZhuangZhi.Calh(F,G,Q,K,M,N)            



