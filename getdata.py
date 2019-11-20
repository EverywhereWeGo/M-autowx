# -*- coding: utf-8 -*-
import time
import requests
import json
import sys
from mail import mail

reload(sys)
sys.setdefaultencoding('utf-8')


def read_file(filepath):
    with open(filepath) as fp:
        content = fp.read()
    return content


def append_file(filepath, content):
    with open(filepath, 'a') as af:
        af.write(content + '\n')


def gethttp():
    response = requests.post('https://m.weibo.cn/profile/info?uid=7136225579')
    # response = requests.post('https://m.weibo.cn/profile/info?uid=3687300407')
    # response = requests.post('https://m.weibo.cn/profile/info?uid=5556273965')

    # byte转str
    result = response.content.decode('utf-8')
    # str转json
    all_news = json.loads(result)
    infos = all_news["data"]["statuses"]
    return infos


def get_news():
    infosaaa = gethttp()
    oldstatus = read_file("code.txt")
    # 遍历由json数据得到的list
    for info in infosaaa:
        idnum = info["id"]
        if idnum not in oldstatus:
            # 动态内容
            text = info["text"]

            # 动态图片
            picurl = []
            if "pics" in info.keys():
                for pic in info["pics"]:
                    picurl.append(pic["large"]["url"])

            # 转发内容
            retweeted = ''
            if "retweeted_status" in info.keys():
                retweeted = (info["retweeted_status"]["text"])

            # 发送
            print("正文:\n\t" + text + "\n图片:\n\t" + "\n\t".join(picurl) + "\n转发:\n\t" + retweeted)
            append_file('code.txt', idnum)
            mail("正文:\n\t" + text + "\n图片:\n\t" + "\n\t".join(picurl) + "\n转发:\n\t" + retweeted)


if __name__ == "__main__":
    while True:
        try:
            get_news()
        except BaseException as e:
            print(e.message)
        time.sleep(10 * 60)
