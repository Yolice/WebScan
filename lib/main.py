import argparse
from CMS_Scan import CMS_Scan_Simple,CMS_Scan_Complex
from Sql_injection import Page_size
from Port_Scan import Work_Scan
from Senstive_file_Scan import SubDomain_Scan,Senstive_Scan
from WhatWeb import WhatWeb
from config import Senstive_label



def get_args():
    parser=argparse.ArgumentParser()
    parser.add_argument('-u','--url',default="http://www.discuz.net",help='请输入你的目标网站,http://www.example.com')
    args=parser.parse_args()
    return args



def Url_to_Host(url):
    host_list=url.split('.')
    host='.'.join(host_list[1:])
    return host


host=Url_to_Host(get_args().url)
url=get_args().url


function_choice={
            1:CMS_Scan_Simple,
            2:CMS_Scan_Complex,
            3:Page_size,
            4:Work_Scan,
            6:SubDomain_Scan,
            7:WhatWeb
        }




print("Web扫描器-----defoliation")
print("usage: main.py [-h] [-u URL]\n"
      "optional arguments:\n"
      "-h, --help         show this help message and exit\n"
      "-u URL, --url URL  请输入你的目标网站,http://www.example.com\n")

print("请输入数字选择你想要的选项\n")

print("扫描器功能选择:\n"
      "1:CMS简易识别\n"
      "2:CMS识别\n"
      "3:SQL注入检测\n"
      "4:端口服务状态扫描\n"
      "5:敏感目录检测[耗时久]\n"
      "6:子域名扫描\n"
      "7:网站指纹识别\n",
      "0:退出扫描器")
def Type_choice():
    print("请选择你想要爆破的类型\n")
    print(Senstive_label)
    Num=input('请输入一个数字\n')
    return int(Num)






while(1):
    choice=input('请输入数字\n')
    choice=int(choice)
    if choice==5:
        types=Senstive_label[Type_choice()]
        Senstive_Scan(url,types)
    elif choice==0:
        break
    elif choice==4:
        Work_Scan(host)
    elif choice==7:
        WhatWeb(url,host)
    else:
        function_choice[choice](url)

print("[*]------------DONE--------------")