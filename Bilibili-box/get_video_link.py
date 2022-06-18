import json
import re  # 正则表达式

import requests

from Home_Video import useragent

headers=useragent()

def get_video_links(url:str):
    html_data=requests.get(url,headers).text
    json_data = re.findall('<script>window\.__playinfo__=(.*?)</script>', html_data)[0]
    json_data = json.loads(json_data)
    audio_url = json_data['data']['dash']['audio'][0]['backupUrl'][0]
    video_url = json_data['data']['dash']['video'][0]['backupUrl'][0]
    video_data={
        'video_data':video_url,
        'audio_data':audio_url
    }
    return json.dumps(video_data)
