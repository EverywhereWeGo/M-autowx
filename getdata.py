# -*- coding: utf-8 -*-
import time
from threading import Timer

import requests
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')

from mail import mail

oldstatus = ["4432072237827758",
             "4432047051360708",
             "4431734302623863",
             "4431733091279116",
             "4431060550860686",
             "4430993596876596",
             "4430682749117386",
             "4428750211387049",
             "4428439836730962",
             "4428375302848802"]


def gethttp():
    response = requests.post('https://m.weibo.cn/profile/info?uid=3687300407')
    # byte转str
    result = response.content.decode('utf-8')

    # str转json
    all_news = json.loads(result)

    infos = all_news["data"]["statuses"]
    print(infos)
    return infos


def get_news():
    infosaaa = gethttp()
    # 遍历由json数据得到的list
    for info in infosaaa:
        text = info["text"]
        id = info["id"]
        if id not in oldstatus:
            print(text)
            oldstatus.append(id)
            # mail(text)
    print oldstatus


if __name__ == "__main__":
    while True:
        get_news()
        time.sleep(60 * 60)
