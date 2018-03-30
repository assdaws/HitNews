# coding=utf-8
from selenium import webdriver
import time
import re
import yagmail
import win32gui
import win32con
import win32clipboard as w


def sendmail():
    # 链接邮箱服务器
    yag = yagmail.SMTP(user="80879464@qq.com", password="jbayqoecbrtzbgii", host='smtp.qq.com')
    # 邮箱正文
    mail_contents = ['西工大软微拟录取通知已发布！',
                     '请去官网查看！', '——驰妹提醒']
    # 发送邮件
    yag.send('80879464@qq.com', '驰妹提醒：西工大软微拟录取通知已发布！', mail_contents)


def getText():
    """获取剪贴板文本"""
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_UNICODETEXT)
    w.CloseClipboard()
    return d


def setText(aString):
    """设置剪贴板文本"""
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT, aString)
    w.CloseClipboard()


def send_qq(to_who, msg):
    """发送qq消息
    to_who：qq消息接收人
    msg：需要发送的消息
    """
    # 消息写到剪贴板
    setText(msg)
    # 获取qq窗口句柄，驰妹提醒：可以进任务管理器查看具体句柄
    qq = win32gui.FindWindow(None, to_who)
    # 投递剪贴板消息到QQ窗体
    win32gui.SendMessage(qq, 258, 22, 2080193)
    win32gui.SendMessage(qq, 770, 0, 0)
    # 模拟按下回车键
    win32gui.SendMessage(qq, win32con.WM_KEYDOWN, win32con.VK_RETURN, 0)
    win32gui.SendMessage(qq, win32con.WM_KEYUP, win32con.VK_RETURN, 0)


def sendqqmsg():
    # 通知发布后QQ消息通知
    to_who = '19西工大软件工程考研'
    # msg = '#test'
    msg = '#Python程序自动发布#驰妹提醒：西工大软微官网拟录取通知有更新！请前往关注！http://rjwdz.nwpu.edu.cn/rcpy/yjspy.htm'
    send_qq(to_who, msg)
    return


def sendmail():
    # 链接邮箱服务器
    yag = yagmail.SMTP(user="80879464@qq.com", password="jbayqoecbrtzbgii", host='smtp.qq.com')
    # 邮箱正文
    mail_contents = ['西工大软微拟录取通知已发布！',
                     '请去官网查看！', '——驰妹提醒']
    # 发送邮件
    yag.send('80879464@qq.com', '驰妹提醒：西工大软微拟录取通知已发布！', mail_contents)


browser = webdriver.Chrome()
browser.get("http://rjwdz.nwpu.edu.cn/rcpy/yjspy.htm")
counter = 0

while 1:
    find = browser.find_elements_by_class_name("article-list")
    for tag in find:
        print(tag.text)
        text = tag.text

        # 正则表达式匹配
        r_pattern = r'拟录取'  # 此处修改需要的匹配字符串
        matchObj = re.search(r_pattern, text, re.M | re.I)
        if matchObj:
            # print('match --> matchObj.group() : ' + matchObj.group())
            print('****** 发现匹配项：' + r_pattern + ' ******')

            sendqqmsg()  # QQ提醒
            print("**** QQ提醒完成 ****")

            # sendmail() # 邮件提醒
            # print("**** 邮件提醒完成 ****")

            break

    counter = counter + 1
    print('查询次数统计：' + str(counter))

    if matchObj:
        print('已找到相关内容，跟踪结束')
        break
    browser.refresh()
    time.sleep(4)
