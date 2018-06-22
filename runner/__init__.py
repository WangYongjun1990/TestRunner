# -*- coding:utf-8 -*-

"""
File Name: `__init__.py`.py
Version:
Description:

Author: wangyongjun
Date: 2018/5/24 10:55
"""
# flask
from flask import Flask
from flask_restful import Api

# mysql
from runner.models.mysql_orm import mysql_db

# blueprint
from runner.views.demo import Demo, demo

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 让jsonify的返回直接显示中文


app.register_blueprint(demo)

view = Api(app)
view.add_resource(Demo, '/runner/demo/<case_id>')

# mysql_db.init_app(app)
