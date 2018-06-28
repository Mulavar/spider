# -*- coding: utf-8 -*-
import scrapy
from scrapy_demo2.items import TencentItem
class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    offset = 0
    start_urls = ['http://hr.tencent.com/position.php?&start=' + str(offset)]

    def parse(self, response):
        node_list = response.xpath('//tr[@class="even"] | //tr[@class="odd"]')
        for node in node_list:
            item = TencentItem()
            position_name = node.xpath('./td[1]/a/text()').extract() # html标记从1开始计数
            position_link = node.xpath('./td[1]/a/@href').extract()
            position_type = node.xpath('./td[2]/text()').extract() # 提取的为Unicode字符串 可加.encode('utf-8')转为utf8
            position_num = node.xpath('./td[3]/text()').extract()
            position_location = node.xpath('./td[4]/text()').extract()
            publish_date = node.xpath('./td[5]/text()').extract()

            item['position_name'] = position_name
            item['position_link'] = position_link
            item['position_type'] = position_type
            item['position_num'] = position_num
            item['position_location'] = position_location
            item['publish_date'] = publish_date

            yield item

        self.offset += 10
        url = 'http://hr.tencent.com/position.php?&start=' + str(self.offset)
        yield scrapy.Request(url=url, callback=self.parse)
