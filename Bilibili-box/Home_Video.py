import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import debug_html
import re
import json as j



URL='https://www.bilibili.com/'
def useragent():
    #实例化UserAgent类
    #由于fack_useragent服务器位于国外，所以使用本地的文件
    headers = {'UserAgent': str(UserAgent(path="./useragent/agent.json").random)}
    return headers
def get_home(json:bool=True):
    resp=requests.get(URL).text
    soup=BeautifulSoup(resp,features='lxml')
    div=soup.find_all(attrs={"class":"video-card-reco"})
    debug_html.debug(str(soup))
    for link_info in div:
        link=re.findall('<a href="(.*?)" target=.*?>',str(link_info))[0]
        title=re.findall('<img alt="(.*?)"',str(link_info))[0]
        img=re.findall('src="(.*?)"/>',str(link_info))[0]
        a=re.findall('<i class="bilifont bili-icon_xinxi_UPzhu"></i>(.*?)</p><p class="play">(.*?)</p>',str(link_info))[0]
        up=a[0]
        play=a[1]
        video_info={
            'link':link,
            'title':title,
            'img':img,
            'up':up,
            'play':play
        }
        if json:
            yield j.dumps(video_info)
        else:
            yield video_info
