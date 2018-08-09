#coding:utf-8
import socket
#链接服务端ip和端口
ip_port = ('127.0.0.1',9999)
#生成一个句柄
sk = socket.socket()
#请求连接服务端
sk.connect(ip_port)
#发送数据
sk.sendall(bytes('hello world','utf8'))
#接受数据
server_reply = sk.recv(1024)
#打印接受的数据
print (str(server_reply).encode("utf-8"))
#关闭连接
sk.close()