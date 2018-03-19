#coding=utf-8
from selenium import webdriver
import time
import yagmail
import qqMsg

# 配置浏览器组件
browser = webdriver.Chrome()
browser.get("http://rjwdz.nwpu.edu.cn/rcpy/yjspy.htm")

counter = 1

while 1:
# 根据页面元素检索需要定位的新闻标签
    find = browser.find_element_by_class_name("date").text # 查询data类标签
    if find == "2018/03/19": 
        browser.quit()
        break
    else:
        print("驰妹提醒：消息未更新")
        print("3月17日复试通知还未发布，请等待")
        print("查询次数统计：" + str(counter))
        counter = counter + 1

    browser.refresh() # 浏览器刷新
    time.sleep(2)

# 通知发布后QQ消息通知
print("驰妹提醒：通知已发布！请去官网查看！！")
to_who = '18西工大软件工程复试'
msg = '#Python程序自动发布#驰妹提醒：西工大软微官网有更新!请前往关注！http://rjwdz.nwpu.edu.cn/rcpy/yjspy.htm'
send_qq(to_who, msg)



# 通知发布后邮件通知，注意：发信收信邮箱自己配置并填写

#参数1：发信邮箱 参数2：发信密钥，不一定是账户密码 参数3：发信服务器
yag = yagmail.SMTP(user="        ", password="        ", host='smtp.qq.com') 
contents = ['西工大软微复试通知已发布！',
            '请去官网查看！', '——驰妹提醒']
# 参数1：收信邮箱           
yag.send('        ', '驰妹提醒：西工大软微复试通知已发布！', contents)  


# 循环提醒
while 1:
    print("新通知提醒已发出！http://rjwdz.nwpu.edu.cn/rcpy/yjspy.htm")
    time.sleep(5)