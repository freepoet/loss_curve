# -*- coding: utf-8 -*-
"""
@File    : extract_log.py
@Time    : 11/6/20 10:39 AM
@Author  : Mingqiang Ning
@Email   : ningmq_cv@foxmail.com
@Modify Time        @Version    @Description
------------        --------    -----------
11/6/20 10:39 AM      1.0         None
# @Software: PyCharm
@Cited{
  author = dspeia
  link = https://blog.csdn.net/qq_34806812/article/details/81459982
}
"""
# coding=utf-8
# 该文件用来提取训练log，去除不可解析的log后使log文件格式化，生成新的log文件供可视化工具绘图

import inspect
import os
import random
import sys


def extract_log(log_file, new_log_file, key_word):
    with open(log_file, 'r') as f:
        with open(new_log_file, 'w') as train_log:
            # f = open(log_file)
            # train_log = open(new_log_file, 'w')
            for line in f:
                # 去除多gpu的同步log
                if 'Syncing' in line:
                    continue
                # 去除除零错误的log
                if 'nan' in line:
                    continue
                if key_word in line:
                    train_log.write(line)
    f.close()
    train_log.close()


extract_log('log _20201106_1030.txt', 'train_log_loss.txt', 'total_loss')
# extract_log('log _20201106_1030.txt', 'train_log_iou.txt', 'IOU')
