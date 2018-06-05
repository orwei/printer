# -*- coding: utf-8 -*-
# @Author: Hu Wei
# @Date:   2018-05-27 13:35:33
# @Last Modified by:   Hu Wei
# @Last Modified time: 2018-06-05 20:26:02

from Ui_Print import Ui_mainWindow

from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog, QGraphicsScene
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtSerialPort import QSerialPort, QSerialPortInfo
from PyQt5.QtCore import QIODevice
import threading
import binascii 
import time
class MainWindow(QMainWindow, Ui_mainWindow):
	def __init__(self, parent=None):
		super(MainWindow, self).__init__(parent)
		self.setupUi(self)
		self.portInit()
		self.openBtn.clicked.connect(self.portOpen)
		self.closeBtn.clicked.connect(self.portClose)
		self.clearBtn.clicked.connect(self.textClear)
		self.selectImageBtn.clicked.connect(self.imageSelect)
		self.printImageBtn.clicked.connect(self.imagePrint)
		self.textBtn.clicked.connect(self.textSend)
		self.hexBtn.clicked.connect(self.hexSend)
		print('界面设置成功！')

	def portInit(self):
		for info in QSerialPortInfo.availablePorts():
			serialPort = QSerialPort()
			serialPort.setPort(info)
			if(serialPort.open(QIODevice.ReadWrite)):
				self.portNameBox.addItem(info.portName())
				serialPort.close()

	def portOpen(self):
		self.serial = QSerialPort()
		self.serial.setPortName(self.portNameBox.currentText())
		self.serial.open(QIODevice.ReadWrite)
		self.serial.setBaudRate(int(self.baudRateBox.currentText()))
		self.serial.setDataBits(QSerialPort.Data8)
		self.serial.setParity(QSerialPort.NoParity)
		self.serial.setFlowControl(QSerialPort.NoFlowControl)
		self.serial.setStopBits(QSerialPort.OneStop)
		self.portGroupBox.setEnabled(False)

	def portClose(self):
		self.serial.close()
		self.portGroupBox.setEnabled(True)

	def imageSelect(self):
		filename = QFileDialog.getOpenFileName(self, "OpenFile", ".", "Image Files(*.jpg *.jpeg *.png *.bmp)")[0]
		if len(filename):
			image = QImage(filename)
			scene = QGraphicsScene()
			scene.addPixmap(QPixmap.fromImage(image))
			self.graphicsView.setScene(scene)
			# self.graphicsView.resize(image.width(), image.height())
			self.graphicsView.show()

	def imagePrint(self):
		file = open('image.bin', 'rb')
		prefix = '1B4BB400'
		suffix = '0D'
		data = ''
		i = 0
		while 1:
			if i % 180 == 0:
				data += suffix + prefix
			c = file.read(1)
			data += str(binascii.b2a_hex(c))[2:-1]
			if not c:
				break
			i += 1
		data = data[2:][:-8]
		self.serial.write(bytes().fromhex(data))# 将16进制转换为字节
		self.textBrowser.append(data)

	def textSend(self):
		data = self.textEdit.toPlainText()+'\n'
		self.serial.write(data.encode('gbk'))
		self.textBrowser.append(self.textEdit.toPlainText())

	def hexSend(self):
		self.serial.write(binascii.a2b_hex(self.textEdit.toPlainText()))
		self.textBrowser.append(self.textEdit.toPlainText())

	def textClear(self):
		self.textBrowser.clear()

if __name__ == '__main__':
	import sys
	app = QApplication(sys.argv)
	ui = MainWindow()
	ui.show()
	sys.exit(app.exec_())