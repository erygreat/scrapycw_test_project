
import time
import scrapy
from scrapy.http.request import Request


class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
    }

    def start_requests(self):
        yield Request('http://baidu.com/', meta={"num": 1}, dont_filter=True)

    def parse(self, response):
        meta = response.meta
        if meta['num'] > 10:
            return
        else:
            yield Request('http://baidu.com/', meta={"num": meta['num'] + 1}, dont_filter=True)
