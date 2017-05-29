from config import HEADER
from bs4 import BeautifulSoup
import random
import requests
import re


def find_ipproxy():
    ip_proxy_url=['http://cn-proxy.com','http://www.xicidaili.com/','http://www.coobobo.com']
    ip_Gene=[]
    web_data=requests.get(ip_proxy_url[0],headers=HEADER)
    web_data.encoding='utf-8'
    soups=BeautifulSoup(web_data.text,'lxml')
    port_list=soups.find_all(string=re.compile("^[80-65535]{1,4}$"))
    ip_list=soups.find_all(string=re.compile("^\d{1,3}\."))
    for ip,port in zip(ip_list,port_list):
        proxys=ip+":"+port
        ip_Gene.append(proxys)
    for proxy_address in ip_Gene:
        proxies_test={
            "http":"http://{}".format(proxy_address)
        }
        try:
            requests.get(url=target_url,headers=HEADER,proxies=proxies_test,timeout=3)
        except:
            ip_Gene.remove(proxy_address)
    proxies={
        "http":"http://{}".format(random.choice(ip_Gene))
    }
    return proxies




