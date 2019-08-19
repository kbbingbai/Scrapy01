# -*- coding: utf-8 -*-
""""
    0 爬取 糗事百科 进行颁布爬取

    1 必须 是继承scrapy.Spider
    2 三个类属性 name   allowed_domains    start_urls


    3 首先: 我们便用: response.css(linext asattr(href)).extract first0查看有木有存在下一页链接，如果存在的话，我们使
        用: urljointnext_page)把相对路径，如: page/1转换为绝对路径，其实也就是加上网站域名，如:
        httpWlab.scrapyd.cn/page/1; 接下来就是耻取下一页或是内容页的秘诀所在，scrapy给我们提供了这么一个方法:
        scrapy.Request() 这个方法还有许多参数，后面我们慢慢说，这里我们只使用了两个参数，一个是: 我们继续假取的链接
        (next_page) ，这里是下一页链接，当然也可以是内容页; 另一个是: 我们要把链接提交给哪一个函数个取，这里是
        parse函数，也就是本函数; 当然，我们也可以在下面另写一个函数，比如: 内容页，专门处理内容页的数据。经过这么一
        个函数，下一页链接又提交给了parse，那就可以不断的耻取了，直到不存在下一页;
    4 这里我们通过 yield 来发起一个请求，并通过 callback 参数为这个请求添加回调函
        数，在请求完成之后会将响应作为参数传递给回调函数。
        
        scrapy框架会根据 yield 返回的实例类型来执行不同的操作，如果是 scrapy-Request 对
        象，scrapy框架会去获得该对象指向的链接并在请求完成后调用该对象的回调函数。

        如果是 scrapy.Item 对象，scrapy框架会将这个对象传递给 pipelines.py做进一步处理。

"""
import scrapy
from scrapy.http.response.html import HtmlResponse
from scrapy.selector.unified import SelectorList

from Scrapy01.items import Scrapy01Item
class QsbkSpider(scrapy.Spider):
    name = 'qsbk'
    allowed_domains = ['qiushibaike.com']
    start_urls = ['https://www.qiushibaike.com/text/page/1/']
    base_domain = 'https://www.qiushibaike.com'

    def parse(self, response):
        # print("="*20)
        # print(type(response))               #<class 'scrapy.http.response.html.HtmlResponse'>
        # print("="*20)

        # contentLeft = response.xpath("//div[@id='content-left']")
        # print(type(contentLeft))            #<class 'scrapy.selector.unified.SelectorList'>

        # duanzidivs = response.xpath("//div[@id='content-left']/div")
        # for duanzi in duanzidivs:
        #     print(type(duanzi))            #<class 'scrapy.selector.unified.Selector'>
        #     break

        duanzidivs = response.xpath("//div[@id='content-left']/div")
        for duanzi in duanzidivs:
            author = duanzi.xpath(".//h2/text()").get().strip()
            content = duanzi.xpath(".//div[@class='content']//text()").getall() #return [x.get() for x in self]
            content = "".join(content).strip()
            item = Scrapy01Item(author=author,content=content)
            yield item

            #爬去第二页的数据
            next_url = response.xpath("//ul[@class='pagination']//li[last()]/a/@href").get()
            if not next_url:
                return
            else:
                yield scrapy.Request(url=QsbkSpider.base_domain+next_url,callback=self.parse)