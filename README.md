# HitNews Python小程序
本程序可以根据网页页面元素持续查询检索信息并给予通知


## 外部依赖库
selenium
yagmail


## pipline注意事项

* 1，需配置浏览器组件（Win环境）
chromedriver.exe放置在chrome安装目录下，系统环境变量PATH添加chrome目录地址。（chromedriver.exe文件源码根目录下已提供，不必再下载）

* 2，发送QQ消息组件
需保持QQ对话窗口打开，保证句柄与程序中填写一致，具体可查看任务管理器

*3，发信程序配置
推荐QQ邮箱，在账户配置中打开发信功能，获取密钥，采用QQ邮箱+密钥形式而不要+密码


## 运行方式
1. 确保安装python3环境及各依赖库
2. 根据需要配置好pipline.py
3. 打开命令行工具（Win下如Powershell），cd到程序根目录。
4. 输入python .\pipline.py即可自动运行


---
驰妹QQ:80879464
个人网站：http://yingchi.io

**时间紧，仅仅快速出原型，复试完后将持续改进此程序。**




