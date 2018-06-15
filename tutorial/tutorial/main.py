#!/usr/bin/env python
# encoding: utf-8

"""
@version: 1.0.0.01
@author: qingyao.wang
@license: kuang-chi Licence 
@contact: qingyao.wang@kuang-chi.com
@site: 
@software: PyCharm
@file: main.py
@time: 2018/6/14 11:27
"""

from scrapy import cmdline

cmdline.execute("scrapy crawl chepai".split())