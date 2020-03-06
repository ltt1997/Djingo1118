## 用于编写任务
from __future__ import absolute_import
from Qshop.celery import app

@app.task
def test():
    print("hello world")


