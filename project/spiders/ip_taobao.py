import json
import os
import scrapy


class IpTaobaoSpider(scrapy.Spider):

    name = 'ip_taobao'

    custom_settings = {
        'LOG_FILE': os.path.realpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '../../logs/ip_taobao.log'))
    }

    def start_requests(self):
        yield scrapy.FormRequest('https://ip.taobao.com/outGetIpInfo', formdata={
            "ip": "myip",
            "accessKey": "alibaba-inc",
        })

    def parse(self, response):
        content = json.loads(response.text)
        if content['code'] != 0:
            self.logger.error(content['msg'])
            return
        else:
            yield content['data']
