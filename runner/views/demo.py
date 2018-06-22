# -*- coding:utf-8 -*-

"""
File Name: `demo`.py
Version:
Description:

Author: wangyongjun
Date: 2018/5/24 11:01
"""

import json
import time

from flask import Blueprint
from flask_restful import Resource
from flask import request
from flask import jsonify

from runner.api.comm_log import logger

# 蓝图
demo = Blueprint('demo_interface', __name__)


class Demo(Resource):
    def __init__(self):
        pass

    def post(self, case_id):
        data = request.get_json()
        logger.info(case_id)
        try:
            env = data['env']
        except TypeError as e:
            env = None
        results = operate_db('mock_service', "SELECT output_msg FROM mock_service.mock_info WHERE interface_name='{}';".format(task_id))
        logger.info(results)
        if results:
            output_msg = results[0][0]
            response = jsonify(json.loads(output_msg))
        else:
            response = jsonify(
                {"code": "000", "message": u"测试一下，demo all right", "result": env, "task_id": task_id}
            )

        logger.info(response)

        return response