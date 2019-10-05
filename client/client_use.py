from UI.presentation_layer import Ui_Dialog
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox, QInputDialog, QLineEdit
from PyQt5.Qt import QPointF
from PyQt5 import QtCore, QtGui
import os
import json
from PyQt5.QtChart import *
from socket import *
import datetime


class Client(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(Client,self).__init__(parent)
        self.setupUi(self)

        # 控制无边窗口移动
        self.m_flag = None
        self.m_Position = None
        # 设置窗体无边框
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        # UDP通信
        self.socket = None
        self.targetIP = None
        self.targetPort = None
        self.bufferSize = None
        self.quire_item = None

        self.startYear = None
        self.startMonth = None
        self.startDay = None

        self.endYear = None
        self.endMonth = None
        self.endDay = None
        # 存储查询的数据以及其相应的时期
        self.date = []
        self.data = []

        self.init()

    def init(self):
        filename = os.path.dirname(os.getcwd()) + '/resources/config.json'
        configJson = None
        if os.path.exists(filename):
            with open(filename) as f:
                configJson = json.load(f)
            print(configJson)
            print(type(configJson))
        if "Host" in configJson and "Port" in configJson and "BufferSize" in configJson:
            self.targetIP = configJson["Host"]
            self.targetPort = int(configJson["Port"])
            self.bufferSize = int(configJson["BufferSize"])

        self.socket = socket(AF_INET, SOCK_DGRAM)

        # 以下三个函数用于控制无边框的窗口移动
        # --------------------------------------------------------------------------------
        # 重载鼠标按压事件

    def mousePressEvent(self, *args, **kwargs):
        event = args[0]
        if event.button() == QtCore.Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))  # 更改鼠标图标

        # 重载鼠标移动事件

    def mouseMoveEvent(self, *args, **kwargs):
        QMouseEvent = args[0]
        if QtCore.Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

        # 重载鼠标释放事件

    def mouseReleaseEvent(self, *args, **kwargs):
        self.m_flag = False
        self.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
    # --------------------------------------------------------------------------------

    def inquire(self):

        self.showLabel.clear()
        self.showLabel.setText("From {}-{}-{} to {}-{}-{}".format(self.startYear, self.startMonth, self.startDay,
                                                                  self.endYear, self.endMonth, self.endDay))

        if self.commitBtn.isEnabled():
            QMessageBox.warning(self, "WARNING", "Please click the commit button first!", QMessageBox.Ok)
            return
        # 进度条设置可用
        self.progressBar.setEnabled(True)
        self.progressBar.setValue(0)
        if not self.quire_item:
            if self.tradingVolumeCheckBox.isChecked():
                self.quire_item = 1
            elif self.marketMoneyCheckBox.isChecked():
                self.quire_item = 2
            elif self.topValueCheckBox.isChecked():
                self.quire_item = 3
            elif self.minValueCheckBox.isChecked():
                self.quire_item = 4
        self.progressBar.setValue(10)
        if not self.quire_item:
            QMessageBox.warning(self, "WARNING", "You Must Select one item to quire!", QMessageBox.Ok)
            return
        data = "{}&{}/{}/{}&{}/{}/{}".format(str(self.quire_item), str(self.startYear), str(self.startMonth),
                                             str(self.startDay), str(self.endYear), str(self.endMonth), str(self.endDay))
        data = data.encode()
        self.progressBar.setValue(20)
        self.socket.sendto(data, (self.targetIP, self.targetPort))
        data, addr = self.socket.recvfrom(self.bufferSize)
        self.progressBar.setValue(50)

        if not data:
            QMessageBox.information(self, "Tip", "There does\'t exist the data you want!", QMessageBox.Ok)
            self.progressBar.setValue(100)
        else:
            data = json.loads(data.decode())
            print(data)
            # 对数据进行分解
            # 分解日期
            self.date = [datetime.datetime.strptime(x.split("&")[0], "%Y-%m-%d").date() for x in data]
            print(self.date)
            # 分解数据
            self.data = [x.split("&")[1] for x in data]
            # 字符串列表转换为float1列表
            self.data = [float(x) for x in self.data]
            print(self.data)

            self.progressBar.setValue(70)

            pointlist, maxitem, minitem = self.format_data(self.data)

            self.progressBar.setValue(80)

            self.paint(self.quire_item, pointlist, maxitem, minitem)

            self.progressBar.setValue(100)

            self.toolsCombox.setEnabled(True)
            self.quire_item = None

    @staticmethod
    def format_data(data):
        pointlist = []
        index = 0
        minitem = 0
        maxitem = 0
        for item in data:
            if item > maxitem:
                maxitem = item
            if item < minitem:
                minitem = item
            pointlist.append(QPointF(index, item))
            index += 1
        return pointlist, maxitem, minitem

    def paint(self, code: int, pointlist: list, minitem: int, maxitem: int):
        series = QLineSeries()
        series.append(pointlist)
        series.setName("折线一")
        if code == 1:
            title_name = '一段时间内成交金额的变化曲线图'
        elif code == 2:
            title_name = '一段时间内市值的变化曲线图'
        elif code == 3:
            title_name = '一段时间内最高价的变化曲线图'
        elif code == 4:
            title_name = '一段时间内最低价的变化曲线图'
        elif code == 5:
            title_name = '一段时间内涨跌的变化'
        x_aix = QValueAxis()
        x_aix.setRange(0.0, len(pointlist))
        x_aix.setLabelFormat("%0.1f")
        x_aix.setTickCount(100)
        x_aix.setMinorTickCount(0)  # 设置每个单元格有几个小的分级

        y_aix = QValueAxis()  # 定义y轴
        y_aix.setRange(minitem, maxitem)
        y_aix.setLabelFormat("%0.1f")
        y_aix.setTickCount(100)
        y_aix.setMinorTickCount(0)

        chartview = QChartView(self.frame)
        chartview.setGeometry(0, 0, self.frame.width(), self.frame.height())
        chartview.chart().addSeries(series)
        chartview.chart().setAxisX(x_aix)
        chartview.chart().setAxisY(y_aix)
        chartview.chart().createDefaultAxes()
        chartview.chart().setTitleBrush(QtGui.QBrush(QtCore.Qt.cyan))
        chartview.chart().setTitle(title_name)
        chartview.show()

    def closeWindow(self):
        exit(0)

    def checkBoxCommit(self):
        self.startYear = int(self.up_year_combox.currentText())
        self.startMonth = int(self.up_month_combox.currentText())
        self.startDay = int(self.up_day_combox.currentText())
        self.endYear = int(self.down_year_combox.currentText())
        self.endMonth = int(self.down_month_combox.currentText())
        self.endDay = int(self.down_day_combox.currentText())
        errorTurple = [(4, 31), (6, 31), (9, 31), (11, 31)]
        if self.startYear > self.endYear:
            QMessageBox.warning(self, "WARNING", 'The Start Date must be less than the End Date!', QMessageBox.Ok)
            return
        if (self.startMonth, self.startDay) in errorTurple or (self.endMonth, self.endDay) in errorTurple:
            QMessageBox.warning(self, "WARNING", 'The month you chose doesn\'t exist 31st!', QMessageBox.Ok)
            return
        if (self.startMonth == 2 and self.startDay > 28) or (self.endMonth == 2 and self.endDay > 28):
            QMessageBox.warning(self, "WARNING", 'February doesn\'t exist the day you chose', QMessageBox.Ok)
            return
        self.commitBtn.setEnabled(False)
        self.up_year_combox.setEnabled(False)
        self.up_month_combox.setEnabled(False)
        self.up_day_combox.setEnabled(False)
        self.down_year_combox.setEnabled(False)
        self.down_month_combox.setEnabled(False)
        self.down_day_combox.setEnabled(False)
        pass

    def checkBoxChanged(self):
        self.commitBtn.setEnabled(True)
        self.up_year_combox.setEnabled(True)
        self.up_month_combox.setEnabled(True)
        self.up_day_combox.setEnabled(True)
        self.down_year_combox.setEnabled(True)
        self.down_month_combox.setEnabled(True)
        self.down_day_combox.setEnabled(True)

    def executeFun(self, index: int):
        if index == 0:
            self.search_data()
        elif index == 1:
            self.calcluate()

    def search_data(self):

        search_date, isok = QInputDialog.getText(self, "查询", "请输入需要查询的日期(年月日用\'-\'分割)",
                                                 QLineEdit.Normal, "")
        if isok:
            search_date = datetime.datetime.strptime(search_date, "%Y-%m-%d").date()
            if search_date in self.date:
                index = self.date.index(search_date)
                out_data = self.data[index]
                QMessageBox.information(self, "结果", "查询结果为：{}".format(str(out_data)), QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "WARNING", "你所选的时间无数据！", QMessageBox.Ok)

    def calcluate(self):
        self.quire_item = 5
        self.inquire()
        calc_date, isok = QInputDialog.getText(self, "计算上证指数", "请输入需要计算上证指数的日期(年月日用\'-\'分割)",
                                   QLineEdit.Normal, "")
        calc_date = datetime.datetime.strptime(calc_date, "%Y-%m-%d").date()
        if isok:
            num = 100  # 起始上证指数为100
            riseAndFallNumberList = []
            index = 0
            for rate in self.data:
                if index == 0:
                    riseAndFallNumberList.append(num)  # 第一个数直接装入列表
                    index += 1
                    continue
                num = num*(1+rate)
                riseAndFallNumberList.append(num)
                index += 1

            if calc_date in self.date:
                index = self.date.index(calc_date)
                curNum = riseAndFallNumberList[index]
                QMessageBox.information(self, "Information", "{}的上证指数为：{}".format(calc_date.strftime("%Y-%m-%d"),
                                                                                  str(curNum)), QMessageBox.Ok)
            else:
                QMessageBox.warning(self, "WARNING", "你选的那天没有上证指数！", QMessageBox.Ok)
                return


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    myWin = Client()
    myWin.exec()
    sys.exit(app.exec_())
