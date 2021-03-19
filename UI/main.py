from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtWidgets import QMessageBox

from login import Ui_Dialog
from mainwindow import Ui_MainWindow
from choosefunction import Ui_ChooseFunction


class choosefunction(QtWidgets.QMainWindow):
    """
    功能页面
    """
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_ChooseFunction()
        self.ui.setupUi(self)
        #初始化单选框选择模式
        self.ui.localAddress.click()
        #设置提交按钮点击事件
        self.ui.Scan.clicked.connect(self.test)



        # self.ui.loginButton.clicked.connect(self.query_formula)
        # # 给button 的 点击动作绑定一个事件处理函数
        # self.ui.lineEdit_2.returnPressed.connect(self.log_returnPressed)

    def getip(self):
        """
        获取测试ip
        :return: 测试ip
        """
        #单选框逻辑处理
        if self.ui.localAddress.isChecked():
             ip = self.ui.AddressText.text()
             return ip
        elif self.ui.NetWorkAddress.isChecked():
             iplist =self.ui.NetWorkAddress_2.text()
             return iplist
        elif self.ui.localAddressS.isChecked():
             AddressS = self.ui.AddressTextS.text()
             return AddressS


    def test(self):
        self.ui.PortOnOff.text()



class query_window(QtWidgets.QMainWindow):
    """
    登录界面
    """
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


