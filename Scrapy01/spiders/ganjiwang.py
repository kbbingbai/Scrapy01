# -*- coding: utf-8 -*-
import scrapy
import re
from urllib import request

from PIL import Image
"""
    这个会有一点问题： 但是思路是可以的
    
    0 赶集网
    1 带图片验证码的数据爬取
    2 如果我们 yield scrapy.FormRequest(url=self.login_url,formdata=data,callback=self.login_success)中没有指定
        callback 函数，它会自动调用parse函数
"""


class GanjiwangSpider(scrapy.Spider):
    name = 'ganjiwang'
    allowed_domains = ['passport.ganji.com']
    start_urls = ['https://passport.ganji.com/login.php']
    login_url = "https://passport.ganji.com/login.php?callback=jQuery18205398264083268478_1566227624443"

    login_success = 'http://www.ganji.com/user/login_success.php?username=15269106322&next=%2F'

    def parse(self, response):
        text = response.text

        data = {
            "username": "15269106322",
            "password": "binghai2010",
            "setcookie": "14",
            "next": "",
            "source": "passport",
        }
        #解析__hash__这个参数
        reg = re.search(r'__hash__":"[^\s}]*',text)
        hash = reg.group().split(":")[1]
        data["__hash__"] = hash

        #解析 checkCode这个参数
        checkCodeImgUrl = response.css("img.login-img-checkcode::attr(data-url)").get()
        request.urlretrieve(checkCodeImgUrl,"./Scrapy01/files/checkCodeImgUrl.png")

        image = Image.open("./Scrapy01/files/checkCodeImgUrl.png")
        image.show()
        cap = input("请输入验证码:")
        data["checkCode"] = cap

        yield scrapy.FormRequest(url=self.login_url,formdata=data,callback=self.login_success)

    def login_success(self,response):
        print(response.text)
        if response.url == self.login_success:
            print("成功---")
        else:
            print('失败-----')


