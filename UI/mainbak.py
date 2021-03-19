from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtWidgets import QMessageBox

from login import Ui_Dialog
from mainwindow import Ui_MainWindow
from choosefunction import Ui_ChooseFunction

class choosefunction(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        QMessageBox.critical(
            self,
            '错误',
            '用户名或密码错误')
        #初始化当选框
        # self.ui.login.clicked.connect(self.a1)
        # self.ui.Scan.clicked.connect(self.test)



        # self.ui.loginButton.clicked.connect(self.query_formula)
        # # 给button 的 点击动作绑定一个事件处理函数
        # self.ui.lineEdit_2.returnPressed.connect(self.log_returnPressed)
    def a1(self):
        QMessageBox.critical(
            self,
            '错误',
            '用户名或密码错误')

    def test(self):
        #单选框逻辑处理
        if self.ui.localAddress.isChecked():
            print(self.ui.AddressText.text())
        elif self.ui.NetWorkAddress.isChecked():
            print(self.ui.NetWorkAddress_2.text())
        elif self.ui.localAddressS.isChecked():
            print(self.ui.AddressTextS.text())

class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.query_formula)
        # 给button 的 点击动作绑定一个事件处理函数
        self.ui.lineEdit_2.returnPressed.connect(self.log_returnPressed)



    def query_formula(self):
        # 此处编写具体的业务逻辑
        self.login()

    def log_returnPressed(self):
        self.login()

    def login(self):
        name = self.ui.lineEdit.text()
        passwd =  self.ui.lineEdit_2.text()
        # if name == "admin" and passwd == "admin":
        if 1==1:
            QMessageBox.information(
                self,
                '密码正确',
                '点击确认进去软件')
            win_main.show()
            self.close()

        else:
            QMessageBox.critical(
                self,
                '错误',
                '用户名或密码错误')

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win_main = choosefunction()
    window = query_window()
    window.show()
    sys.exit(app.exec_())


