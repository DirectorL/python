import json
import requests
import threading
num = 0
rs = requests.get(url="http://apissl.gifshow.com/rest/n/feed/hot?ll=&mod=HMD%20Global%28Nokia%20X7%29&appver=7.2.4.13202&isp=CMCC&lon=0&language=zh-cn&sys=ANDROID_9&max_memory=256&ud=0&egid=DFP7FC066E6E17FA8FFBCA4B3B2D3EFC9EEAD6F7684D50846452D422728DBA10&pm_tag=&oc=ALI_CPD%2C9&sh=2246&browseType=1&ddpi=420&extId=ad0daef758ef3e0503f8a5a1c0da9612&net=WIFI&socName=%3A%20Qualcomm%20Snapdragon%20710&lat=0&kcv=188&app=0&kpf=ANDROID_PHONE&ver=7.2&c=ALI_CPD%2C9&sw=1080&ftt=&kpn=KUAISHOU&country_code=cn&nbh=126&hotfix_ver=&did_gt=1586673320149&iuid=&sbh=86&did=ANDROID_dcbc9b109aca14bd&type=7&page=3&coldStart=false&count=20&pv=false&id=28&refreshTimes=26&pcursor=1&source=1&needInterestTag=false&seid=678680b0-f55c-4cd1-ac2e-a3b3a83a1cd5&volume=0.0&backRefresh=false&pageCount=28&adChannel=&passThrough=0&thanosSpring=false&newUserRefreshTimes=25&newUserAction=%7B%22click%22%3A%5B5234871642520114867%2C5245286216401956061%2C5221079368685776403%2C5194620719600593117%5D%2C%22follow%22%3A%5B%5D%2C%22like%22%3A%5B%5D%7D&os=android&sig=92cefa5516a781c2fe404e0c0a321a1b&client_key=3c2cd3f3&__NS_sig3=2204022259d8a2f4effe1b41fb49702a7f0925cf02").json()
def a():
    json_str = json.dumps(rs)  # 对数据进行编码。
    data = json.loads(json_str)  # 对数据进行解码。
    data_page = data["feeds"]  # json文本里feeds里的内容
    name = data_page[num]["user_name"]
    url = data_page[num]["main_mv_urls"][0]["url"]
    r = requests.get(url)
    content = r.content
    f = open(("videos/"+str(name)+".mp4"), "ab")
    f.write(content)
    f.close()
    print("_------------下载完毕------------_")
def c():
    for i in range(8):
        t = threading.Thread(target=a)
        t.start()
        global num
        num = num+1
if __name__ == "__main__":
    c()