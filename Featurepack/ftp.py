#! /usr/bin/env python
# _*_  coding:utf-8 _*_

import ftplib, time

username_list = ['root', 'ftp', 'admin']
password_list = ['root', '123', 'ftp', 'oracle']


def ftp(ip, port=21):
    for username in username_list:
        user = username.rstrip()
        for password in password_list:
            pwd = password.rstrip()
            try:
                ftp = ftplib.FTP()
                ftp.connect(ip, port, 10)
                ftp.login(user, pwd)
                ftp.quit()
                print('[+] FTP weak password: ' + user, pwd)

            except:
                print('[-] checking for ' + user, pwd + ' fail')



if __name__ == '__main__':
    start_time = time.time()

    ftp('192.168.0.160')
    print('Checking for FTP weak password： %d 秒' % (time.time() - start_time))
