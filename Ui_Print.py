# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\print.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(862, 617)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        font = QtGui.QFont()
        font.setFamily("Microsoft YaHei")
        font.setPointSize(10)
        self.centralwidget.setFont(font)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 761, 541))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.portGroupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.portGroupBox.setObjectName("portGroupBox")
        self.formLayout_2 = QtWidgets.QFormLayout(self.portGroupBox)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label = QtWidgets.QLabel(self.portGroupBox)
        self.label.setObjectName("label")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.portNameBox = QtWidgets.QComboBox(self.portGroupBox)
        self.portNameBox.setObjectName("portNameBox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.portNameBox)
        self.label_2 = QtWidgets.QLabel(self.portGroupBox)
        self.label_2.setObjectName("label_2")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.baudRateBox = QtWidgets.QComboBox(self.portGroupBox)
        self.baudRateBox.setObjectName("baudRateBox")
        self.baudRateBox.addItem("")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.baudRateBox)
        self.label_3 = QtWidgets.QLabel(self.portGroupBox)
        self.label_3.setObjectName("label_3")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.bytesize = QtWidgets.QComboBox(self.portGroupBox)
        self.bytesize.setObjectName("bytesize")
        self.bytesize.addItem("")
        self.bytesize.addItem("")
        self.bytesize.addItem("")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.bytesize)
        self.label_4 = QtWidgets.QLabel(self.portGroupBox)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.parity = QtWidgets.QComboBox(self.portGroupBox)
        self.parity.setObjectName("parity")
        self.parity.addItem("")
        self.parity.addItem("")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.parity)
        self.label_5 = QtWidgets.QLabel(self.portGroupBox)
        self.label_5.setObjectName("label_5")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.stopbits = QtWidgets.QComboBox(self.portGroupBox)
        self.stopbits.setObjectName("stopbits")
        self.stopbits.addItem("")
        self.stopbits.addItem("")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.stopbits)
        self.verticalLayout_4.addWidget(self.portGroupBox)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.openBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.openBtn.setObjectName("openBtn")
        self.verticalLayout_4.addWidget(self.openBtn)
        self.closeBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.closeBtn.setObjectName("closeBtn")
        self.verticalLayout_4.addWidget(self.closeBtn)
        self.clearBtn = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.clearBtn.setObjectName("clearBtn")
        self.verticalLayout_4.addWidget(self.clearBtn)
        self.horizontalLayout.addLayout(self.verticalLayout_4)
        self.groupBox = QtWidgets.QGroupBox(self.horizontalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.groupBox)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.selectImageBtn = QtWidgets.QPushButton(self.tab)
        self.selectImageBtn.setGeometry(QtCore.QRect(290, 180, 75, 23))
        self.selectImageBtn.setObjectName("selectImageBtn")
        self.printImageBtn = QtWidgets.QPushButton(self.tab)
        self.printImageBtn.setGeometry(QtCore.QRect(380, 180, 75, 23))
        self.printImageBtn.setObjectName("printImageBtn")
        self.graphicsView = QtWidgets.QGraphicsView(self.tab)
        self.graphicsView.setGeometry(QtCore.QRect(10, 10, 256, 191))
        self.graphicsView.setObjectName("graphicsView")
        self.tabWidget.addTab(self.tab, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textEdit = QtWidgets.QTextEdit(self.tab_3)
        self.textEdit.setGeometry(QtCore.QRect(10, 10, 251, 191))
        self.textEdit.setObjectName("textEdit")
        self.hexBtn = QtWidgets.QPushButton(self.tab_3)
        self.hexBtn.setGeometry(QtCore.QRect(370, 180, 75, 23))
        self.hexBtn.setObjectName("hexBtn")
        self.textBtn = QtWidgets.QPushButton(self.tab_3)
        self.textBtn.setGeometry(QtCore.QRect(290, 180, 75, 23))
        self.textBtn.setObjectName("textBtn")
        self.tabWidget.addTab(self.tab_3, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout.addWidget(self.groupBox)
        self.horizontalLayout.setStretch(1, 3)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 862, 23))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "打印机"))
        self.portGroupBox.setTitle(_translate("mainWindow", "串口设置"))
        self.label.setText(_translate("mainWindow", "串口号"))
        self.label_2.setText(_translate("mainWindow", "波特率"))
        self.baudRateBox.setItemText(0, _translate("mainWindow", "9600"))
        self.label_3.setText(_translate("mainWindow", "数据位"))
        self.bytesize.setItemText(0, _translate("mainWindow", "8"))
        self.bytesize.setItemText(1, _translate("mainWindow", "7"))
        self.bytesize.setItemText(2, _translate("mainWindow", "6"))
        self.label_4.setText(_translate("mainWindow", "校验位"))
        self.parity.setItemText(0, _translate("mainWindow", "0"))
        self.parity.setItemText(1, _translate("mainWindow", "1"))
        self.label_5.setText(_translate("mainWindow", "停止位"))
        self.stopbits.setItemText(0, _translate("mainWindow", "1"))
        self.stopbits.setItemText(1, _translate("mainWindow", "0"))
        self.openBtn.setText(_translate("mainWindow", "打开"))
        self.closeBtn.setText(_translate("mainWindow", "关闭"))
        self.clearBtn.setText(_translate("mainWindow", "清理"))
        self.groupBox.setTitle(_translate("mainWindow", "传输内容"))
        self.textBrowser.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">欢迎使用！——胡伟</p></body></html>"))
        self.selectImageBtn.setText(_translate("mainWindow", "选择图片"))
        self.printImageBtn.setText(_translate("mainWindow", "打印图片"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("mainWindow", "图片"))
        self.textEdit.setHtml(_translate("mainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Microsoft YaHei\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">bbb6d3adcab9d3c3bafaceb0</p></body></html>"))
        self.hexBtn.setText(_translate("mainWindow", "Hex发送"))
        self.textBtn.setText(_translate("mainWindow", "文本发送"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("mainWindow", "文本"))

