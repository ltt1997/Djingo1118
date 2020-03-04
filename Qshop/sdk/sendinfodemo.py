# import requests
# ## 短信请求地址
# url = "https://106.ihuyi.com/webservice/sms.php?method=Submit"
# ## APIID
# account = "C20639973"
# ## APIkey
# password = "47b76af402cc76218faa715a97fe5d11"
# # 接收人手机号
# mobile = "17513275362"
# ## 发送内荣
# content = "您的验证码是：1234。请不要把验证码泄露给其他人。"
# # 请求头
# headers = {
#     "Content_type":"application/x-www-form-urlencoded",
#     "Accept": "text/plain"
# }
#
# data = {
#     "account":account,
#     "password":password,
#     "mobile":mobile,
#     "content":content
# }
#
# response = requests.post(url,headers = headers,data=data)
#
# print(response.content.decode())


import requests
## 短信请求地址
url = "http://106.ihuyi.com/webservice/sms.php?method=Submit"
#APIID
account = "C20639973"
#APIkey
password = "47b76af402cc76218faa715a97fe5d11"
## 接收人手机号
mobile = "17812325270"
## 发送内容
content = "您的验证码是：1234。请不要把验证码泄露给其他人。"
## 请求头
headers = {
    "Content-type": "application/x-www-form-urlencoded",
    "Accept": "text/plain"
}
## 请求数据
data = {
    "account": account,
    "password": password,
    "mobile": mobile,
    "content": content,
}
## 发送请求
response = requests.post(url,headers = headers,data=data)
    #url 请求地址
    #headers 请求头
    #data 请求数据
print(response.content.decode())