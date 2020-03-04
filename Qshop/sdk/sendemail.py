import smtplib
from django.http import JsonResponse
from email.mime.text import MIMEText
def sendemail(params):
    """

    :param params={
        "subject": 标题
        "content": 内容
        "recver": 收件人
    }
    :return:
    """
    ##构建邮件内容
    subject = params.get("subject")
    content = params.get("content")
    sender = 'ltt_py@163.com'
    recver = """{}""".format(params.get("recver"))
    password = 'ltt1997'
    message = MIMEText(content,'plain','utf-8')
    """
    _text, 内容
    _subtype='plain', 内容类型 文本
     _charset=None  编码格式
    """
    message['Subject'] = subject # 主题
    message['From'] = sender # 发件人
    message['To'] = recver  # 收件人

    try:
          ## 授权码 不是密码
        ## 登录邮件服务器
        smtp = smtplib.SMTP_SSL("smtp.163.com",465)
        ## 登录
        smtp.login(sender,password)
        smtp.sendmail(sender,recver.split(","),message.as_string())
        #  sender 发件人
        #  recver 收件人，可以是列表
        #  message  邮件内容
        #  as_string()  方法和join方法类似
        res = {"code":10000,"msg":"验证码发送成功"}

    except:
        res = {"code": 10001, "msg": "验证码发送失败"}
    finally:
        smtp.close()


    return JsonResponse(res)








