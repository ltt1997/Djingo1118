"""
Django settings for Qshop project.

Generated by 'django-admin startproject' using Django 2.2.1.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'e#2(s*)q!^9us*%ev+$f#la#5t@hd9&5g(+(h=+1swld63=#vf'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Buyer',
    'Buyer.templatetags',
    'Sheller',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'Qshop.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Qshop.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':'qshop',
        'USER':'root',
        'PASSWORD':'123456',
        'HOST':'127.0.0.1',
        'PORT':'3306'
        ''
    }
}








# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = False


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

# STATIC_ROOT = os.path.join(BASE_DIR,'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'static')


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
