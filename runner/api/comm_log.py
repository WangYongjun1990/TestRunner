# -*- coding:utf-8 -*-

"""
File Name: `comm_log`.py
Version:
Description:

Author: wangyongjun
Date: 2018/5/24 11:03
"""

import logging
from logging.handlers import WatchedFileHandler
import time

from runner.config.config import log_path


formatter = logging.Formatter('[%(filename)-12s]: [%(levelname)-6s] [%(asctime)s]: %(message)s')

watched_file_handler = WatchedFileHandler(log_path, encoding="utf-8")
watched_file_handler.setFormatter(formatter)

watched_file_handler.setLevel(logging.DEBUG)
# watched_file_handler.setLevel(logging.INFO)

logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
logger.setLevel(logging.INFO)

logger.addHandler(watched_file_handler)

if __name__ == "__main__":

    for i in range(100):
        logger.debug("This is debug infomation")
        logger.info("This is info infomation")
        logger.error("This is error infomation")
        time.sleep(.1)
