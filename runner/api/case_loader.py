# -*- coding:utf-8 -*-

"""
File Name: `case_loader`.py
Version:
Description:

Author: wangyongjun
Date: 2018/5/24 15:56
"""
import re

variable_regexp = r"\${([\w_]+)}"


def extract_variable(content):
    """
    :param content: (str)
    :return: (list)

    e.g. ${var} => ['var']
         ${var_1}/${var_2}/$token => ['var_1', 'var_2']
         abc => []
    """
    try:
        return re.findall(variable_regexp, content)
    except TypeError:
        print('011')
        return []

if __name__ == '__main__':
    res = extract_variable('${var_1}/${var_2}/$token')
    print(res)