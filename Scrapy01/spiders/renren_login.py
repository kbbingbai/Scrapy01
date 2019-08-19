# -*- coding: utf-8 -*-
import scrapy

"""
在scrapy.Spider框架下，实现人人网的登陆，重写start_requests

发送POST请求:
        有时候我们想杰在请求数据的时候发送post请求，那么这时候需要使用 Request 的子类FormRequest 如果想要爬虫一开始
        的时候发送 PosT 请求，那么需要在爬虫类中重写 :start_request(self) 方法，并且不再调用: start_urls里的url。
"""

class RenrenLoginSpider(scrapy.Spider):
    name = 'renren_login'
    allowed_domains = ['renren.com']
    start_urls = ['http://renren.com/']


    def start_requests(self):
        url_login = 'http://www.renren.com/PLogin.do'  # 登陆页面
        header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
        }
        data = {
            "email": "15269106322",
            "password": "binghai2012"
        }
        req = scrapy.FormRequest(url_login,formdata=data,headers=header,callback=self.save_loginPage)
        yield req

    def save_loginPage(self,response):
        #进入登陆页面

        # with open("./Scrapy01/files/renrenLogin.html","w",encoding="utf-8") as ft:
        #     ft.write(response.text)
        url_main = 'http://www.renren.com/971667441/profile'  # 登陆后的个人主页
        req = scrapy.FormRequest(url_main,callback=self.save_pro)
        yield req


    def save_pro(self, response):
        # 进入个人主页
        with open("./Scrapy01/files/renrenPro.html","w",encoding="utf-8") as ft:
            ft.write(response.text)






