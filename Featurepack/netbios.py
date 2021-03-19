import os
import re

from Featurepack.myPool import MyPool


class NETBIOS():
    def __init__(self):
        """
        netbios信息获取
        """
        print('扫描开始')
        print('请等待不要着急...........')
        result = os.popen("route print").read()  # 打开路由表
        ip = re.search(r"0.0.0.0\s+0.0.0.0\s+\S+\s+(\S+)", result).group(1)  # 选取当前上网的ip
        self.net = re.findall(r"(\d+\.\d+\.\d+\.)\d+", ip)[0]  # 截取网段
        self.j = []

    def task(self, ag):
        """
        获取netbios信息
        :param cmd:执行命令
        :param ip:当前测试IP
        :return:无
        """
        r = os.popen(ag[0]).read()
        if "<00>" in r:
            r1 = re.findall(r"(\S+.+)<00>", r)  # 截取主机名和工作组
            print(r1)
            self.j.append([r1, ag[1]])
        return self.j



def end_callback(msg):
    """
    进程池执行结束后的回调函数
    :param msg: 执行结束后的结果
            msg数据 List->
    hostname = i[0][0] ,
    workgroup = i[0][1],
    newip = i[1]
    :return: 无
    """
    for i in msg:
        print(i[0][0],i[0][1],i[1])


if __name__ == '__main__':
    netbios=NETBIOS()
    cmdList = []
    for i in range(1, 255):
        newip = netbios.net + str(i)
        cmdList.append([f"nbtstat -A {newip}", newip])  # 扫描网段
    myPool = MyPool(10, True)
    myPool.run( netbios.task, cmdList)
    myPool.start()
