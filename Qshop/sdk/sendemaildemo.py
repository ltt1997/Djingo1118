import smtplib
from email.mime.text import MIMEText

##构建邮件内容
subject = "爱你"
content = '么么哒'
sender = 'ltt_py@163.com'
recver = """765908052@qq.com,2268607031@qq.com"""
message = MIMEText(content,'plain','utf-8')
"""
_text, 内容
_subtype='plain', 内容类型 文本
 _charset=None  编码格式
"""
message['Subject'] = subject # 主题
message['From'] = sender # 发件人
message['To'] = recver  # 收件人


password = 'ltt1997'  ## 授权码 不是密码
## 登录邮件服务器
smtp = smtplib.SMTP_SSL("smtp.163.com",465)
## 登录
smtp.login(sender,password)
smtp.sendmail(sender,recver.split(","),message.as_string())
#  sender 发件人
#  recver 收件人，可以是列表
#  message  邮件内容
#  as_string()  方法和join方法类似
smtp.close()











