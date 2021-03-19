import time

import os

# 定义函数完成文件或文件夹的创建
def mkdir_file(dir_name):
    """
    如果不存在文件夹，创建文件
    :param dir_name: 文件夹名
    :return:
    """
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)


def caches(func):
    """ 缓存装饰器 """
    data = {}

    def wrapper(*args, **kwargs):
        key = '{}_{}_{}'.format(func.__name__, str(args), str(kwargs))
        if key in data:
            result = data[key]
            print('我是被缓存下来的！')
        else:
            result = func(*args, **kwargs)
            data[key] = result
            print('我是新来的！')
        return result

    return wrapper


def caches_upgrade(ex=None):
    """ 缓存装饰器升级版，如果超过某个时间就重新更新数据，ex：超时秒数 """
    data = {}

    def func_wrapper(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            key = f'{func.__name__}{args}{kwargs}'
            keyn = key + 'new_dt'
            new_dt = time.time()
            if key in data and ex and keyn in data and new_dt - data[keyn] > ex:
                data[key] = func(*args, **kwargs)
                data[keyn] = new_dt
            elif key not in data:
                data[key] = func(*args, **kwargs)
                data[keyn] = new_dt
            return data[key]

        return wrapper

    return func_wrapper


def errors(func):
    """ 异常捕获装饰器 """

    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            print('出现异常：', exc)

    return wrapper


def times(func):
    """ 记录执行时间装饰器 """

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print('执行时间', time.time() - start, '秒')
        return result

    return wrapper


def loggers(func):
    """ 记录日志装饰器 """

    def wrapper(*args, **kwargs):
        print('记录日志：{}_{}_{}'.format(func, str(args), str(kwargs)))
        return func(*args, **kwargs)

    return wrapper


class Wrappers:
    """ Python 常用类里面的装饰器 """

    __slots__ = ('_name',)  # 此类里面允许的属性

    def __init__(self):
        self._name = None

    @property
    def name(self):
        """ 相当于GET方法，能像属性一样操作 """
        return self._name

    @name.setter
    def name(self, name):
        """ 相当于SET方法，能像属性一样操作赋值 """
        self._name = name

    @staticmethod
    def adds(x, y):
        """ 静态方法，在类没有创建实例的
            情况下，可以通过类名直接引用 """
        return x + y

    @classmethod
    def addc(self, x, y):
        """ 类方法 """
        return x + y
