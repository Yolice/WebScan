from config import HEADER,Site_info,IP_INFO
import requests
import os
import re
from bs4 import BeautifulSoup


def WhatWeb(target_url,target_host):
    web_headers=requests.get(url=target_url,headers=HEADER).headers
    Site_info["Server"]=web_headers["Server"]
    if web_headers.get("X-Powered-By"):
        Site_info["Other"]=web_headers["X-Powered-By"]
    Nslookup_info=os.popen('nslookup {} 8.8.4.4'.format(target_host)).read()
    Ping_info=os.popen('ping -c 3 {}'.format(target_host)).read()
    IP_Reg=re.compile("\d+\.\d+\.\d+\.\d+")
    Find_IP=list(set(IP_Reg.findall(Ping_info+Nslookup_info)))
    Find_IP.remove('8.8.4.4')
    for ip in Find_IP:
        data_list={
            "s":ip,
            "vcode":"h2o2"
        }
        try:
            Geo_ip=requests.post(url="http://q.ip5.me/q.php",data=data_list,headers=HEADER).text
            Ip_pos=BeautifulSoup(Geo_ip,'lxml').find_all('div',id="ip_pos")
            for postion in Ip_pos:
                IP_INFO.append(ip+'/'+postion.get_text())
        except Exception as e:
          print("IP地址查询失败")
          #print(e)
    if IP_INFO:
        Site_info["IP_INFO"]=IP_INFO
        print("[*]IP信息为 "+str(IP_INFO)+"  -")



    print("[*]--------扫描完毕 --------")