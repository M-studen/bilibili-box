# *Home_Video.py文件函数介绍*

## useragent

通过fake_useragent模块获取浏览器ua

由于服务器位于国外访问不稳定，所以使用本地/useragent/ua.json里的信息

可以随时更新，更新网址：
<https://fake-useragent.herokuapp.com/browsers/0.1.11>

后面的0.1.11是模块的版本号，可改变

## get_home

 



获取主页的视频信息

参数 `json`布尔类型是否返回json数据，默认为True，否则返回dict数据

返回值信息：

返回一个Generator对象，需要使用`next`方法


| 返回参数 |     参数介绍 |
| -------- | -----------: |
| link     | 返回视频链接 |
| img      | 返回封面地址 |
| up       |     返回作者 |
| play     |   返回播放量 |

