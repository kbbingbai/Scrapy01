
######################怎样完成登陆再进行抓取######################

from scrapy.contrib.spiders.init import InitSpider
from scrapy.http import Request, FormRequest
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import Rule

class MySpider(InitSpider):
    name = 'myspider'
    allowed_domains = ['domain.com']
    login_page = 'http://www.domain.com/login'
    start_urls = ['http://www.domain.com/useful_page/',
                  'http://www.domain.com/another_useful_page/']

    rules = (
        Rule(SgmlLinkExtractor(allow=r'-\w+.html$'),
             callback='parse_item', follow=True),
    )

    def init_request(self):
        """This function is called before crawling starts."""
        return Request(url=self.login_page, callback=self.login)

    def login(self, response):
        """Generate a login request."""
        return FormRequest.from_response(response,
                    formdata={'name': 'herman', 'password': 'password'},
                    callback=self.check_login_response)

    def check_login_response(self, response):
        """Check the response returned by a login request to see if we are
        successfully logged in.
        """
        if "Hi Herman" in response.body:
            self.log("Successfully logged in. Let's start crawling!")
            # Now the crawling can begin..
            self.initialized()
        else:
            self.log("Bad times :(")
            # Something went wrong, we couldn't log in, so nothing happens.

    def parse_item(self, response):

        # Scrape data from page


------------------
复制代码
备注: 该代码片段来自于: http://www.sharejs.com/codes/python/8544


使用header
request_headers = { 'User-Agent': 'PeekABoo/1.3.7' }
request = urllib2.Request('http://sebsauvage.net', None, request_headers)
urlfile = urllib2.urlopen(request)

######################Request对象######################
Request对象在我们写爬虫，爬取一面的数据需要重新发送一个请求的时候调用的。这个类需要传递一些参数，其中比较常用的参数

	1 url :request对象发送请求的url。
	2 callback:在下载器下载完相应的数据后执行的回调函统。
	3 method : 请求的方法。默认为 cET 方法，可以设置为其他方法。
	4 hesaders : 请求头，对于一些固定的设置，放在 :ettings.py 中指定就可以了。对于那些非固定的，可以在发送请求时指定。
	5 meta : 比较常用。用于在不同的请求之间传递数据用的。用来共享数据
	6 encoding : 编码。 默认的为 vef-8 ，使用默认的就可以了。
	7 dot_filter : 表示不由调度器过滤 。在执行多次重复的请求的时候用得比较多 。
	8 errback : 在发生祝误的讨候执行的画数。

######################Response对象######################
Response对象:

	Response对象一般是由 scrapy 绽你自动构建的。因此开发者不需要关心如何创建 Rezponze 对象，而是如何使用他。 Respenze 对
	象有很多属性，可以用来提取数据的。主要有以下属性:
	1. meta: 从其他请求传过来的 meta 属性，可以用来保持多个请求之间的数据共享。
	2.encoding: 返回当前字符串编码和解码的方式。
	3.text: 将返回来的数据作为 unicode 字符串返回。
	4. body: 将返回来的数据作为 byes 字符申返回。
	5. xpath: xapth选择器 。
	6. css: css选择器

	发送POST请求:
        有时候我们想杰在请求数据的时候发送post请求，那么这时候需要使用 Request 的子类FormRequest 如果想要爬虫一开始
        的时候发送 PosT 请求，那么需要在爬虫类中重写 :start_request(self) 方法，并且不再调用: start_urls里的url。

