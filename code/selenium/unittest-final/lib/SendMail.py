import yagmail

class SendMail:
    def __init__(self,report):
        #连接邮箱服务器
        yag = yagmail.SMTP(user="qiushicumt@126.com", password="Zqs021713", host='smtp.126.com')
        #主题
        subject=['ShopXO项目自动化测试报告']
        #邮箱正文
        contents = ['领导，您好。附件为此轮自动化测试报告，请查看']
        # 发送邮件
        yag.send('516660797@qq.com', subject, contents,report)

