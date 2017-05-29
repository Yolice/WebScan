from config import HEADER,Senstive_list,SubDomain_list
from ip_proxy import find_ipproxy
import requests
import multiprocessing



def Senstive_Scan(target_url,types):
    print("[*]--------可查询到的敏感目录为--------")
    Senstive_list=[]
    proxies=find_ipproxy()
    _dict=open(r'/Users/yohane/Documents/defoliation/data/{}.txt'.format(types))
    try:
        while True:
            dict_name=_dict.readline().replace('\n','')
            if len(dict_name)==0:
                print("[*]--------字典已到末尾--------")
                print(Senstive_list)
                break
            link_url=target_url+dict_name
            status_code=requests.get(url=link_url,headers=HEADER,proxies=proxies,timeout=5).status_code
            urls=requests.get(url=link_url,headers=HEADER,proxies=proxies,timeout=5).url
            if status_code not in [400,404,500,502]:
                print(urls)
                Senstive_list.append(urls)
    except:
        pass
    _dict.close()

def SubDomain_Scan(target_host):
    print("[*]--------可查询到的子域名为--------")
    proxies=find_ipproxy()
    SubDomain_list=[]
    SubDomain_dict=open(r'/Users/yohane/Documents/defoliation/data/subdomain_dict.txt')
    try:
        while True:
            dict_name=SubDomain_dict.readline().replace('\n','')
            if len(dict_name)==0:
                print("[*]--------字典已到末尾--------")
                print(SubDomain_list)
                break
            link_url='http://'+dict_name+'.'+target_host
            status_code=requests.get(url=link_url,headers=HEADER,proxies=proxies,timeout=5).status_code
            urls=requests.get(url=link_url,headers=HEADER,proxies=proxies,timeout=5).url
            if status_code not in [400,404,500,502]:
                print(urls)
                SubDomain_list.append(urls)
    except Exception as e:
        #print(e)
        pass
    SubDomain_dict.close()

    print("[*]--------扫描完毕 --------")


