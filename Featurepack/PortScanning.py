#!/usr/bin/python3
# -*- coding: utf-8 -*-
from socket import *
import threading


class OPENPROT():
    def __init__(self):
        self.openNum = 0
        self.openPortList = []
        self.threads = []
        self.msg = []



    def portScanner(self,host, port):
        print(host,port)
        try:
            s = socket(AF_INET, SOCK_STREAM)
            s.connect((host, port))
            # self.lock.acquire()
            self.openNum += 1
            self.openPortList.append(port)
            # self.lock.release()
            s.close()
        except:
            pass


    def main(self,ip):
        for p in range(1, 1024):
            # print(p)
            self.portScanner(ip,p)
            t = threading.Thread(target=self.portScanner, args=(ip, p))
            self.threads.append(t)
        #
        for t in self.threads:
            # print(t)
            t.start()
            t.join()
        # return self.openPortList
        # print('[*] The scan is complete!')
        # print('[*] A total of %d open port ' % (openNum))


    def callback(self,msgList):
        self.msg +=msgList
        print(msgList)
        with open('../dictionary/1.txt', 'w+') as f:
            f.write(msgList)











if __name__ == '__main__':
    pass
    # openprot = OPENPROT()
    # ip_list = get_ip_list()

    # print(openprot('192.168.0.160'))
    # a= []
    # for i in ip_list:
    #     a.append({"func":openprot.main,'args':(i,)})
    # print(use_multiprocessing(a))


    # myPool = MyPool(8, True)
    # myPool.run(openprot.main,ip_list,openprot.callback)
    # myPool.start()
    # print(openprot.openPortList)




    # print(openprot.main('192.168.0.1'))