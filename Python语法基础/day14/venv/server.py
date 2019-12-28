# coding=utf-8
"""
网路
# """

from time import time
from threading import Thread

import requests
#
# class DownloadHanlder(Thread):
#
#     def __init__(self, url):
#         super().__init__()
#         self._url = url
#
#     def run(self) -> None:
#         filename = self._url[self._url.rfind("/") + 1:]
#         resp = requests.get(self._url)
#         with open(filename, "wb") as f:
#             f.write(resp.content)
#
# def main():
#     resp = requests.get("http://api.tianapi.com/generalnews/?key=fa95bf887251632dd4c8020b6ed167f9&num=10")
#     data_model = resp.json()
#     for dic in data_model["newslist"]:
#         url = dic["picUrl"]
#         DownloadHanlder(url).start()
#
# if __name__ == '__main__':
#     main()


"""
TCP套接字
"""

from socket import  socket, SOCK_STREAM, AF_INET
from datetime import datetime

# def main():
#     # 1.创建套接字对象并指定使用哪种传输服务
#     # family=AF_INET - IPv4地址
#     # family=AF_INET6 - IPv6地址
#     # type=SOCK_STREAM - TCP套接字
#     # type=SOCK_DGRAM - UDP套接字
#     # type=SOCK_RAW - 原始套接字
#     server = socket(AF_INET,SOCK_STREAM)
#     # 2.绑定ip
#     server.bind(("10.10.11.21", 8789))
#     # 3.开启监听
#     # 参数512可以理解为连接队列的大小
#     server.listen(521)
#     print("服务期开始监听")
#     while True:
#         # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
#         # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
#         # accept方法返回一个元组其中的第一个元素是客户端对象
#         # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
#         client, addr = server.accept()
#         print(str(addr) + "连接到了服务期")
#         # 5.发送数据
#         client.send(str(datetime.now()).encode("utf-8"))
#         # 6.断开连接
#         client.close()

from json import dumps
from base64 import b64encode

def main():

    class FileTransferHandler(Thread):

        def __init__(self, client):
            super().__init__()
            self.client = client

        def run(self) -> None:
            my_dict = {}
            my_dict["filename"] = "5db29ccf6748d.jpg"
            my_dict["filedata"] = data
            json_str = dumps(my_dict)
            self.client.send(json_str.encode("utf-8"))
            self.client.close()



    # 1.创建套接字对象并指定使用哪种传输服务
    # family=AF_INET - IPv4地址
    # family=AF_INET6 - IPv6地址
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(AF_INET,SOCK_STREAM)
    # 2.绑定ip
    server.bind(("10.10.11.21", 8789))
    # 3.开启监听
    # 参数512可以理解为连接队列的大小
    server.listen(521)
    print("服务期开始监听")
    with open("5db29ccf6748d.jpg", "rb") as f:
        data = b64encode(f.read()).decode("utf-8")
    while True:
        # 4.通过循环接收客户端的连接并作出相应的处理(提供服务)
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端的地址(由IP和端口两部分构成)
        client, addr = server.accept()
        print(str(addr) + "连接到了服务期")
        # 启动线程处理客户端请求
        FileTransferHandler(client).start()

if __name__ == '__main__':
    main()





