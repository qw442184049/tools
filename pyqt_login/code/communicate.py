import socket
import ctypes
import configparser


def communication(send_data):
    config = configparser.ConfigParser()
    try:
        config.readfp(open('config.ini'))  # 打开配置文件
    except FileNotFoundError:
        ctypes.windll.user32.MessageBoxA(0, u"file error".encode('gb2312'), u'信息'.encode('gb2312'), 0)
        return
    remoteip = config.get('ip', "remote_ip")  #暂时没用到，若要启用需要填写正确的服务器ip，并在client.connect函数中替换localhost
    remoteport = config.get('ip', "remote_port")
    client = socket.socket()
    client.connect(("localhost", int(9999)))  # 连接服务器
    client.send(send_data)  # 发送数据
    #time.sleep(0.01)
    retdata = client.recv(1024)
    # client.close()
    return retdata


def get_host_ip(): #获取本机ip
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

