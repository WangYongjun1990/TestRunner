# -*- coding:utf-8 -*-

"""
File Name: `mysql_orm`.py
Version:
Description:

Author: wangyongjun
Date: 2018/5/24 11:23
"""

from flask_sqlalchemy import SQLAlchemy

mysql_db = SQLAlchemy()


class CAAccount(mysql_db.Model):
    __bind_key__ = "credit_audit"
    __tablename__ = "CA_APPL_ACCOUNT"
    APPL_NO = mysql_db.Column(mysql_db.VARCHAR(64), primary_key=True)
    ACCOUNT_NO = mysql_db.Column(mysql_db.VARCHAR(64))
    REGISTER_TIME = mysql_db.Column(mysql_db.VARCHAR(64))
    REGISTER_MOBILE = mysql_db.Column(mysql_db.VARCHAR(64))
    BIND_MOBILE = mysql_db.Column(mysql_db.VARCHAR(64))
    SEX = mysql_db.Column(mysql_db.VARCHAR(16))
    BIRTHDAY = mysql_db.Column(mysql_db.VARCHAR(64))
    CREATE_TIME = mysql_db.Column(mysql_db.DateTime)


class ModelService(mysql_db.Model):
    __bind_key__ = "model_service"
    __tablename__ = "model_service_test"
    id = mysql_db.Column(mysql_db.Integer, primary_key=True)
    example = mysql_db.Column(mysql_db.VARCHAR(64))
    APPL_NO = mysql_db.Column(mysql_db.VARCHAR(64))