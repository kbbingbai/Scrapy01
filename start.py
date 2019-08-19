#!/user/bin/env python3
# -*- coding: utf-8 -*-
# @Time   :2019/8/15 22:41
# @Author :zhai shuai
"""
 作用
    一：
 难点
    
 注意点
    
"""

from scrapy import cmdline

#cmdline.execute("scrapy crawl qsbk".split())# 等价于下面的
# cmdline.execute(["scrapy", "crawl", "qsbk"])
# cmdline.execute(["scrapy", "crawl", "renren_login"])

cmdline.execute(["scrapy", "crawl", "ganjiwang"])
