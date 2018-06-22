# -*- coding:utf-8 -*-

"""
File Name: `http_client`.py
Version:
Description:

Author: wangyongjun
Date: 2018/5/29 18:17
"""

import re
import time

import requests
import urllib3
from requests import Request, Response
from requests.exceptions import (InvalidSchema, InvalidURL, MissingSchema,
                                 RequestException)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

absolute_http_url_regexp = re.compile(r"^https?://", re.I)

from decimal import *

if __name__ == '__main__':
    a = 10.0
    b = 10.0000000000000001

    print(type(a))
    assert a == b

    print(20/3.0)


