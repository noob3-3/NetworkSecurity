import subprocess


def testping(host):
    cmd = 'ping -c %d %s' % (1, host)  # 获取ping测试主机地址
    p = subprocess.Popen(args=cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)  # 执行ping命令，并输出命令执行结果
    (stdoutput, erroutput) = p.communicate()  # 保存输出结果
    output = stdoutput.decode('gbk')  # 因为communicate()输出的结果为bytes类型，转换为字符串
    if output.find("ttl=") >= 0:  # 对输出信息进行筛选，输出结果
        return True
    else:
        return False


if __name__ == "__main__":
    testping(input('请输入主机地址:'))