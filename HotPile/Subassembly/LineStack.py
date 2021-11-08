#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Created on 2017年12月28日
@author: Irony
@site: https://pyqt.site , https://github.com/PyQt5
@email: 892768447@qq.com
@file: charts.line.LineStack
@description: like http://echarts.baidu.com/demo.html#line-stack
"""

import sys

try:
    from PyQt5.QtChart import QChartView, QChart, QLineSeries, QLegend, \
        QCategoryAxis
    from PyQt5.QtCore import Qt, QPointF, QRectF, QPoint
    from PyQt5.QtGui import QPainter, QPen
    from PyQt5.QtWidgets import QApplication, QGraphicsLineItem, QWidget, \
        QHBoxLayout, QLabel, QVBoxLayout, QGraphicsProxyWidget
except ImportError:
    from PySide2.QtCore import Qt, QPointF, QRectF, QPoint
    from PySide2.QtGui import QPainter, QPen
    from PySide2.QtWidgets import QApplication, QGraphicsLineItem, QWidget, \
        QHBoxLayout, QLabel, QVBoxLayout, QGraphicsProxyWidget
    from PySide2.QtCharts import QtCharts

    QChartView = QtCharts.QChartView
    QChart = QtCharts.QChart
    QLineSeries = QtCharts.QLineSeries
    QLegend = QtCharts.QLegend
    QCategoryAxis = QtCharts.QCategoryAxis


class ToolTipItem(QWidget):

    def __init__(self, color, text, parent=None):
        super(ToolTipItem, self).__init__(parent)
        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        clabel = QLabel(self)
        clabel.setMinimumSize(12, 12)
        clabel.setMaximumSize(12, 12)
        clabel.setStyleSheet("border-radius:6px;background: rgba(%s,%s,%s,%s);" % (
            color.red(), color.green(), color.blue(), color.alpha()))
        layout.addWidget(clabel)
        self.textLabel = QLabel(text, self, styleSheet="color:white;")
        layout.addWidget(self.textLabel)

    def setText(self, text):
        self.textLabel.setText(text)


class ToolTipWidget(QWidget):
    Cache = {}

    def __init__(self, *args, **kwargs):
        super(ToolTipWidget, self).__init__(*args, **kwargs)
        self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet(
            "ToolTipWidget{background: rgba(50, 50, 50, 100);}")
        layout = QVBoxLayout(self)
        self.titleLabel = QLabel(self, styleSheet="color:white;")
        layout.addWidget(self.titleLabel)

    def updateUi(self, title, points):
        self.titleLabel.setText(title)
        for serie, point in points:
            if serie not in self.Cache:
                item = ToolTipItem(
                    serie.color(),
                    (serie.name() or "-") + ":" + str(point.y()), self)
                self.layout().addWidget(item)
                self.Cache[serie] = item
            else:
                self.Cache[serie].setText(
                    (serie.name() or "-") + ":" + str(point.y()))
            self.Cache[serie].setVisible(serie.isVisible())  # 隐藏那些不可用的项
        self.adjustSize()  # 调整大小


class GraphicsProxyWidget(QGraphicsProxyWidget):

    def __init__(self, *args, **kwargs):
        super(GraphicsProxyWidget, self).__init__(*args, **kwargs)
        self.setZValue(999)
        self.tipWidget = ToolTipWidget()
        self.setWidget(self.tipWidget)
        self.hide()

    def width(self):
        return self.size().width()

    def height(self):
        return self.size().height()

    def show(self, title, points, pos):
        self.setGeometry(QRectF(pos, self.size()))
        self.tipWidget.updateUi(title, points)
        super(GraphicsProxyWidget, self).show()


class ChartView(QChartView):

    def __init__(self, *args, **kwargs):
        super(ChartView, self).__init__(*args, **kwargs)
        self.resize(800, 600)
        self.setRenderHint(QPainter.Antialiasing)  # 抗锯齿
        # 自定义x轴label
        # self.category = ["10℃", "15℃", "20℃", "25℃", "30℃", "35℃", "40℃"]
        self.SetData({})
        self.DrawChart()



    #      if oData:
    #             self.category=oData["category"]
    #         self.title=oData["title"]
    #         self.dataTable=oData["dataTable"]
    #         self.XTickCount=oData["XTickCount"]
    #         self.YTickCount=oData["YTickCount"]
    #         self.YRangeMax=oData["YRangeMax"]
    #         self.YRangeMin=oData["YRangeMin"]
    #     else:
    #         self.InitData()
    
    # def InitData(self):
    #     self.category=["10℃", "15℃", "20℃", "25℃", "30℃", "35℃", "40℃"]
    #     self.title=""
    #     self.dataTable=[
    #         ["产品1", [-10, 12, 14, 16, 18, 20, 22]],
    #         ["产品2", [22, 18.2, 19.1, 23.4, 29.0, 33.0, 31.0]],
    #         ["产品3", [15.0, 23.2, 20.1, 15.4, 19.0, 33.0, 41.0]],
    #         ["产品4", [32.0, 33.2, 30.1, 33.4, 39.0, 33.0, 32.0]],
    #         ["产品5", [82.0, 93.2, 90.1, 93.4, 129.0, 133.0, 132.0]]
    #     ]
    #     self.XTickCount=7
    #     self.YTickCount=7
    #     self.YRangeMax=100
    #     self.YRangeMin=-100
        # tempData={}
        # tempData["category"]=["fd", "gd", "gdfg", "dfg", "ete", "re3", "twtrw"]
        # tempData["title"]="sdgsdgdsg"
        # tempData["dataTable"]=[
        #     ["ger", [-10, 12, 14, 16, 18, 20, 22]],
        #     ["et", [22, 18.2, 19.1, 23.4, 29.0, 33.0, 31.0]],
        #     ["64", [15.0, 23.2, 20.1, 15.4, 19.0, 33.0, 41.0]],
        #     ["364", [32.0, 33.2, 30.1, 33.4, 39.0, 33.0, 32.0]],
        #     ["366", [82.0, 93.2, 90.1, 93.4, 129.0, 133.0, 132.0]]
        # ]
        # tempData["XTickCount"]=7
        # tempData["YTickCount"]=7
        # tempData["YRangeMax"]=100
        # tempData["YRangeMin"]=-100




        # self.SetData(tempData)
        # self.DrawChart()

        # # 提示widget
        # self.toolTipWidget = GraphicsProxyWidget(self._chart)

        # # line
        # self.lineItem = QGraphicsLineItem(self._chart)
        # pen = QPen(Qt.gray)
        # pen.setWidth(1)
        # self.lineItem.setPen(pen)
        # self.lineItem.setZValue(998)
        # self.lineItem.hide()

        # # 一些固定计算，减少mouseMoveEvent中的计算量
        # # 获取x和y轴的最小最大值
        # axisX, axisY = self._chart.axisX(), self._chart.axisY()
        # self.min_x, self.max_x = axisX.min(), axisX.max()
        # self.min_y, self.max_y = axisY.min(), axisY.max()

    def resizeEvent(self, event):
        super(ChartView, self).resizeEvent(event)
        # 当窗口大小改变时需要重新计算
        # 坐标系中左上角顶点
        self.point_top = self._chart.mapToPosition(
            QPointF(self.min_x, self.max_y))
        # 坐标原点坐标
        self.point_bottom = self._chart.mapToPosition(
            QPointF(self.min_x, self.min_y))
        self.step_x = (self.max_x - self.min_x) / \
                      (self._chart.axisX().tickCount() - 1)

    def mouseMoveEvent(self, event):
        super(ChartView, self).mouseMoveEvent(event)
        pos = event.pos()
        # 把鼠标位置所在点转换为对应的xy值
        x = self._chart.mapToValue(pos).x()
        y = self._chart.mapToValue(pos).y()
        index = round((x - self.min_x) / self.step_x)
        # 得到在坐标系中的所有正常显示的series的类型和点
        points = [(serie, serie.at(index))
                  for serie in self._chart.series()
                  if self.min_x <= x <= self.max_x and
                  self.min_y <= y <= self.max_y]
        if points:
            pos_x = self._chart.mapToPosition(
                QPointF(index * self.step_x + self.min_x, self.min_y))
            self.lineItem.setLine(pos_x.x(), self.point_top.y(),
                                  pos_x.x(), self.point_bottom.y())
            self.lineItem.show()
            try:
                title = self.category[index]
            except:
                title = ""
            t_width = self.toolTipWidget.width()
            t_height = self.toolTipWidget.height()
            # 如果鼠标位置离右侧的距离小于tip宽度
            x = pos.x() - t_width if self.width() - \
                                     pos.x() - 20 < t_width else pos.x()
            # 如果鼠标位置离底部的高度小于tip高度
            y = pos.y() - t_height if self.height() - \
                                      pos.y() - 20 < t_height else pos.y()
            self.toolTipWidget.show(
                title, points, QPoint(x, y))
        else:
            self.toolTipWidget.hide()
            self.lineItem.hide()

    def handleMarkerClicked(self):
        marker = self.sender()  # 信号发送者
        if not marker:
            return
        visible = not marker.series().isVisible()
        #         # 隐藏或显示series
        marker.series().setVisible(visible)
        marker.setVisible(True)  # 要保证marker一直显示
        # 透明度
        alpha = 1.0 if visible else 0.4
        # 设置label的透明度
        brush = marker.labelBrush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setLabelBrush(brush)
        # 设置marker的透明度
        brush = marker.brush()
        color = brush.color()
        color.setAlphaF(alpha)
        brush.setColor(color)
        marker.setBrush(brush)
        # 设置画笔透明度
        pen = marker.pen()
        color = pen.color()
        color.setAlphaF(alpha)
        pen.setColor(color)
        marker.setPen(pen)

    def handleMarkerHovered(self, status):
        # 设置series的画笔宽度
        marker = self.sender()  # 信号发送者
        if not marker:
            return
        series = marker.series()
        if not series:
            return
        pen = series.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if status else -1))
        series.setPen(pen)

    def handleSeriesHoverd(self, point, state):
        # 设置series的画笔宽度
        series = self.sender()  # 信号发送者
        pen = series.pen()
        if not pen:
            return
        pen.setWidth(pen.width() + (1 if state else -1))
        series.setPen(pen)

    def initChart(self):
        self._chart = QChart(title=self.title)
        self._chart.setAcceptHoverEvents(True)
        # Series动画
        self._chart.setAnimationOptions(QChart.SeriesAnimations)
        # dataTable = [
        #     ["产品1", [-10, 12, 14, 16, 18, 20, 22]],
        #     ["产品2", [22, 18.2, 19.1, 23.4, 29.0, 33.0, 31.0]],
        #     ["产品3", [15.0, 23.2, 20.1, 15.4, 19.0, 33.0, 41.0]],
        #     ["产品4", [32.0, 33.2, 30.1, 33.4, 39.0, 33.0, 32.0]],
        #     ["产品5", [82.0, 93.2, 90.1, 93.4, 129.0, 133.0, 132.0]]
        # ]
        dataTable=self.dataTable
        for series_name, data_list in dataTable:
            series = QLineSeries(self._chart)
            for j, v in enumerate(data_list):
                series.append(j, v)
            series.setName(series_name)
            series.setPointsVisible(True)  # 显示圆点
            series.hovered.connect(self.handleSeriesHoverd)  # 鼠标悬停
            self._chart.addSeries(series)
        self._chart.createDefaultAxes()  # 创建默认的轴
        axisX = self._chart.axisX()  # x轴
        axisX.setTickCount(self.XTickCount)  # x轴设置7个刻度
        axisX.setGridLineVisible(False)  # 隐藏从x轴往上的线条
        axisY = self._chart.axisY()
        axisY.setTickCount(self.YTickCount)  # y轴设置7个刻度
        axisY.setTitleText("液塞")
        axisY.setRange(self.YRangeMin, self.YRangeMax)  # 设置y轴范围
        # 自定义x轴
        axis_x = QCategoryAxis(
            self._chart, labelsPosition=QCategoryAxis.AxisLabelsPositionOnValue)
        axis_x.setTickCount(self.XTickCount)
        axis_x.setGridLineVisible(False)
        axis_x.setTitleText("工作温度")
        min_x = axisX.min()
        max_x = axisX.max()
        step = (max_x - min_x) / (self.XTickCount - 1)  # 7个tick
        for i in range(0, self.XTickCount):
            axis_x.append(self.category[i], min_x + i * step)
        self._chart.setAxisX(axis_x, self._chart.series()[-1])
        # chart的图例
        legend = self._chart.legend()
        # 设置图例由Series来决定样式
        legend.setMarkerShape(QLegend.MarkerShapeFromSeries)
        # 遍历图例上的标记并绑定信号
        for marker in legend.markers():
            # 点击事件
            marker.clicked.connect(self.handleMarkerClicked)
            # 鼠标悬停事件
            marker.hovered.connect(self.handleMarkerHovered)
        self.setChart(self._chart)
    
    def SetData(self,oData={}):
        #self.category = ["10℃", "15℃", "20℃", "25℃", "30℃", "35℃", "40℃"]
        if oData:
            self.category=oData["category"]
            self.title=oData["title"]
            self.dataTable=oData["dataTable"]
            self.XTickCount=oData["XTickCount"]
            self.YTickCount=oData["YTickCount"]
            self.YRangeMax=oData["YRangeMax"]
            self.YRangeMin=oData["YRangeMin"]
        else:
            self.InitData()
    
    def InitData(self):
        self.category=["10℃", "15℃", "20℃", "25℃", "30℃", "35℃", "40℃"]
        self.title="示例数据"
        self.dataTable=[
            ["产品1", [1, 1, 1, 1, 1, 1, 1]],
            ["产品2", [1, 1, 1, 1, 1, 1, 1]],
            ["产品3", [1, 1, 1, 1, 1, 1, 1]],
            ["产品4", [1, 1, 1, 1, 1, 1, 1]],
            ["产品5", [1, 1, 1, 1, 1, 1, 1]]
        ]
        self.XTickCount=7
        self.YTickCount=7
        self.YRangeMax=10
        self.YRangeMin=-10
    
    def DrawChart(self):
        self.initChart()
        # 提示widget
        self.toolTipWidget = GraphicsProxyWidget(self._chart)
        # line
        self.lineItem = QGraphicsLineItem(self._chart)
        pen = QPen(Qt.gray)
        pen.setWidth(1)
        self.lineItem.setPen(pen)
        self.lineItem.setZValue(998)
        self.lineItem.hide()

        # 一些固定计算，减少mouseMoveEvent中的计算量
        # 获取x和y轴的最小最大值
        axisX, axisY = self._chart.axisX(), self._chart.axisY()
        self.min_x, self.max_x = axisX.min(), axisX.max()
        self.min_y, self.max_y = axisY.min(), axisY.max()




        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = ChartView()
    view.show()
    sys.exit(app.exec_())
