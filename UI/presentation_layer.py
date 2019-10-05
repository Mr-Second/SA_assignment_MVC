# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'presentation_layer.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from resources import myIcons_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(835, 508)
        Dialog.setWindowOpacity(0.9)
        Dialog.setStyleSheet("QCheckBox{\n"
"    color: rgb(0, 0, 0);\n"
"    font: 14pt \"华文楷体\";\n"
"}\n"
"QCheckBox::indicator{\n"
"    width: 25px;\n"
"    height: 25px;\n"
"}\n"
"QCheckBox::indicator:unchecked{\n"
"    \n"
"    border-image: url(:/Unchecked.png);\n"
"}\n"
"QCheckBox::indicator:checked{\n"
"    \n"
"    border-image: url(:/Check.png);\n"
"}\n"
"")
        self.topLabel = QtWidgets.QLabel(Dialog)
        self.topLabel.setGeometry(QtCore.QRect(0, 0, 835, 51))
        self.topLabel.setStyleSheet("background-color: rgb(0, 170, 255);\n"
"font: 20pt \"华文新魏\";")
        self.topLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.topLabel.setObjectName("topLabel")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setGeometry(QtCore.QRect(280, 91, 555, 311))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(3, 60, 271, 131))
        self.groupBox.setStyleSheet("font: 11pt \"华文楷体\";")
        self.groupBox.setObjectName("groupBox")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setGeometry(QtCore.QRect(134, 40, 101, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setGeometry(QtCore.QRect(134, 90, 101, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(20, 40, 101, 22))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 90, 101, 22))
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(0, 210, 271, 141))
        self.groupBox_2.setStyleSheet("font: 11pt \"华文楷体\";")
        self.groupBox_2.setObjectName("groupBox_2")
        self.up_month_combox = QtWidgets.QComboBox(self.groupBox_2)
        self.up_month_combox.setGeometry(QtCore.QRect(148, 30, 51, 22))
        self.up_month_combox.setObjectName("up_month_combox")
        self.up_month_combox.addItem("")
        self.up_month_combox.addItem("")
        self.up_month_combox.addItem("")
        self.up_month_combox.addItem("")
        self.up_month_combox.addItem("")
        self.up_month_combox.addItem("")
        self.up_month_combox.addItem("")
        self.up_month_combox.addItem("")
        self.up_month_combox.addItem("")
        self.up_month_combox.addItem("")
        self.up_month_combox.addItem("")
        self.up_month_combox.addItem("")
        self.up_year_combox = QtWidgets.QComboBox(self.groupBox_2)
        self.up_year_combox.setGeometry(QtCore.QRect(80, 30, 61, 22))
        self.up_year_combox.setObjectName("up_year_combox")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_year_combox.addItem("")
        self.up_day_combox = QtWidgets.QComboBox(self.groupBox_2)
        self.up_day_combox.setGeometry(QtCore.QRect(208, 30, 61, 22))
        self.up_day_combox.setObjectName("up_day_combox")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.up_day_combox.addItem("")
        self.startLabel = QtWidgets.QLabel(self.groupBox_2)
        self.startLabel.setGeometry(QtCore.QRect(10, 20, 61, 41))
        self.startLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.startLabel.setObjectName("startLabel")
        self.endLabel = QtWidgets.QLabel(self.groupBox_2)
        self.endLabel.setGeometry(QtCore.QRect(12, 50, 61, 41))
        self.endLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.endLabel.setObjectName("endLabel")
        self.down_month_combox = QtWidgets.QComboBox(self.groupBox_2)
        self.down_month_combox.setGeometry(QtCore.QRect(150, 60, 51, 22))
        self.down_month_combox.setObjectName("down_month_combox")
        self.down_month_combox.addItem("")
        self.down_month_combox.addItem("")
        self.down_month_combox.addItem("")
        self.down_month_combox.addItem("")
        self.down_month_combox.addItem("")
        self.down_month_combox.addItem("")
        self.down_month_combox.addItem("")
        self.down_month_combox.addItem("")
        self.down_month_combox.addItem("")
        self.down_month_combox.addItem("")
        self.down_month_combox.addItem("")
        self.down_month_combox.addItem("")
        self.down_day_combox = QtWidgets.QComboBox(self.groupBox_2)
        self.down_day_combox.setGeometry(QtCore.QRect(210, 60, 61, 22))
        self.down_day_combox.setObjectName("down_day_combox")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_day_combox.addItem("")
        self.down_year_combox = QtWidgets.QComboBox(self.groupBox_2)
        self.down_year_combox.setGeometry(QtCore.QRect(82, 60, 61, 22))
        self.down_year_combox.setObjectName("down_year_combox")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.down_year_combox.addItem("")
        self.commitBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.commitBtn.setGeometry(QtCore.QRect(86, 85, 51, 51))
        self.commitBtn.setStyleSheet("#commitBtn{\n"
"    background-color:rgba(100,225,100,30); \n"
"    border-style:outset;                \n"
"    border-width:4px;                   \n"
"    border-radius:25px;                 \n"
"    border-color:rgba(255,255,0,1);                              \n"
"    padding:10px;\n"
"}\n"
"\n"
"#commitBtn:hover{\n"
"    background-color: rgb(68, 204, 204);\n"
"}\n"
"\n"
"#commitBtn:pressed{\n"
"    background-color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"#commitBtn:disabled{\n"
"    border-color: rgb(111, 111, 111);   \n"
"    color: rgb(111, 111, 111);\n"
"}")
        self.commitBtn.setObjectName("commitBtn")
        self.changeBtn = QtWidgets.QPushButton(self.groupBox_2)
        self.changeBtn.setGeometry(QtCore.QRect(210, 85, 51, 51))
        self.changeBtn.setStyleSheet("#changeBtn{\n"
"    background-color:rgba(100,225,100,30); \n"
"    border-style:outset;                \n"
"    border-width:4px;                   \n"
"    border-radius:25px;                 \n"
"    border-color:rgba(255,255,0,1);                              \n"
"    padding:10px;\n"
"}\n"
"\n"
"#changeBtn:hover{\n"
"    background-color: rgb(68, 204, 204);\n"
"}\n"
"\n"
"#changeBtn:pressed{\n"
"    background-color: rgb(170, 255, 255);\n"
"}\n"
"\n"
"#changeBtn:disabled{\n"
"    border-color: rgb(111, 111, 111);   \n"
"    color: rgb(111, 111, 111);\n"
"}\n"
"")
        self.changeBtn.setObjectName("changeBtn")
        self.inquireBtn = QtWidgets.QPushButton(Dialog)
        self.inquireBtn.setGeometry(QtCore.QRect(360, 430, 161, 61))
        self.inquireBtn.setStyleSheet("#inquireBtn{\n"
"    font: 16pt \"华文楷体\";    \n"
"    background-color: rgb(68, 206, 206);\n"
"    border-width:2px;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"#inquireBtn:hover{\n"
"    \n"
"    background-color: rgb(55, 165, 165);\n"
"}\n"
"\n"
"#inquireBtn:pressed{\n"
"    \n"
"    background-color: rgb(82, 248, 248);\n"
"}")
        self.inquireBtn.setObjectName("inquireBtn")
        self.exitBtn = QtWidgets.QPushButton(Dialog)
        self.exitBtn.setGeometry(QtCore.QRect(630, 430, 161, 61))
        self.exitBtn.setStyleSheet("#exitBtn{\n"
"    font: 16pt \"华文楷体\";    \n"
"    background-color: rgb(68, 206, 206);\n"
"    border-width:2px;\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"#exitBtn:hover{\n"
"    \n"
"    background-color: rgb(55, 165, 165);\n"
"}\n"
"\n"
"#exitBtn:pressed{\n"
"    \n"
"    background-color: rgb(82, 248, 248);\n"
"}")
        self.exitBtn.setObjectName("exitBtn")
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 350, 271, 151))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tradingVolumeCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.tradingVolumeCheckBox.setObjectName("tradingVolumeCheckBox")
        self.checkBoxGroup = QtWidgets.QButtonGroup(Dialog)
        self.checkBoxGroup.setObjectName("checkBoxGroup")
        self.checkBoxGroup.addButton(self.tradingVolumeCheckBox)
        self.verticalLayout.addWidget(self.tradingVolumeCheckBox)
        self.marketMoneyCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.marketMoneyCheckBox.setObjectName("marketMoneyCheckBox")
        self.checkBoxGroup.addButton(self.marketMoneyCheckBox)
        self.verticalLayout.addWidget(self.marketMoneyCheckBox)
        self.topValueCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.topValueCheckBox.setObjectName("topValueCheckBox")
        self.checkBoxGroup.addButton(self.topValueCheckBox)
        self.verticalLayout.addWidget(self.topValueCheckBox)
        self.minValueCheckBox = QtWidgets.QCheckBox(self.layoutWidget)
        self.minValueCheckBox.setObjectName("minValueCheckBox")
        self.checkBoxGroup.addButton(self.minValueCheckBox)
        self.verticalLayout.addWidget(self.minValueCheckBox)
        self.progressBar = QtWidgets.QProgressBar(Dialog)
        self.progressBar.setEnabled(False)
        self.progressBar.setGeometry(QtCore.QRect(360, 400, 461, 23))
        self.progressBar.setStyleSheet("QProgressBar{\n"
"    font: 11pt \"华文楷体\";\n"
"    color: rgb(0, 0, 0);\n"
"    border:1px solid black;\n"
"    height:30;\n"
"    background:white;\n"
"    text-align:center;\n"
"    border-radius:10px;\n"
"}\n"
"\n"
"\n"
"QProgressBar::chunk{\n"
"    border-radius:10px;\n"
"    background:qlineargradient(spread:pad,x1:0,y1:0,x2:1,y2:0,stop:0 red,stop:1 blue);\n"
"}\n"
"\n"
"QProgressBar:disabled{\n"
"    color:rgb(240,240,240);\n"
"    background-color:rgb(240,240,240);\n"
"    border-color:rgb(240,240,240);\n"
"}\n"
"")
        self.progressBar.setProperty("value", 0)
        self.progressBar.setAlignment(QtCore.Qt.AlignCenter)
        self.progressBar.setObjectName("progressBar")
        self.toolsCombox = QtWidgets.QComboBox(Dialog)
        self.toolsCombox.setEnabled(False)
        self.toolsCombox.setGeometry(QtCore.QRect(0, 0, 141, 22))
        self.toolsCombox.setStyleSheet("QComboBox{\n"
"    background-color: rgb(10, 170, 255);\n"
"    font: 11pt \"华文楷体\";\n"
"    border:none;\n"
"}\n"
"\n"
"*:focus{\n"
"    outline:none\n"
"}\n"
"\n"
"QComboBox::drop-down:disabled{\n"
"    background-color: rgba(10, 170, 255,0);\n"
"}")
        self.toolsCombox.setCurrentText("")
        self.toolsCombox.setIconSize(QtCore.QSize(20, 20))
        self.toolsCombox.setObjectName("toolsCombox")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/quire.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolsCombox.addItem(icon, "")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/calculate.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolsCombox.addItem(icon1, "")
        self.showLabel = QtWidgets.QLabel(Dialog)
        self.showLabel.setGeometry(QtCore.QRect(280, 50, 555, 41))
        self.showLabel.setStyleSheet("font: 16pt \"华文楷体\";\n"
"color: rgb(0, 186, 186);")
        self.showLabel.setText("")
        self.showLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.showLabel.setObjectName("showLabel")

        self.retranslateUi(Dialog)
        self.toolsCombox.setCurrentIndex(-1)
        self.inquireBtn.clicked.connect(Dialog.inquire)
        self.exitBtn.clicked.connect(Dialog.closeWindow)
        self.commitBtn.clicked.connect(Dialog.checkBoxCommit)
        self.changeBtn.clicked.connect(Dialog.checkBoxChanged)
        self.toolsCombox.currentIndexChanged['int'].connect(Dialog.executeFun)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.topLabel.setText(_translate("Dialog", "浦发银行股票分析系统"))
        self.groupBox.setTitle(_translate("Dialog", "股票信息选择"))
        self.comboBox.setItemText(0, _translate("Dialog", "600000.SH"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "浦发银行"))
        self.label.setText(_translate("Dialog", "股票代码"))
        self.label_2.setText(_translate("Dialog", "单位"))
        self.groupBox_2.setTitle(_translate("Dialog", "股票信息变化时间选择"))
        self.up_month_combox.setItemText(0, _translate("Dialog", "1"))
        self.up_month_combox.setItemText(1, _translate("Dialog", "2"))
        self.up_month_combox.setItemText(2, _translate("Dialog", "3"))
        self.up_month_combox.setItemText(3, _translate("Dialog", "4"))
        self.up_month_combox.setItemText(4, _translate("Dialog", "5"))
        self.up_month_combox.setItemText(5, _translate("Dialog", "6"))
        self.up_month_combox.setItemText(6, _translate("Dialog", "7"))
        self.up_month_combox.setItemText(7, _translate("Dialog", "8"))
        self.up_month_combox.setItemText(8, _translate("Dialog", "9"))
        self.up_month_combox.setItemText(9, _translate("Dialog", "10"))
        self.up_month_combox.setItemText(10, _translate("Dialog", "11"))
        self.up_month_combox.setItemText(11, _translate("Dialog", "12"))
        self.up_year_combox.setItemText(0, _translate("Dialog", "1999"))
        self.up_year_combox.setItemText(1, _translate("Dialog", "2000"))
        self.up_year_combox.setItemText(2, _translate("Dialog", "2001"))
        self.up_year_combox.setItemText(3, _translate("Dialog", "2002"))
        self.up_year_combox.setItemText(4, _translate("Dialog", "2003"))
        self.up_year_combox.setItemText(5, _translate("Dialog", "2004"))
        self.up_year_combox.setItemText(6, _translate("Dialog", "2005"))
        self.up_year_combox.setItemText(7, _translate("Dialog", "2006"))
        self.up_year_combox.setItemText(8, _translate("Dialog", "2007"))
        self.up_year_combox.setItemText(9, _translate("Dialog", "2008"))
        self.up_year_combox.setItemText(10, _translate("Dialog", "2009"))
        self.up_year_combox.setItemText(11, _translate("Dialog", "2010"))
        self.up_year_combox.setItemText(12, _translate("Dialog", "2011"))
        self.up_year_combox.setItemText(13, _translate("Dialog", "2012"))
        self.up_year_combox.setItemText(14, _translate("Dialog", "2013"))
        self.up_year_combox.setItemText(15, _translate("Dialog", "2014"))
        self.up_year_combox.setItemText(16, _translate("Dialog", "2015"))
        self.up_year_combox.setItemText(17, _translate("Dialog", "2016"))
        self.up_day_combox.setItemText(0, _translate("Dialog", "1"))
        self.up_day_combox.setItemText(1, _translate("Dialog", "2"))
        self.up_day_combox.setItemText(2, _translate("Dialog", "3"))
        self.up_day_combox.setItemText(3, _translate("Dialog", "4"))
        self.up_day_combox.setItemText(4, _translate("Dialog", "5"))
        self.up_day_combox.setItemText(5, _translate("Dialog", "6"))
        self.up_day_combox.setItemText(6, _translate("Dialog", "7"))
        self.up_day_combox.setItemText(7, _translate("Dialog", "8"))
        self.up_day_combox.setItemText(8, _translate("Dialog", "9"))
        self.up_day_combox.setItemText(9, _translate("Dialog", "10"))
        self.up_day_combox.setItemText(10, _translate("Dialog", "11"))
        self.up_day_combox.setItemText(11, _translate("Dialog", "12"))
        self.up_day_combox.setItemText(12, _translate("Dialog", "13"))
        self.up_day_combox.setItemText(13, _translate("Dialog", "14"))
        self.up_day_combox.setItemText(14, _translate("Dialog", "15"))
        self.up_day_combox.setItemText(15, _translate("Dialog", "16"))
        self.up_day_combox.setItemText(16, _translate("Dialog", "17"))
        self.up_day_combox.setItemText(17, _translate("Dialog", "18"))
        self.up_day_combox.setItemText(18, _translate("Dialog", "19"))
        self.up_day_combox.setItemText(19, _translate("Dialog", "20"))
        self.up_day_combox.setItemText(20, _translate("Dialog", "21"))
        self.up_day_combox.setItemText(21, _translate("Dialog", "22"))
        self.up_day_combox.setItemText(22, _translate("Dialog", "23"))
        self.up_day_combox.setItemText(23, _translate("Dialog", "24"))
        self.up_day_combox.setItemText(24, _translate("Dialog", "25"))
        self.up_day_combox.setItemText(25, _translate("Dialog", "26"))
        self.up_day_combox.setItemText(26, _translate("Dialog", "27"))
        self.up_day_combox.setItemText(27, _translate("Dialog", "28"))
        self.up_day_combox.setItemText(28, _translate("Dialog", "29"))
        self.up_day_combox.setItemText(29, _translate("Dialog", "30"))
        self.up_day_combox.setItemText(30, _translate("Dialog", "31"))
        self.startLabel.setText(_translate("Dialog", "Start："))
        self.endLabel.setText(_translate("Dialog", "End："))
        self.down_month_combox.setItemText(0, _translate("Dialog", "1"))
        self.down_month_combox.setItemText(1, _translate("Dialog", "2"))
        self.down_month_combox.setItemText(2, _translate("Dialog", "3"))
        self.down_month_combox.setItemText(3, _translate("Dialog", "4"))
        self.down_month_combox.setItemText(4, _translate("Dialog", "5"))
        self.down_month_combox.setItemText(5, _translate("Dialog", "6"))
        self.down_month_combox.setItemText(6, _translate("Dialog", "7"))
        self.down_month_combox.setItemText(7, _translate("Dialog", "8"))
        self.down_month_combox.setItemText(8, _translate("Dialog", "9"))
        self.down_month_combox.setItemText(9, _translate("Dialog", "10"))
        self.down_month_combox.setItemText(10, _translate("Dialog", "11"))
        self.down_month_combox.setItemText(11, _translate("Dialog", "12"))
        self.down_day_combox.setItemText(0, _translate("Dialog", "1"))
        self.down_day_combox.setItemText(1, _translate("Dialog", "2"))
        self.down_day_combox.setItemText(2, _translate("Dialog", "3"))
        self.down_day_combox.setItemText(3, _translate("Dialog", "4"))
        self.down_day_combox.setItemText(4, _translate("Dialog", "5"))
        self.down_day_combox.setItemText(5, _translate("Dialog", "6"))
        self.down_day_combox.setItemText(6, _translate("Dialog", "7"))
        self.down_day_combox.setItemText(7, _translate("Dialog", "8"))
        self.down_day_combox.setItemText(8, _translate("Dialog", "9"))
        self.down_day_combox.setItemText(9, _translate("Dialog", "10"))
        self.down_day_combox.setItemText(10, _translate("Dialog", "11"))
        self.down_day_combox.setItemText(11, _translate("Dialog", "12"))
        self.down_day_combox.setItemText(12, _translate("Dialog", "13"))
        self.down_day_combox.setItemText(13, _translate("Dialog", "14"))
        self.down_day_combox.setItemText(14, _translate("Dialog", "15"))
        self.down_day_combox.setItemText(15, _translate("Dialog", "16"))
        self.down_day_combox.setItemText(16, _translate("Dialog", "17"))
        self.down_day_combox.setItemText(17, _translate("Dialog", "18"))
        self.down_day_combox.setItemText(18, _translate("Dialog", "19"))
        self.down_day_combox.setItemText(19, _translate("Dialog", "20"))
        self.down_day_combox.setItemText(20, _translate("Dialog", "21"))
        self.down_day_combox.setItemText(21, _translate("Dialog", "22"))
        self.down_day_combox.setItemText(22, _translate("Dialog", "23"))
        self.down_day_combox.setItemText(23, _translate("Dialog", "24"))
        self.down_day_combox.setItemText(24, _translate("Dialog", "25"))
        self.down_day_combox.setItemText(25, _translate("Dialog", "26"))
        self.down_day_combox.setItemText(26, _translate("Dialog", "27"))
        self.down_day_combox.setItemText(27, _translate("Dialog", "28"))
        self.down_day_combox.setItemText(28, _translate("Dialog", "29"))
        self.down_day_combox.setItemText(29, _translate("Dialog", "30"))
        self.down_day_combox.setItemText(30, _translate("Dialog", "31"))
        self.down_year_combox.setItemText(0, _translate("Dialog", "1999"))
        self.down_year_combox.setItemText(1, _translate("Dialog", "2000"))
        self.down_year_combox.setItemText(2, _translate("Dialog", "2001"))
        self.down_year_combox.setItemText(3, _translate("Dialog", "2002"))
        self.down_year_combox.setItemText(4, _translate("Dialog", "2003"))
        self.down_year_combox.setItemText(5, _translate("Dialog", "2004"))
        self.down_year_combox.setItemText(6, _translate("Dialog", "2005"))
        self.down_year_combox.setItemText(7, _translate("Dialog", "2006"))
        self.down_year_combox.setItemText(8, _translate("Dialog", "2007"))
        self.down_year_combox.setItemText(9, _translate("Dialog", "2008"))
        self.down_year_combox.setItemText(10, _translate("Dialog", "2009"))
        self.down_year_combox.setItemText(11, _translate("Dialog", "2010"))
        self.down_year_combox.setItemText(12, _translate("Dialog", "2011"))
        self.down_year_combox.setItemText(13, _translate("Dialog", "2012"))
        self.down_year_combox.setItemText(14, _translate("Dialog", "2013"))
        self.down_year_combox.setItemText(15, _translate("Dialog", "2014"))
        self.down_year_combox.setItemText(16, _translate("Dialog", "2015"))
        self.down_year_combox.setItemText(17, _translate("Dialog", "2016"))
        self.commitBtn.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">To commit the date</span></p></body></html>"))
        self.commitBtn.setWhatsThis(_translate("Dialog", "<html><head/><body><p><br/></p></body></html>"))
        self.commitBtn.setText(_translate("Dialog", "S"))
        self.changeBtn.setToolTip(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">To change the date</span></p></body></html>"))
        self.changeBtn.setText(_translate("Dialog", "C"))
        self.inquireBtn.setText(_translate("Dialog", "Inquire"))
        self.exitBtn.setText(_translate("Dialog", "Exit"))
        self.tradingVolumeCheckBox.setText(_translate("Dialog", "一段时间内成交金额的变化"))
        self.marketMoneyCheckBox.setText(_translate("Dialog", "一段时间内市值的变化"))
        self.topValueCheckBox.setText(_translate("Dialog", "一段时间内最高价的变化"))
        self.minValueCheckBox.setText(_translate("Dialog", "一段时间内最低价的变化"))
        self.toolsCombox.setItemText(0, _translate("Dialog", "查询某天的数据"))
        self.toolsCombox.setItemText(1, _translate("Dialog", "计算上证指数"))

