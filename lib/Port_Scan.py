import socket
from config import PORT,Open_Port_List
import multiprocessing



'''
关于端口扫描其实很不建议这么做,因为完成了三次握手会在IDS留下痕迹,
建议使用scapy库,鉴于scapy对python3实在是不友好所以我这里使用了socket库
'''



def Port_Scan(target_host,target_port):
    Sockets=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    socket.setdefaulttimeout(5)
    try:
        Sockets.connect((target_host,target_port))
        Open_Port_List.append(target_port)
    except:
        pass
    Sockets.close()


def Work_Scan(target_host):
    for port in PORT:
        Port_Scan(target_host,port)
    for port in Open_Port_List:
        print("[*]--------开放端口为 "+str(port)+" /对应服务为--------"+PORT[port])


    print("[*]--------扫描完毕 --------")


