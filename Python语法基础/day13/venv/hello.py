# coding=utf-8
"""
进程 and 线程
"""

from random import randint
from time import time, sleep
from multiprocessing import Process
from os import getpid


# def download_task(filename):
#     print("开始下载%s>>>>" % filename)
#     time_download = randint(5, 10)
#     sleep(time_download)
#     print("%s 下载完成！耗时%d秒" % (filename, time_download))
#
#
# def main():
#     start = time()
#     download_task("hello.txt")
#     download_task("你好.txt")
#     end = time()
#     print ("总共耗时%d秒" % (end - start))



"""
线程
"""
# def download_task(filename):
#     print("启动下载进程，进程号[%d]" % getpid())
#     print("开始下载%s>>>>" % filename)
#     time_download = randint(5, 10)
#     sleep(time_download)
#     print("%s 下载完成！耗时%d秒" % (filename, time_download))
#
# def main():
#     start = time()
#     p1 = Process(target=download_task, args=('Python从入门到住院.pdf', ))
#     p1.start()
#     p2 = Process(target=download_task, args=('Peking Hot.avi', ))
#     p2.start()
#     p1.join()
#     p2.join()
#     end = time()
#     print ("总共耗时%d秒" % (end - start))

"""
进程通信
"""
import queue

# def sub_task(q,string):
#     global counter
#     while counter < 10:
#         q.put(string)
#         print(string, end= "", flush=True)
#         counter += 1
#         sleep(0.01)
#
# def main():
#     q = queue.Queue(maxsize=0)
#     p1 = Process(target=sub_task, args=(q,"ping", ))
#     p1.start()
#     p2 = Process(target=sub_task, args=(q,"pong",))
#     p2.start()
#     p1.join()
#     p2.join()

from threading import Thread, Lock
#
# class DownloadTask(Thread):
#     def __init__(self, filename):
#         super().__init__()
#         self._filename = filename
#
#     def run(self):
#         print("开始下载%s..." % self._filename)
#         time_download = randint(5, 10)
#         sleep(time_download)
#         print("%s 下载完成！耗时%d秒" % (self._filename, time_download))
#
# def main():
#     start = time()
#     t1 = DownloadTask("Python从入门到住院1.pdf")
#     t1.start()
#     t2 = DownloadTask("Python从入门到住院2.pdf")
#     t2.start()
#     t1.join()
#     t2.join()
#     end = time()
#     print('总共耗费了%.2f秒.' % (end - start))


"""
临界问题
"""

class Account(object):

    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        """计算余额"""
        # 先获取锁才能执行后续代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance

class AddMoneyThread(Thread):

    def __init__(self, account, monney):
        super().__init__()
        self._account = account
        self._monney = monney

    def run(self):
        self._account.deposit(self._monney)

def main():
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为: ￥%d元' % account.balance)


if __name__ == '__main__':
    main()
