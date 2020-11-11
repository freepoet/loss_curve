# -*- coding: utf-8 -*-
"""
@File    : d2_loss_visualization.py
@Time    : 11/6/20 11:24 AM
@Author  : Mingqiang Ning
@Email   : ningmq_cv@foxmail.com
@Modify Time        @Version    @Description
------------        --------    -----------
11/6/20 11:24 AM      1.0         None
# @Software: PyCharm
"""
import json
import re
from pylab import *
fig = figure(figsize=(8,6), dpi=300)
y1 = fig.add_subplot(111)
y1.set_xlabel('Iterations')
y2 = y1.twinx()
y1.set_ylim(0,1.0)
parsed=[]
with open('./metrics1.json') as f:
    # whole = f.read()
    # # #pattern = re.compile(r'json_stats: (\{.*\})')
    # pattern = re.compile(r'\"data_time\":.*')
    # # #r:ban zhaunyi
    # lis = pattern.findall(whole)
    try:
        #ke neng chu xian de yi chang kuai
        # parsed = [json.loads(j) for j in lis]
        for line in f:
            parsed.append(json.loads(line))
        # print(parsed[0])

    except:
        #shang shu yi chang kuai de chu li fang fa
        print("json format is not corrrect")
        exit(1)

    _iter = [j['iteration'] for j in parsed]
    _loss = [j['total_loss'] for j in parsed]
    _loss_bbox = [j['loss_box_reg'] for j in parsed]
    _loss_cls = [j['loss_cls'] for j in parsed]
    try:
         _accuracy_cls = [j['fast_rcnn/cls_accuracy'] for j in parsed]
    except:
        _accuracy_cls = None
    _lr = [j['lr'] for j in parsed]
    try:
        _mask_loss = [j['mask_loss'] for j in parsed]
    except:
        _mask_loss = None

    y1.plot(_iter, _loss_bbox, color="green", linewidth=0.3,linestyle="-",label='loss_box_reg')

    y1.plot(_iter, _loss, color="blue", linewidth=0.3, linestyle="-",label='total_loss')
    y1.plot(_iter, _loss_cls, color="black", linewidth=0.3, linestyle="-",label='loss_cls')
    y1.plot(_iter, _accuracy_cls, color="red", linewidth=0.3, linestyle="-",label='cls_accuracy')
    if _mask_loss is not None:
         y1.plot(_iter, _mask_loss, color="grey", linewidth=0.3, linestyle="-",label='mask_loss')

    y2.set_ylim(0,max(_lr)/0.8)
    y2.plot(_iter, _lr, color="purple", linewidth=1.0, linestyle="-",label='lr')
    y2.set_ylabel('lr')

    #可以选择开启网格
    #grid()
    #图例
    y1.legend()
    savefig('./fig.png')
    show()
