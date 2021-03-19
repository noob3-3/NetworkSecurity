import requests

r = requests.options('http://'+'192.168.0.197')	#使用options请求方法
result = r.headers['Public']
if result.find('PUT') and result.find('MOVE'):
    print('存在IIS PUT漏洞')
else:
    print('不存在')
