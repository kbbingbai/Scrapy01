# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

"""
    保存数据的第一个版本 使用 open文件的格式，
1 初始化 ft 可以在__init__ 也可以在open_spider中

"""
# import json
# class Scrapy01Pipeline(object):
#
#     def __init__(self):
#         print("__init__")
#         self.ft = open("./Scrapy01/files/qsbk.json","w",encoding="utf-8")
#
#     def open_spider(self,spider):
#         print("open_spider")
#
#     def process_item(self, item, spider):
#         item = json.dumps(dict(item),ensure_ascii=False)
#         self.ft.write(item+"\n")
#         return item
#
#     def close_spider(self,spider):
#         print("close_spider")

"""
    保存数据的第二种方式 
    
        1 使用 JsonItemExporter,注意这种方式适合数据量比较小的
        它会把item保存在内容中，当没有item没有时，它才调用 self.exporter.finish_exporting() 进行统一的保存，
        当数据量大的时候，就不能采用这种方式了
        
        2 注意保存的数据是一个列表,保存的形式是：[{"key":"value"}]
        
        3 注意必须是 self.ft = open("./Scrapy01/files/qsbk.json","bw") bw的形式，查看源码就可以知道了
        
"""
# from scrapy.exporters import JsonItemExporter
#
# class Scrapy01Pipeline(object):
#
#     def __init__(self):
#         print("__init__")
#         self.ft = open("./Scrapy01/files/qsbk.json","bw") #注意以二进制的形式打开
#         self.exporter = JsonItemExporter(self.ft,ensure_ascii=False,encoding='utf-8')
#         self.exporter.start_exporting()
#
#     def open_spider(self,spider):
#         print("open_spider")
#
#     def process_item(self, item, spider):
#         self.exporter.export_item(item)
#         return item
#
#     def close_spider(self,spider):
#         self.exporter.finish_exporting()
#         self.ft.close()
#         print("close_spider")


"""
    保存数据的第二种方式 
        1 使用 JsonLinesItemExporter,注意这种方式适合数据量大小都可
        每一条item立马进行保存，不会在最后进行统一保存
        
        2 注意保存的形式是：{"key":"value"}
        
        3 注意必须是 self.ft = open("./Scrapy01/files/qsbk.json","bw") bw的形式，查看源码就可以知道了
"""
from scrapy.exporters import JsonLinesItemExporter

class Scrapy01Pipeline(object):

    def __init__(self):
        print("__init__")
        self.ft = open("./Scrapy01/files/qsbk.json","wb") #注意以二进制的形式打开
        self.exporter = JsonLinesItemExporter(self.ft,ensure_ascii=False,encoding='utf-8')

    def open_spider(self,spider):
        print("open_spider")

    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item

    def close_spider(self,spider):
        self.ft.close()
        print("close_spider")