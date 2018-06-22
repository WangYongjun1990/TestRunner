# -*- coding:utf-8 -*-

"""
File Name: `http_runner`.py
Version:
Description:

Author: wangyongjun
Date: 2018/5/24 15:55
"""

import copy


class CaseRunner(object):
    def __init__(self, config_dict=None, http_client_session=None):
        self.http_client_session = http_client_session

        config_dict = config_dict or {}

    def init_config(self, testcase_dict):
        return copy.deepcopy(testcase_dict["request"])

    def run_test(self, testcase_dict):
        """
        :param testcase_dict: (dict)
            {
                "id": "1",
                "name": "testcase name",
                "variables": [],
                "request": {
                    "url": "http://99.48.58.31:6000/mock/queryMock",
                    "method": "POST",
                    "headers": {
                        "Content-Type": "application/json",
                    },
                    "body": '{"pageSize": 10, "currentPage": 1, "interfaceName": "test007", "projectName": "test"}',
                },
                "extract": [],
                "validate": [
                    {"eq": ["status_code", 200]},
                    {"eq": ["headers.Content-Type", "application/json"]},
                    {"eq": ["content.success", true]},
                    {"eq": ["content.msg", "user created successfully."]}
                ],
                "setup_hooks": [],
                "teardown_hooks": [],
            }
        :return:
        """
        parsed_request = self.init_config(testcase_dict)

        setup_hooks = testcase_dict.get("setup_hooks", [])
        self.do_hook_actions(setup_hooks)

        try:
            url = parsed_request.pop('url')
            method = parsed_request.pop('method')
        except KeyError:
            raise Exception

        # request
        resp = self.http_client_session.request(
            method,
            url,
            **parsed_request
        )

        print(url)

    def do_hook_actions(self, setup_hooks):
        pass




if __name__ == '__main__':
    case = {
                "id": "1",
                "name": "testcase name",
                "variables": [],
                "request": {
                    "url": "http://99.48.58.31:6000/mock/queryMock",
                    "method": "POST",
                    "headers": {
                        "Content-Type": "application/json",
                    },
                    "body": '{"pageSize": 10, "currentPage": 1, "interfaceName": "demo_post_json", "projectName": "ups"}',
                },
                "extract": [],
                "validate": [],
                "setup_hooks": [],
                "teardown_hooks": [],
            }

    cr = CaseRunner()
    cr.run_test(case)