import time

from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from PyQt5.QtWidgets import QMessageBox

from NetworkSegmentsParsing import get_ip_list
from login import Ui_Dialog
from mainwindow import Ui_MainWindow
from choosefunction import Ui_ChooseFunction

functionLIstanbul = ['PortOnOff', 'FTP', 'IIS', 'startService', 'SNTP', 'SNMP', 'NetBios', 'POP3', 'SqlServer_', 'Remote', 'www', 'socket5', 'Tlent', 'SSH']

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
        self.ui.Scan.clicked.connect(self.my_run)

    def getip(self):
        """
        获取测试ip
        :return: 测试ip
        """
        res = []
        #单选框逻辑处理
        try:
            if self.ui.localAddress.isChecked():
                 res[0] = self.ui.AddressText.text()

            elif self.ui.localAddressS.isChecked():
                 iplist = self.ui.AddressTextS.text()
                 res =  iplist.split(',')
            elif self.ui.NetWorkAddress.isChecked():
                 AddressS = self.ui.NetWorkAddress_2.text()
                 # print(AddressS)
                 res =  get_ip_list(AddressS)
        except :
            self.my_critical("网段设置错误")
        return res

    def getfunction(self):
        """
        返回用户选择的
        :return:返回字典，储存所有复选框勾选信息
        """
        fundic = {
            "PortOnOff": self.ui.PortOnOff.isChecked(),#端口扫描
            "FTP": self.ui.FTP.isChecked(),#ftp
            "IIS": self.ui.IIS.isChecked(),#
            "startService": self.ui.startService.isChecked(),#开放服务
            "SNTP": self.ui.SNTP.isChecked(),#SNTP
            "SNMP": self.ui.SNMP.isChecked(),#SNMP
            "NetBios": self.ui.NetBios.isChecked(),#NetBios
            "POP3": self.ui.POP3.isChecked(),#POP3
            "SqlServer_": self.ui.SqlServer_.isChecked(),#SqlServer_
            "Remote": self.ui.Remote.isChecked(),#Remote
            "www": self.ui.www.isChecked(),#www
            "socket5": self.ui.socket5.isChecked(),#socket5
            "Tlent": self.ui.Tlent.isChecked(),#Tlent
            "SSH": self.ui.SSH.isChecked()#SSH

        }
        return fundic

    def my_critical(self,e):
        QMessageBox.critical(
            self,
            '错误',
            e)


    def get_concurrency(self):
        """
        获取线程与进程配置信息
        :return: 无
        """
        try:
            _process_sum = int(self.ui.lineEdit_4.text())
            _Thread_sum = int(self.ui.lineEdit_5.text())
            if 0 < _process_sum < 20 and 0 < _Thread_sum < 40:
                self.process_sum = _process_sum
                self.Thread_sum = _Thread_sum
            else:
                self.my_critical("请按照要求重新填写线程/进程数")
        except:
            self.my_critical('请正确填写')

    def get_responsiveness(self):
        """
        获取用户是否选择跳过未响应程序
        :return:无
        """
        self.UnresponsiveHost = self.ui.passAnswer.isChecked()
        self.passAddress = self.ui.passAddress.isChecked()



    def my_run(self):
        #获取IP信息
        self.ip_list = self.getip()
        #获取线程，进程数
        self.get_concurrency()
        #判断是否需要跳过未响应主机
        self.get_responsiveness()
        if self.UnresponsiveHost:
            #跳过未响应
            #ip是否在线筛选 进度显示
            #获取在线的IP信息 更新到ip_list去 结果显示
            pass
        #判断是否跳过未开放端口
        if self.passAddress:
            #跳过未开放端口的服务
            #端口扫描 进度显示
            #去做服务检测
            pass
        else:
            #做服务检测  结果显示
            pass








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


