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
    response = requests.post('https://m.weibo.cn/profile/info?uid=7136225579')
    # response = requests.post('https://m.weibo.cn/profile/info?uid=3687300407')
    # response = requests.post('https://m.weibo.cn/profile/info?uid=5556273965')

    # byte转str
    result = response.content.decode('utf-8')

    # str转json
    all_news = json.loads(result)
    print(type(all_news))
    print(all_news)

    infos = all_news["data"]["statuses"]
    print(infos)
    return infos


def get_news():
    infosaaa = gethttp()
    # 遍历由json数据得到的list
    for info in infosaaa:
        text = info["text"]

        picurl = []
        if "pics" in info.keys():
            for pic in info["pics"]:
                # print(pic["large"]["url"])
                picurl.append(pic["large"]["url"])

        retweeted = []
        if "retweeted_status" in info.keys():
            print (info["retweeted_status"]["text"])
            retweeted.append(info["retweeted_status"]["text"])

        id = info["id"]
        if id not in oldstatus:
            print(text + str(picurl) + str(retweeted))
            oldstatus.append(id)
            mail(text + str(picurl) + str(retweeted))
    print oldstatus


if __name__ == "__main__":
    while True:
        get_news()
        time.sleep(10 * 60)
