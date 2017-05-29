from config import CMS_list,HEADER,Site_info
from bs4 import BeautifulSoup
import requests
import json
import hashlib
import multiprocessing
import re




def CMS_Scan_Simple(target_url):
    web_data=requests.get(url=target_url,headers=HEADER).text
    web_robots=requests.get(target_url+'/robots.txt',headers=HEADER).text
    Select_Gene=BeautifulSoup(web_data,'lxml')
    GeneratorTag=Select_Gene.find_all('meta',attrs={"name":'generator'})


    if GeneratorTag:
        for Cms in CMS_list:
            if Cms in str(GeneratorTag):
                Site_info["CMS"]=Cms
                print("[*]--------已扫到CMS为 "+Cms+" --------")



    else:
        for Cms in CMS_list:
            if Cms in web_robots + web_data:
                Site_info["CMS"]=Cms
                print("[*]--------已扫到CMS为 "+Cms+" --------")

    print("[*]--------扫描完毕 --------")





def CMS_Scan_Complex(target_url):
    cms_file=open(r'/Users/yohane/Documents/defoliation/data/data.json')
    json_info=json.load(cms_file,encoding='utf-8')


    for info in json_info:
        status=requests.get(url=target_url+info['url'],headers=HEADER).status_code


        if status != 200:
            continue



        cms_analysis=requests.get(url=target_url+info['url'],headers=HEADER).text
        Encode_Text=cms_analysis.encode('utf-8')
        if cms_analysis == None:
            continue

        REG=re.compile(info['re'])
        Results=REG.findall(cms_analysis)
        if Results:
            Site_info['CMS']=info['name']
            print("[*]--------已扫到CMS为 "+info['name']+" --------")
            return

        else:
            GeneMd5=hashlib.md5()
            GeneMd5.update(Encode_Text)
            if info['md5']==GeneMd5.hexdigest():
                Site_info['CMS']=info['name']
                print("[*]--------已扫到CMS为 "+info['name']+" --------")
                return

    cms_file.close()
    print("[*]--------扫描完毕 --------")






