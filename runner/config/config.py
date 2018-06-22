# -*- coding:utf-8 -*-

"""
File Name: `config`.py
Version:
Description:

Author: wangyongjun
Date: 2018/5/24 11:04
"""

import platform

if platform.system() == 'Windows':
    log_path = r'E:\git_mime\TestRunner\runner\logs\flask.log'
else:
    log_path = '/usr/local/src/logs/TestRunner/TestRunner.log'

db_connects = {
    "SIT": {
        "mock_service": "mysql+pymysql://autotestsit:Autotestsit@123@99.48.66.40:3306/mock_service?charset=utf8",
    },
    "ALIUAT": {
        "mock_service": "mysql+pymysql://autotestuat:Autotestuat@123@192.168.10.2:3306/mock_service?charset=utf8",
    }
}

default_env = "ALIUAT"

email_to = ['yongjun.wang@mi-me.com']