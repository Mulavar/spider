# -*- coding: utf-8 -*-
import scrapy

from scrapy_demo1.items import ItcastItem


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/channel/teacher.shtml']

    def parse(self, response):

        nodes = response.xpath('//div[@class="li_txt"]')

        for node in nodes:
            item = ItcastItem()
            name = node.xpath('.//h3/text()').extract_first()
            title = node.xpath('.//h4/text()').extract_first()
            info = node.xpath('.//p/text()').extract_first()

            item['name'] = name
            item['title'] = title
            item['info'] = info

            yield item

