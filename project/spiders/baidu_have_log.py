
import time
import os
import scrapy
from scrapy.http.request import Request


class BaiduHaveLogSpider(scrapy.Spider):
    name = 'baidu_log'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    custom_settings = {
        'DOWNLOAD_DELAY': 2,
        'LOG_FILE': os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../logs/baidu-have-log.log'))
    }

    def start_requests(self):
        yield Request('http://baidu.com/', meta={"num": 1}, dont_filter=True)

    def parse(self, response):
        meta = response.meta
        if meta['num'] > 10:
            return
        else:
            yield Request('http://baidu.com/', meta={"num": meta['num'] + 1}, dont_filter=True)
