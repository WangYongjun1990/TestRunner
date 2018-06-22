# -*- coding:utf-8 -*-

"""
File Name: `testHttpRunner`.py
Version:
Description:

Author: wangyongjun
Date: 2018/6/4 15:45
"""

from httprunner import HttpRunner

kwargs = {
    "failfast": False,
    # "dot_env_path": "/path/to/.env"
}
runner = HttpRunner(**kwargs)

testset = [
    {
        "name": "testset_name",
        "config": {
            "request": {
                "base_url": "http://99.48.58.241",
                "headers": {
                    "Content-Type": "application/json;charset=UTF-8"
                }
            },
            "variables": [
                {"pageSize": 1},
                {"currentPage": 1}
            ],
            "parameters": [],
            "name": "testset description"
        },
        "testcases": [
            {
                "request": {
                    "json": {},
                    "url": "/mock/config/queryProject",
                    "headers": {"Content-Type": "application/json"},
                    "method": "POST"
                },
                "extract": [
                    {
                        "mockName": "content.desc.ups.0"
                    }
                ],
                "validate": [
                    {
                        "eq": [
                            "status_code",
                            200
                        ]
                    },
                    {
                        "eq": [
                            "headers.Content-Type",
                            "application/json"
                        ]
                    },
                    {
                        "eq": [
                            "content.code",
                            "000"
                        ]
                    }
                ],
                "variables": [],
                "name": "queryProject"
            },
            {
                "request": {
                    "json": {
                        "pageSize": "$pageSize",
                        "interfaceName": "demo_post_json",
                        "currentPage": "$currentPage",
                        "projectName": "ups",
                        "op": "$mockName"
                    },
                    "url": "/mock/config/queryMock",
                    "headers": {},
                    "method": "POST"
                },
                "extract": [
                    {
                        "tableData": "content.tableData"
                    }
                ],
                "validate": [
                    {
                        "eq": [
                            "status_code",
                            200
                        ]
                    },
                    {
                        "eq": [
                            "headers.Content-Type",
                            "application/json"
                        ]
                    },
                    {
                        "eq": [
                            "content.code",
                            "100"
                        ]
                    }
                ],
                "variables": [],
                "name": "queryMock"
            }
        ]
    }
]

# runner.run(r"E:\git_mime\TestRunner\case_list.pretty.json")
runner.run(testset)
summary = runner.summary
print(summary)
runner.gen_html_report(
    html_report_name="demo",
)