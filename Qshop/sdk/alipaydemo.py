## 支付宝demo
## 公钥
alipay_public_key_string = """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAqB+q0ucS76mOYRgq1H4WLpqyXRpmi8F9NzG3/gfoleUt64w/iJZpVhYWB1D7uDhTQD2XENctMdca+4HlJ3UXQAAyb8Zbt1PcX6ykTNFv8jGmDLLVv43iEozsMiYnxOqEiGL6Z82unUYA4nVZ3Ngmj69Vpl+0XaBUgf2n5M/0dyPh/Lv3tMfKSH8cQkWXFkzlWxFtcjtTe65qB6CMX1JI4hCyck9KBQFCDDulsjeQ1jTCLptBKoj+3rf59wSyQ0uoLV5gW12IuY9EwWrXAyaXNXSVNYlTjZpumKEysLuFUnUNv5rUYdzPT24W0TQdlSx6cbIpqw2gAmFQHJBMZiHaiwIDAQAB
-----END PUBLIC KEY-----"""
## 私钥
app_private_key_string = """-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAqB+q0ucS76mOYRgq1H4WLpqyXRpmi8F9NzG3/gfoleUt64w/iJZpVhYWB1D7uDhTQD2XENctMdca+4HlJ3UXQAAyb8Zbt1PcX6ykTNFv8jGmDLLVv43iEozsMiYnxOqEiGL6Z82unUYA4nVZ3Ngmj69Vpl+0XaBUgf2n5M/0dyPh/Lv3tMfKSH8cQkWXFkzlWxFtcjtTe65qB6CMX1JI4hCyck9KBQFCDDulsjeQ1jTCLptBKoj+3rf59wSyQ0uoLV5gW12IuY9EwWrXAyaXNXSVNYlTjZpumKEysLuFUnUNv5rUYdzPT24W0TQdlSx6cbIpqw2gAmFQHJBMZiHaiwIDAQABAoIBABR/3/1dTZLJcuHl53sHcL73/92YVX6e9hyfxFaGMlbsnd/Ftw15gZiMkt0Lg9XfkE8Z82yLQCh+mPynxwA7p70XCQ9V+WLuJ8XGsDXpp6O5aAzOVX/I1hL6+eXXfyvkiIp0vyGfE7Z7jaoPMwjZlkIY1/G0Y7Ky1PsQqcMdlCpek6pXYysa7XL4Vsa/rjaV5efcFYKpj2dIbRZjakc78OEV7nbqwZuLjHqDHBPWFEOTQvhWn2mI1bZwIz2l70bCQ8cUALXy0vUOTm9Jj2NZCTou4+1JL76Vw/OEQn7cflCD44A5f4Vj3LKSAonV/6ZA9cKUC3OytpDETo3Bj95d7rkCgYEA7PN4y530JiYyl6HhcLGrnXSLpgcHJdjsuARqFgEqA6c3esM2zKEBVLtnsIG3D5eW4kPkx5RrAuBXd/OJd+m5IW1cs/aXyelU/nq3n6+ogpMoqC4RFw/EO0itYDtk+WGb+FWBmcPAJCMrV7+tG54lrWHwbIegtOqnmuBPejcZTbcCgYEAtaO02g+lx6IY8rtJbuHSwsQ2WYsT0duHqo3ZP4iIsf3LO2/hqMowjpVNWwBxYXGiHjUtdvyHR2XTftlQ+Y0BQf1c0p08Hx4ZSzDR0ijGXhXpL/Ji5jnO0KHcoKujt0DV4Sj4JNYx36qGLcIHXExqRcGQJWRTP7+hYeAlWJv2Wc0CgYA5/yn85K+Cuuy9MpFEjShNRN59h9DXEa53KBVzR1uqQz6QHMIH+gyiWbB6gnV1Koxy211fAFPlA1ZFdOWb5Sg8J1F+dwgWEreMBit1uYAMXcqgx43FUEWeoR5WpJMFez+62+r54PDhp34PX0oWrXHZa1R2rAfI4HqfrPGnH19hJwKBgB7jlRjUOmQFq+pzcRx7KMVYasm1fgxdIegeMUi9pklmmI4mC6ERqUpGF56XJ7DjiydJ8c5fSX4Z0eqreDrIAOPA+20Rsiy0iKahybzMlFdhsIMn3Cu8vu/55rQoHDJIw1aEChbxmg+oRyM28NuAXz43mZTSR9n6c65aWN+FvlItAoGBANhOuYen2148lk5li6nNrlkleKzFniY7QYs0qaxIwLizd+Uc+Y0jJm9r2J7uPqYEu0A/GPvIaN6Ab4Hd1ZysNF9bkbK1GguYNUtgdBJw304TDlYnxvMzKWFYC/fqVNRn2jx7Qv0c82S4ZqlFsN5+4oOS1Pw7IM9vRwKrl9tBLn0a
-----END RSA PRIVATE KEY-----"""





## 导包
from alipay import AliPay

## 实例化
alipay = AliPay(
        appid = '2016101800717535',
        app_notify_url=None,
        app_private_key_string=app_private_key_string,
        alipay_public_key_string=alipay_public_key_string,
        sign_type="RSA2",
        debug=False
)

## 创建一个订单
order_str = alipay.api_alipay_trade_page_pay(
    subject='py交易',
    out_trade_no = '347213462183641',
    total_amount = '10000',
    return_url=None,
    notify_url=None
)

res = 'https://openapi.alipaydev.com/gateway.do?' + order_str
print(res)




