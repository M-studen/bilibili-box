import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup



URL='https://www.bilibili.com/'
def useragent():
    #实例化UserAgent类
    #由于fack_useragent服务器位于国外，所以使用本地的文件
    headers = {'UserAgent': str(UserAgent(path="./useragent/agent.json").random)}
    return headers
def get_home(headers):
    resp=requests.get(URL).text
    soup=BeautifulSoup(resp,features='lxml')
    div=soup.find_all(attrs={"data-report":"b_7265636f6d6d656e64.10"})
    print(soup)
headers=useragent()
get_home(headers)
#<div '

#
#
#