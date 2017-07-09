# -*- coding: utf-8 -*-

import send_task
from config import USER_NAME, PASSWD
from weibo.new_login import login
from weibo import weibo_login

if __name__ == '__main__':
    http, uid = login(username=USER_NAME, password=PASSWD)
    # (http, uid) = weibo_login.wblogin()
    http.get('http://weibo.com/')
    task =  send_task.SendTask(http, uid)
    task.start()
    # task.stop()
    