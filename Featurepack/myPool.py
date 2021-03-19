from multiprocessing import Pool


class MyPool():
    def __init__(self, num,isDebug=False):
        """
        进程池
        :param num: 进程池同时执行的数量
        """
        self.pool = Pool(num)
        self.isDebug = isDebug
        # self.poolLost = []

    def run(self, function, taskList, callback=None):
        """
        进程池添加数据
        :param function:进程执行的函数
        :param taskList: 进程行的参数列表
        :param callback: 函数执行完毕后的回调函数
        :return: 无
        """
        if self.isDebug:
            print(function)
            print(taskList)
            print(callback)
        for i in taskList:
            print(i)
            # 从进程池中申请进程，传入callback参数作为进程结束后的回调函数
            self.pool.apply_async(func=function, args=(i,), callback=callback)

    def start(self):
        if self.isDebug:
            print("start")
        """
        开始执行多进程操作
        :return: 无
        """
        self.pool.close()
        self.pool.join()


# 测试函数
class T():
    def p(self,i):
        print(i)
        return i


    def p1(self,msg):
        print(msg, "结束回调")


if __name__ == "__main__":
    myPool = MyPool(10,True)
    t= T()
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    myPool.run(t.p, a, t.p1)
    myPool.start()
