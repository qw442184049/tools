# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'second.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QFileDialog
from PyQt5.QtCore import Qt

import ctypes
import binascii
import hashlib
import zlib
import configparser
import communicate
import os

SHA256 = 0
SHA512 = 1

CPU_1902s = 0

UNEARSE = 0
EARSE = 1

fileoptimes = 0
setfilestr = ''

diroptimes = 0
set_outdirstr = ''

class Ui_sencond(QtWidgets.QWidget):

    def __init__(self):
        super(Ui_sencond, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, sencond):
        sencond.setObjectName("sencond")
        sencond.resize(711, 480)
        sencond.setAutoFillBackground(False)
        self.test_tab = QtWidgets.QTabWidget(sencond)
        self.test_tab.setGeometry(QtCore.QRect(20, 20, 671, 441))
        self.test_tab.setObjectName("test_tab")

        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")

        self.functional_area = QtWidgets.QGroupBox(self.tab)
        self.functional_area.setGeometry(QtCore.QRect(10, 10, 641, 221))
        self.functional_area.setObjectName("functional_area")

        self.button1 = QtWidgets.QPushButton(self.functional_area)
        self.button1.setGeometry(QtCore.QRect(20, 20, 101, 31))
        self.button1.setObjectName("button1")

        self.button2 = QtWidgets.QPushButton(self.functional_area)
        self.button2.setGeometry(QtCore.QRect(20, 70, 101, 31))
        self.button2.setObjectName("button2")

        self.button3 = QtWidgets.QPushButton(self.functional_area)
        self.button3.setGeometry(QtCore.QRect(20, 127, 101, 31))
        self.button3.setObjectName("button3")

        self.button4 = QtWidgets.QPushButton(self.functional_area)
        self.button4.setGeometry(QtCore.QRect(20, 178, 101, 31))
        self.button4.setObjectName("button4")

        self.choose1 = QtWidgets.QCheckBox(self.functional_area)
        self.choose1.setGeometry(QtCore.QRect(490, 130, 101, 21))
        self.choose1.setObjectName("choose1")

        self.selectfile = QtWidgets.QTextEdit(self.functional_area)
        self.selectfile.setGeometry(QtCore.QRect(150, 20, 321, 31))
        self.selectfile.setObjectName("selectfile")
        self.selectfile.setReadOnly(True)  # 新增属性

        self.out_dir = QtWidgets.QTextEdit(self.functional_area)
        self.out_dir.setGeometry(QtCore.QRect(150, 70, 321, 31))
        self.out_dir.setObjectName("out_dir")
        self.out_dir.setReadOnly(True) #新增属性

        self.parameter1 = QtWidgets.QLabel(self.functional_area)
        self.parameter1.setGeometry(QtCore.QRect(150, 130, 61, 21))
        self.parameter1.setObjectName("parameter1")

        self.parameter2 = QtWidgets.QLabel(self.functional_area)
        self.parameter2.setGeometry(QtCore.QRect(150, 180, 61, 31))
        self.parameter2.setObjectName("label")

        self.parameter3 = QtWidgets.QLabel(self.functional_area)
        self.parameter3.setGeometry(QtCore.QRect(322, 130, 61, 21))
        self.parameter3.setObjectName("parameter3")

        self.parameter4 = QtWidgets.QLabel(self.functional_area)
        self.parameter4.setGeometry(QtCore.QRect(322, 180, 61, 31))
        self.parameter4.setObjectName("parameter4")

        self.select1 = QtWidgets.QLabel(self.functional_area)
        self.select1.setGeometry(QtCore.QRect(490, 20, 71, 21))
        self.select1.setObjectName("select1")

        self.select2 = QtWidgets.QLabel(self.functional_area)
        self.select2.setGeometry(QtCore.QRect(490, 75, 71, 21))
        self.select2.setObjectName("select2")

        self.select1_type = QtWidgets.QComboBox(self.functional_area)
        self.select1_type.setGeometry(QtCore.QRect(560, 15, 71, 31))
        self.select1_type.setObjectName("select1_type")
        self.select1_type.addItem("")
        self.select1_type.addItem("")

        self.select2_type = QtWidgets.QComboBox(self.functional_area)
        self.select2_type.setGeometry(QtCore.QRect(560, 70, 71, 31))
        self.select2_type.setObjectName("select2_type")
        self.select2_type.addItem("")
        self.select2_type.addItem("")

        #This is edittext
        self.parameter1_text = QtWidgets.QTextEdit(self.functional_area)
        self.parameter1_text.setGeometry(QtCore.QRect(220, 125, 81, 31))
        self.parameter1_text.setObjectName("parameter1_text")

        self.parameter2_text = QtWidgets.QTextEdit(self.functional_area)
        self.parameter2_text.setGeometry(QtCore.QRect(220, 180, 81, 31))
        self.parameter2_text.setObjectName("parameter2_text")

        self.parameter3_text = QtWidgets.QTextEdit(self.functional_area)
        self.parameter3_text.setGeometry(QtCore.QRect(390, 125, 81, 31))
        self.parameter3_text.setObjectName("parameter3_text")

        self.parameter4_text = QtWidgets.QTextEdit(self.functional_area)
        self.parameter4_text.setGeometry(QtCore.QRect(390, 180, 81, 31))
        self.parameter4_text.setObjectName("parameter4_text")

        self.logoutput = QtWidgets.QGroupBox(self.tab)
        self.logoutput.setGeometry(QtCore.QRect(10, 240, 641, 161))
        self.logoutput.setObjectName("logoutput")

        self.clearlog = QtWidgets.QPushButton(self.logoutput)
        self.clearlog.setGeometry(QtCore.QRect(560, 20, 71, 131))
        self.clearlog.setObjectName("clear_log")

        self.log = QtWidgets.QTextEdit(self.logoutput)
        self.log.setGeometry(QtCore.QRect(20, 20, 531, 131))
        self.log.setObjectName("log")
        self.log.setReadOnly(True) #新增属性

        self.test_tab.addTab(self.tab, "")

        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.test_tab.addTab(self.tab_2, "")

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.test_tab.addTab(self.tab_3, "")

        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.test_tab.addTab(self.tab_4, "")

        self.tab_5 = QtWidgets.QWidget()
        self.tab_5.setObjectName("tab_5")
        self.test_tab.addTab(self.tab_5, "")

        self.retranslateUi(sencond)
        self.test_tab.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(sencond)

        self.readconfig(self)  #Read config from config file when opening interface

    def retranslateUi(self, sencond):
        _translate = QtCore.QCoreApplication.translate
        sencond.setWindowTitle(_translate("sencond", "template V1.00"))
        self.functional_area.setTitle(_translate("sencond", "Functional Area"))

        self.button1.setText(_translate("sencond", "button1"))
        self.button2.setText(_translate("sencond", "button2"))
        self.button3.setText(_translate("sencond", "button3"))
        self.button4.setText(_translate("sencond", "button4"))

        self.choose1.setText(_translate("sencond", "choose1"))

        self.parameter1.setText(_translate("sencond", "parameter1"))
        self.parameter2.setText(_translate("sencond", "parameter2"))
        self.parameter3.setText(_translate("sencond", "parameter3"))
        self.parameter4.setText(_translate("sencond", "parameter4"))

        self.select1_type.setItemText(0, _translate("sencond", "1"))
        self.select1_type.setItemText(1, _translate("sencond", "2"))

        self.select2_type.setItemText(0, _translate("sencond", "1"))
        self.select2_type.setItemText(1, _translate("sencond", "2"))

        self.select1.setText(_translate("sencond", "select1"))
        self.select2.setText(_translate("sencond", "select2"))

        self.logoutput.setTitle(_translate("sencond", "log"))
        self.clearlog.setText(_translate("sencond", "clear"))

        self.test_tab.setTabText(self.test_tab.indexOf(self.tab), _translate("sencond", "view1"))
        self.test_tab.setTabText(self.test_tab.indexOf(self.tab_2), _translate("sencond", "view2"))
        self.test_tab.setTabText(self.test_tab.indexOf(self.tab_3), _translate("sencond", "view3"))
        self.test_tab.setTabText(self.test_tab.indexOf(self.tab_4), _translate("sencond", "view4"))
        self.test_tab.setTabText(self.test_tab.indexOf(self.tab_5), _translate("sencond", "view5"))

        self.parameter1_text.setAlignment(Qt.AlignCenter)  #居中
        self.parameter2_text.setAlignment(Qt.AlignCenter)
        self.parameter3_text.setAlignment(Qt.AlignCenter)
        self.parameter4_text.setAlignment(Qt.AlignCenter)

        # 槽函数
        self.button1.clicked.connect(self.get_download_path)
        self.button2.clicked.connect(self.set_output_path)

        self.button3.clicked.connect(self.test1)
        self.button4.clicked.connect(self.test2)

        self.clearlog.clicked.connect(self.clear_log)


    def readconfig(self, sencond):
        config = configparser.ConfigParser()
        try:
            config.readfp(open('config.ini'))  # open config file
        except FileNotFoundError:
            ctypes.windll.user32.MessageBoxA(0, u"file error".encode('gb2312'), u'msg'.encode('gb2312'), 0)
            return

        sourcedir = config.get('dir', "sourcedir")
        outdir = config.get('dir', "outdir")

        value1 = config.get('value', "value1")
        value2 = config.get('value', "value2")
        value3 = config.get('value', "value3")
        value4 = config.get('value', "value4")

        self.selectfile.setText(sourcedir)
        self.out_dir.setText(outdir)

        self.parameter1_text.setText(value1)
        self.parameter2_text.setText(value2)
        self.parameter3_text.setText(value3)
        self.parameter4_text.setText(value4)

    def clear_log(self):
        self.log.setText("")

    def get_download_path(self):
        filestr = self.fmdir.toPlainText()
        global fileoptimes
        global setfilestr
        if fileoptimes % 2 == 0:
            filename = QFileDialog.getOpenFileName(self, 'open file', filestr)
            fileoptimes = 1
        else:
            filename = QFileDialog.getOpenFileName(self, 'open file', setfilestr)
        filestr = str(filename[0])
        setfilestr = filestr
        self.fmdir.setText(setfilestr)

    def set_output_path(self):
        outdirstr = self.out_dir.toPlainText()
        global diroptimes
        global set_outdirstr
        if diroptimes % 2 == 0:
            dirname = QtWidgets.QFileDialog.getExistingDirectory(self, "scan", outdirstr)
            diroptimes = 1
        else:
            dirname = QtWidgets.QFileDialog.getExistingDirectory(self, "scan", set_outdirstr)
        dirstr = str(dirname)
        set_outdirstr = dirstr
        self.out_dir.setText(set_outdirstr)

    def test1(self):   #Slots function test， you can delete and write your code here
        filestr = self.fmdir.toPlainText()
        outdirstr = self.out_dir.toPlainText()
        select1_index = self.select1.currentIndex()
        select2_index = self.select2.currentIndex()

        filename = os.path.basename(filestr)  #获取文件后缀名
        if "." in filename:
            filename = filename.split(".")[0]

        erase_choose = 0
        if self.choose1.isChecked():
            choose1 = 1

        #str to hex test
        test_str = 'asdasfgfa 11112 ..'     #32字节,不够的填充0
        test_str = str(binascii.b2a_hex(test_str.encode("gbk")))[2:-1]
        test_str = test_str.ljust(64,'0')  #后面填充0，0与有效字符相加是32字节
        test_hex = bytes.fromhex(test_str)


        test1_type = bytes.fromhex('00000002')[::-1]
        if select1_index == "1":
            test1_type = bytes.fromhex('00000004')[::-1]

        test2_type = bytes.fromhex('00')
        if select2_index == "1":
            erase_type = bytes.fromhex('01')

        with open(filestr,'rb') as f:
            filedata = f.read()
        filesize = len(filedata)

        sh = hashlib.sha256() #hash test
        sh.update(filedata)
        hash_256_value = sh.hexdigest()
        hashval = bytes.fromhex(hash_256_value)

        crc32cal = str(hex(zlib.crc32(hashval)))[2:] #crc32 test
        crc32cal = crc32cal.ljust(8, '0')
        crc32val = bytes.fromhex(crc32cal)[::-1]



    def test2(self):  #Slots function
        test = 1
