# -*- coding:utf-8 -*-

"""
File Name: `manage`.py
Version:
Description:

Author: wangyongjun
Date: 2018/5/24 11:36
"""

from runner import app

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=7000, debug=True)