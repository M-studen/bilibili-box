# get_video_link

该模块用于获取某个视频链接的视频以及音频地址

## get_video_links

该函数需要一个str类型的url参数该参数只可以是视频地址

例如

`https://www.bilibili.com/video/BV1CA4y1o74Z`

返回值为一个json类型

如下：



| 参数       | 解释     |
| ---------- | -------- |
| video_data | 视频地址 |
| audio_data | 音频地址 |

## 注意

在请求视频地址会遇到`403没有权限`的问题，这是因为在请求之前需要先向该地址发送一个`OPTION`请求，请求的`headers`中需要`referer`和`range`两个参数其中`range`这个参数可以省略,`referer`

这个参数就是要请求的url

详细可以看一下这篇文章

[如何使用Python爬取bilibili视频（详细教程） - 知乎 (zhihu.com)](https://zhuanlan.zhihu.com/p/148988473)

其中的ffmpeg用来合并音频数据