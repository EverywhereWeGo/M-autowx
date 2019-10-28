# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr

my_sender = '964353527@qq.com'  # 发件人邮箱账号
my_pass = 'jnyeaedxdwbsbefj'  # 发件人邮箱密码(当时申请smtp给的口令)
my_user = '964353527@qq.com'  # 收件人邮箱账号，我这边发送给自己


def mail(context):
    try:
        msg = MIMEText(context, 'plain', 'utf-8')
        msg['From'] = formataddr(["发件人昵称", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["收件人昵称", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = "新信息"  # 邮件的主题，也可以说是标题

        server = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 发件人邮箱中的SMTP服务器，端口是465
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, [my_user, ], msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
        print("发送成功")
    except Exception:
        print("发送失败")
