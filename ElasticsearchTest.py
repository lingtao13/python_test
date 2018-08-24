#!/usr/bin/python
# _*_ coding:utf-8 _*_
__author__ = 'nelson'
__date__ = '2018/7/17 下午5:40'

from datetime import datetime
from elasticsearch import Elasticsearch
es=Elasticsearch()

doc={
    '作者':'kimi',
    '文档':'弹性搜索，流行歌曲，自然语言处理',
    '时间戳':datetime.now(),
}

res=es.index(index="test-index",doc_type="")