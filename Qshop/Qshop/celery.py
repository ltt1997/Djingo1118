## 管理控制celery
import os
from celery import Celery
from django.conf import settings
os.environ.setdefault("DJANGO_SETTINGS_MODULE","Cmdb.settings")
## 实例化celery
app = Celery("art_project" )
# 加载celery设置
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda :settings.INSTALLED_APPS)











