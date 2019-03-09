# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import QCoreApplication

from second import Ui_sencond
import cryption
import communicate
import ctypes
import binascii


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setupUi(self)
        self.retranslateUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(430, 280)

        self.login = QtWidgets.QPushButton(Form)
        self.login.setGeometry(QtCore.QRect(60, 200, 121, 31))
        self.login.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.login.setObjectName("login")
        self.logexit = QtWidgets.QPushButton(Form)
        self.logexit.setGeometry(QtCore.QRect(240, 200, 121, 31))
        self.logexit.setObjectName("logexit")
        self.ID = QtWidgets.QTextEdit(Form)
        self.ID.setEnabled(True)
        self.ID.setGeometry(QtCore.QRect(140, 70, 221, 21))
        self.ID.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.ID.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.ID.setUndoRedoEnabled(True)
        self.ID.setAcceptRichText(True)
        self.ID.setObjectName("ID")
        #self.ID.setReadOnly(True)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(70, 70, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(70, 120, 61, 21))
        self.label_2.setObjectName("label_2")

        self.pwd = QtWidgets.QLineEdit(Form)
        self.pwd.setGeometry(QtCore.QRect(140, 120, 221, 20))
        self.pwd.setObjectName("pwd")
        self.pwd.setEchoMode(self.pwd.Password) #新增属性

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "System Login"))
        self.login.setText(_translate("Form", "Login"))
        self.logexit.setText(_translate("Form", "Exit"))
        self.label.setText(_translate("Form", "ID："))
        self.label_2.setText(_translate("Form", "PWD："))

        #槽函数
        self.login.clicked.connect(self.slots_login)
        self.logexit.clicked.connect(QCoreApplication.instance().quit)


    def slots_login(self):
        key = b'\x31\x31\x31\x31\x31\x31\x31\x31\x32\x32\x32\x32\x32\x32\x32\x32'
        inputID = self.ID.toPlainText()
        inputpwd = self.pwd.text()
        if len(inputpwd) > 24 or inputID == '' or inputpwd == '':
            ctypes.windll.user32.MessageBoxA(0, u"ID or PWD error".encode('gb2312'), u'msg'.encode('gb2312'), 0)
            return

        #封装了个des加解密函数，根据key的长度不同可以调用des或者3des
        #pwd_cipher = cryption.des_algorithm('encrypt', 'ecb', inputpwd, key, 'iv')
        retdata = communicate.communication(b'\x01\x02\x03\x04')

        if (retdata == b'\x04\x03\x02\x01'):  #这个部分的条件判断可以自己做，比如密文不匹配数据库，或者ID有问题等等
            Ui_sencond.widget = QtWidgets.QWidget()  # 进入下一界面
            Ui_sencond.newui = Ui_sencond()
            Ui_sencond.newui.setupUi(Ui_sencond.widget)
            Ui_sencond.widget.show()
            widget.close()  #关闭当前窗口
        else:
            ctypes.windll.user32.MessageBoxA(0, u"ID or PWD error".encode('gb2312'),u'msg'.encode('gb2312'), 0)
            return


if __name__=="__main__":
    import sys
    app = 0
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(widget)
    widget.show()
    sys.exit(app.exec_())



