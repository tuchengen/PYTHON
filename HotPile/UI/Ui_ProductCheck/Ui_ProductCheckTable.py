# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\HotPile\ProductCheckTable.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ProductCheckTable(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1118, 896)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(9, 9, 1100, 436))
        self.widget.setMaximumSize(QtCore.QSize(16777215, 500))
        self.widget.setObjectName("widget")
        self.tableWidget = QtWidgets.QTableWidget(self.widget)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 1101, 881))
        self.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setObjectName("tableWidget")
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
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setMinimumSectionSize(50)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(460, 470, 75, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
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
        self.pushButton.setText(_translate("Form", "导出数据"))
