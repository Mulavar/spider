# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy_demo3.items import NESAItem

class NesaSpider(scrapy.Spider):
    name = 'nesa'
    allowed_domains = ['nesa.zju.edu.cn']
    start_urls = ['http://nesa.zju.edu.cn/webpage/people.html']

    def parse(self, response):
        person_list = response.xpath('//div[@class="view view-ninth"]')
        for person in person_list:
            item = NESAItem()
            name = person.xpath('.//h2/text()').extract_first()
            position = person.xpath('.//p/text()').extract_first()
            img_src = person.xpath('.//img/@src').extract_first()
            img_src = re.sub(r'\.\./', r'http://nesa.zju.edu.cn', img_src)

            item['name'] = name
            item['position'] = position
            item['img_src'] = img_src

            yield item
