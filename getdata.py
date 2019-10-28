# -*- coding: utf-8 -*-
from threading import Timer

import requests
import json

from mail import mail

oldstatus = ["q", \
             "4432047051360708", \
             "4431734302623863", \
             "4431733091279116", \
             "4431060550860686", \
             "4430993596876596", \
             "4430682749117386", \
             "4428750211387049", \
             "4428439836730962", \
             "4428375302848802"]
response = requests.post('https://m.weibo.cn/profile/info?uid=7136225579')
# byte转str
result = response.content.decode('utf-8')

# str转json
all_news = json.loads(result)

infos = all_news["data"]["statuses"]
print(infos)


def get_news():
    # 遍历由json数据得到的list
    for info in infos:
        text = info["text"]
        id = info["id"]
        if id not in oldstatus:
            print(text)
            oldstatus.append(id)
            # mail(text)


if __name__ == "__main__":
    t = Timer(1 * 60, get_news)
    t.start()
