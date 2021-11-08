# -*- encoding: utf-8 -*-
'''
2021/9/20 12:48 PM   tuchengen      1.0         None
--------------------------------------------------------
'''
import sys

from PyQt5.QtWidgets import QApplication, QWidget,  QVBoxLayout,  QTableWidget, QCheckBox, QHeaderView, QStyle, QStyleOptionButton, QTableWidgetItem
from PyQt5.QtCore import Qt, pyqtSignal, QRect
from PyQt5 import QtCore, QtGui, QtWidgets
from Subassembly import CheckBoxInTable,Ui_setbox
from Tools import ProductSelect
from res import picres_rc
import gl

# 表头字段，全局变量
header_field = ['全选', '序号', '产品名称', '产品代号', '截面形状', '厚度', '应用方式', '弯曲情况', '传热能力', '热流密度', '重量', '液塞', '孔数', '操作']
# 用来装行表头所有复选框 全局变量
all_header_combobox = []


class CheckBoxHeader(QHeaderView):
    """自定义表头类"""

    # 自定义 复选框全选信号
    select_all_clicked = pyqtSignal(bool)
    # 这4个变量控制列头复选框的样式，位置以及大小
    _x_offset = 0
    _y_offset = 0
    _width = 20
    _height = 20

    def __init__(self, orientation=Qt.Horizontal, parent=None):
        super(CheckBoxHeader, self).__init__(orientation, parent)
        self.isOn = False

    def paintSection(self, painter, rect, logicalIndex):
        painter.save()
        super(CheckBoxHeader, self).paintSection(painter, rect, logicalIndex)
        painter.restore()

        self._y_offset = int((rect.height() - self._width) / 2.)

        if logicalIndex == 0:
            option = QStyleOptionButton()
            option.rect = QRect(rect.x() + self._x_offset, rect.y() + self._y_offset, self._width, self._height)
            option.state = QStyle.State_Enabled | QStyle.State_Active
            if self.isOn:
                option.state |= QStyle.State_On
            else:
                option.state |= QStyle.State_Off
            self.style().drawControl(QStyle.CE_CheckBox, option, painter)

    def mousePressEvent(self, event):
        index = self.logicalIndexAt(event.pos())
        if 0 == index:
            x = self.sectionPosition(index)
            if x + self._x_offset < event.pos().x() < x + self._x_offset + self._width and self._y_offset < event.pos().y() < self._y_offset + self._height:
                if self.isOn:
                    self.isOn = False
                else:
                    self.isOn = True
                    # 当用户点击了行表头复选框，发射 自定义信号 select_all_clicked()
                self.select_all_clicked.emit(self.isOn)

                self.updateSection(0)
        super(CheckBoxHeader, self).mousePressEvent(event)

    # 自定义信号 select_all_clicked 的槽方法
    def change_state(self, isOn):
        # 如果行表头复选框为勾选状态
        if isOn:
            # 将所有的复选框都设为勾选状态
            for i in all_header_combobox:
                # i.Setstate(1)
                pass
                # i.setCheckState(Qt.Checked)
        else:
            for i in all_header_combobox:
                # i.Setstate(0)
                pass
                # i.setCheckState(Qt.Unchecked)


class TableDemo(QWidget):
    """窗口类"""
    mySignal = pyqtSignal(str,str,str)
    def __init__(self, parent = None):
        super(TableDemo, self).__init__(parent)
        self.shaixuanInfo=''
        #默认产品id排序
        self.sortProductid=[]
        self.initUI()

    # def __init__(self):
    #     super().__init__()
    #     self.initUI()

    def initUI(self):
        self.setWindowTitle('这是QTableWidget类行表头添加复选框全选功能')
        self.resize(1200*gl.w, 480*gl.h)

        # 垂直布局
        self.vlayout = QVBoxLayout(self)
        self.vlayout.setAlignment(Qt.AlignTop)  # 设置 垂直布局 的对齐方式
        self.setTableWidget()  # 设置表格

        self.show()

    # 设置表格
    def setTableWidget(self):
        # 表格控件
        # self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1200, 480))
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.verticalHeader().setVisible(False) 
        # sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())

        self.tablewidget = QTableWidget(0,14)        # 3行4列
        self.tablewidget.verticalHeader().setVisible(False)
        self.tablewidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tablewidget.sizePolicy().hasHeightForWidth())


        # self.tablewidget.setFixedWidth(300)         # 表格宽度
        self.setTableHeaderField()               # 设置表格行表头字段
        # self.tablewidget.setAlternatingRowColors(True)      # 交替行颜色
        self.vlayout.addWidget(self.tablewidget)

    # 设置行表头字段
    def setTableHeaderField(self):

        self.tablewidget.setColumnCount(len(header_field))   # 设置列数
        # for i in range(len(header_field)-1):
        #     header_item = QTableWidgetItem(header_field[i])

        #     checkbox = QCheckBox()
        #     # 将所有的复选框都添加到 全局变量 all_header_combobox 中
        #     all_header_combobox.append(checkbox)
        #     # 为每一行添加复选框
        #     self.tablewidget.setCellWidget(i,0,checkbox)

        header = CheckBoxHeader()               # 实例化自定义表头
        self.tablewidget.setHorizontalHeader(header)            # 设置表头
        self.tablewidget.setHorizontalHeaderLabels(header_field)        # 设置行表头字段
        self.tablewidget.setColumnWidth(0,50*gl.w)       # 设置第0列宽度
        self.tablewidget.setColumnWidth(1,85*gl.w);
        self.tablewidget.setColumnWidth(2,85*gl.w);
        self.tablewidget.setColumnWidth(3,85*gl.w);
        self.tablewidget.setColumnWidth(4,85*gl.w);
        self.tablewidget.setColumnWidth(5,85*gl.w);
        self.tablewidget.setColumnWidth(6,85*gl.w);
        self.tablewidget.setColumnWidth(7,85*gl.w);
        self.tablewidget.setColumnWidth(8,85*gl.w);
        self.tablewidget.setColumnWidth(9,85*gl.w);
        self.tablewidget.setColumnWidth(10,85*gl.w);
        self.tablewidget.setColumnWidth(11,85*gl.w);
        self.tablewidget.setColumnWidth(12,85*gl.w);
        self.tablewidget.setColumnWidth(13,85*gl.w);
        header.select_all_clicked.connect(self.headercheck)        # 行表头复选框单击信号与槽
    
    def headercheck(self,bool):
        if bool:
            for i in range(self.tablewidget.rowCount()):
                self.tablewidget.cellWidget(i,0).Setstate(1)
        else:
            for i in range(self.tablewidget.rowCount()):
                self.tablewidget.cellWidget(i,0).Setstate(0)
        
    # 设置表格内容，根据实际情况设置即可
    def setTableContents(self,oData,_shaixuanInfo):
        self.shaixuanInfo=_shaixuanInfo
        NewData=ProductSelect.sortProductList(self.shaixuanInfo,oData)
        if len(self.shaixuanInfo)<1:
            return
        dicshaixuanInfo=eval(self.shaixuanInfo)
        irow=len(NewData)
        self.tablewidget.setRowCount(irow)
        self.sortProductid=[]
        for row_number, row_data in enumerate(NewData):
            self.tablewidget.setRowHeight(row_number,40*gl.h)
            self.sortProductid.append(row_data["id"])
            checkbox = self.CheckBoxForRow(row_number)
            all_header_combobox.append(checkbox)
            self.tablewidget.setCellWidget(row_number,0,checkbox)
            # self.tablewidget.setCellWidget(row_number, 0, self.CheckBoxForRow(row_number))
            self.tablewidget.setItem(row_number, 1, QtWidgets.QTableWidgetItem(str(row_number+1)))
            item=QtWidgets.QLabel()
            item.setText(str(row_data['name']))
            self.tablewidget.setCellWidget(row_number,2,item)
            # self.tablewidget.setItem(row_number, 2, QtWidgets.QTableWidgetItem(str(row_data["name"])))
            self.tablewidget.setItem(row_number, 3, QtWidgets.QTableWidgetItem(str(row_data["code"])))
            # icon = QtGui.QIcon()
            shapicon=":/product/"+str(row_data["ishape"])+".ico"
            item=QtWidgets.QLabel()
            # item.setStyleSheet("text-align : center;")
            item.setAlignment(Qt.AlignCenter)
            item.setPixmap(QtGui.QPixmap(shapicon).scaled(40*gl.w, 40*gl.h))
            
            self.tablewidget.setCellWidget(row_number,4,item)
        #     self.ReRanpic = QtWidgets.QLabel(self)
        # self.ReRanpic.setGeometry(QtCore.QRect(0, 530, 1100, 500))
        # self.ReRanpic.setText("")
        # self.ReRanpic.setPixmap(QtGui.QPixmap(":/SingleRe/SingleRe.png"))
        # self.ReRanpic.setObjectName("label")
            # self.tablewidget.setItem(row_number, 4, QtWidgets.QTableWidgetItem(str(row_data["ishape"])))
            item=QtWidgets.QLabel()
            item.setText(str(row_data['thickness']))
            if row_data['thickness']-float(dicshaixuanInfo["thickness"])<1e-6:
                item.setStyleSheet("color: rgb(255, 0, 0);")
            self.tablewidget.setCellWidget(row_number,5,item)
            # self.tablewidget.setItem(row_number, 5, QtWidgets.QTableWidgetItem(str(row_data["thickness"])))
            item=QtWidgets.QLabel()
            item.setText(row_data['apptyle'])
            if dicshaixuanInfo["type"] not in row_data['apptyle']:
                item.setStyleSheet("color: rgb(255, 0, 0);")
            self.tablewidget.setCellWidget(row_number,6,item)
            # self.tablewidget.setItem(row_number, 6, QtWidgets.QTableWidgetItem(str(row_data["apptyle"])))
            item=QtWidgets.QLabel()
            item.setText(row_data['wanqu'])
            # print(dicshaixuanInfo["wanqunum"],row_data['wanqu'])
            if (dicshaixuanInfo["wanqunum"]<1 and row_data['wanqu']=="可弯曲") or (dicshaixuanInfo["wanqunum"]>0 and ("不可弯曲" in row_data['wanqu']) ):
                item.setStyleSheet("color: rgb(255, 0, 0);")
            # if dicshaixuanInfo["wanqunum"]>0 and "不可弯曲" in row_data['wanqu']:
            #     item.setStyleSheet("color: rgb(255, 0, 0);")
            # if dicshaixuanInfo["wanqunum"]==0 and row_data['wanqu']=="可弯曲":
            #     item.setStyleSheet("color: rgb(255, 0, 0);")
            self.tablewidget.setCellWidget(row_number,7,item)
            # self.tablewidget.setItem(row_number, 7, QtWidgets.QTableWidgetItem(str(row_data["wanqu"])))
            # if item['prtkong20']-CalTotalgonglv(selectData)<1e-6:
            #     unsuitablelist.append(item)
            # continue
            item=QtWidgets.QLabel()
            item.setText(str(row_data['prtkong20']))
            if row_data['prtkong20']-ProductSelect.CalTotalgonglv(self.shaixuanInfo)<1e-6:
                # print(row_data['prtkong20'],ProductSelect.CalTotalgonglv(self.shaixuanInfo))
                item.setStyleSheet("color: rgb(255, 0, 0);")
            self.tablewidget.setCellWidget(row_number,8,item)
            # self.tablewidget.setItem(row_number, 8, QtWidgets.QTableWidgetItem(str(row_data["prtkong20"])))
            self.tablewidget.setItem(row_number, 9, QtWidgets.QTableWidgetItem(str(row_data["midulinjie20"])))
            item=QtWidgets.QLabel()
            item.setText(self.GetWeight(row_data["midulinjie20"]))
            if row_data['midulinjie20']*ProductSelect.GetL(self.shaixuanInfo)-float(dicshaixuanInfo["weight"])>1e-6:
                item.setStyleSheet("color: rgb(255, 0, 0);")
            self.tablewidget.setCellWidget(row_number,10,item)
            # self.tablewidget.setItem(row_number, 10, QtWidgets.QTableWidgetItem(self.GetWeight(row_data["midulinjie20"])))
            item=QtWidgets.QLabel()
            str1=self.CalYeSai(self.shaixuanInfo,row_data["id"])
            if "突显" in str1:
                str2 = str1.replace('突显','')
                item.setStyleSheet("color: rgb(255, 0, 0);")
                # item.setFont(QtGui.QFont(14, QtGui.QFont.Red))
                item.setText(str2)
                
            elif "失效" in str1:
                item.setStyleSheet("color: rgb(255, 0, 0);")
                item.setText(str1)
            else:
                item.setText(str1)
            self.tablewidget.setCellWidget(row_number,11,item)
            # self.tablewidget.setItem(row_number, 11, QtWidgets.QTableWidgetItem(self.CalYeSai(self.shaixuanInfo,row_data["id"])))
            self.tablewidget.setItem(row_number, 12, QtWidgets.QTableWidgetItem(str(row_data["kongnum"])))
            self.tablewidget.setCellWidget(row_number, 13, self.buttonForRow(row_data["id"]))
    
    def CheckBoxForRow(self,num):
        addBtn=CheckBoxInTable.MyCheckBox()
        addBtn.getidfromfather(num)
        addBtn.mySignal.connect(self.getcheckboxSignal)
        return addBtn
    
    def getcheckboxSignal(self,str1,str2):
        print(str1,str2)
    
      #计算重量，当用户为点击筛选的时候无法获取长度 为空
    def GetWeight(self,vapordensity):
        if len(self.shaixuanInfo)==0:
            return str(0.00)
        else:
            dicshaixuanInfo=eval(self.shaixuanInfo)
            # lis=[]
            # for item in dicshaixuanInfo["tabledata"]:
            #     lis.append(item["juli"])
            # rongcha=float(dicshaixuanInfo["rongcha"])
            l=self.GetL()
            return str(vapordensity*l)
    #获取热管总长
    def GetL(self):
        if len(self.shaixuanInfo)==0:
            return 0.0
        else:
            dicshaixuanInfo=eval(self.shaixuanInfo)
            lis=[]
            for item in dicshaixuanInfo["tabledata"]:
                lis.append(item["juli"])
            l=max(lis)
            l=l+self.GetRongCha()
            return l
    #获取液塞容差
    def GetRongCha(self):
        if len(self.shaixuanInfo)==0:
            return 0.0
        else:
            dicshaixuanInfo=eval(self.shaixuanInfo)
            return float(dicshaixuanInfo["rongcha"])
    
    #计算产品表格中的液塞
    def CalYeSai(self,shaixuanInfo,productid):
        lenght=self.GetL()
        lenght1=self.GetRongCha()
        return ProductSelect.CalYeSaiByid(shaixuanInfo,productid,lenght,lenght1)
    
    #查看液塞按钮
    def buttonForRow(self,id):
        widget=QtWidgets.QWidget()
        addBtn = QtWidgets.QPushButton('查看液塞')
        addBtn.setStyleSheet(''' text-align : center;
                                  background-color : NavajoWhite;
                                  height : 30px;
                                  border-style: outset;
                                  font : 13px; ''')

        addBtn.clicked.connect(lambda: self.lookYeSai(id))
        hLayout = QtWidgets.QHBoxLayout()
        # hLayout.addWidget(updateBtn)
        hLayout.addWidget(addBtn)
        hLayout.setContentsMargins(5,2,5,2)
        widget.setLayout(hLayout)
        return widget
    
    #查看液塞按钮
    def lookYeSai(self,id):
        if hasattr(self,"ChartView"):
            self.ChartView.close()
        else:
            pass
        if hasattr(self,"ReRanpic"):
            self.ReRanpic.close()
        else:
            pass
        if hasattr(self,"settemp"):
            self.settemp.close()
        else:
            pass
        if hasattr(self,"settemplabel"):
            self.settemplabel.close()
        else:
            pass
        my = Ui_setbox.MyDialog(self)
        my.SetProductID(id)
        my.SetChongZhuangTemp(eval(self.shaixuanInfo)["edingtemp"])
        # 在主窗口中连接信号和槽
        my.mySignal.connect(self.getDialogSignal)
        my.exec_()
    
    def getDialogSignal(self, connect):
        dic=eval(connect)
        CalYeSaiData={}
        if len(self.shaixuanInfo)==0:
            #提示 为点击筛选
            MsgBox=QtWidgets.QMessageBox(QtWidgets.QMessageBox.Warning, '提示', '还未进行筛选操作!')
            MsgBox.setGeometry(QtCore.QRect(1000*gl.w, 500*gl.h, 500*gl.w, 500*gl.h))
            MsgBox.exec_()
            pass
        else:
            dicshaixuanInfo=eval(self.shaixuanInfo)
            CalYeSaiData['hightemp']=dicshaixuanInfo['hightemp']#最高工作温度
            CalYeSaiData['lowtemp']=dicshaixuanInfo['lowtemp']#最低工作温度
            CalYeSaiData['edingtemp']=dicshaixuanInfo['edingtemp']#额定工作温度
            CalYeSaiData['iempjiange']=dic['iempjiange']#温度间隔
            CalYeSaiData['chongzhuangtemp']=dic['tempeding']#额定充装温度
            CalYeSaiData['chongzhuangtempup']=dic['tempup']#充装温度上限
            CalYeSaiData['chongzhuangtempdn']=dic['tempdn']#充装温度下线
            CalYeSaiData['productid']=dic['productid']#产品id
            # a = list(range(float(CalYeSaiData['hightemp']), float(CalYeSaiData['lowtemp']), float(CalYeSaiData['iempjiange'])))
            Rowtitle = list(range(int(float(CalYeSaiData['lowtemp'])), int(float(CalYeSaiData['hightemp'])), 5))#int(float(CalYeSaiData['iempjiange']))))
            #range 是开区间 需要补齐最后一个数
            Rowtitle.append(int(float(CalYeSaiData['hightemp'])))
            if int(float(CalYeSaiData['edingtemp'])) in Rowtitle:
                pass
            else:
                Rowtitle.append(int(float(CalYeSaiData['edingtemp'])))
            Rowtitle.sort()
            # coltitle=list()
            # coltitle.append(float(CalYeSaiData['chongzhuangtempdn']))
            # coltitle.append(float(CalYeSaiData['chongzhuangtemp']))
            # coltitle.append(float(CalYeSaiData['chongzhuangtempup']))
            coltitle = list(range(int(float(CalYeSaiData['chongzhuangtempdn'])), int(float(CalYeSaiData['chongzhuangtempup'])), int(float(CalYeSaiData['iempjiange']))))
            coltitle.append(int(float(CalYeSaiData['chongzhuangtempup'])))
            #  
            self.mySignal.emit(str(CalYeSaiData),str(Rowtitle),str(coltitle))
    #获取选中状态
    def GetCheckedState(self):
        result=[]
        CheckStatelist=[]
        for i in range(self.tablewidget.rowCount()):
            CheckStatelist.append(self.tablewidget.cellWidget(i,0).GetChecked())
        if len(CheckStatelist)==len(self.sortProductid):
            for j in range(len(CheckStatelist)):
                item={}
                item["checkstate"]=CheckStatelist[j]
                item["productid"]=self.sortProductid[j]
                result.append(item)
            return result
        else:
            return result
    
