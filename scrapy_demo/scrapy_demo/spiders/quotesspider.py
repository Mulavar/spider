# -*- coding: utf-8 -*-
import scrapy

from scrapy_demo.items import QuoteItem


class QuotesspiderSpider(scrapy.Spider):
    name = 'quotesspider'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']


    def parse(self, response):
        items = []
        quotes = response.css('.quote')
        for quote in quotes:
            item = QuoteItem()
            author = quote.css('.author::text').extract_first()
            text = quote.css('.text::text').extract_first()
            keywords = quote.css('.tags .tag::text').extract()
            item['author'] = author
            item['text'] = text
            item['keywords'] = keywords
            items.append(item)
            yield item


        next_page = response.css('.next a::attr(href)').extract_first()
        next_url = response.urljoin(next_page)
        yield scrapy.Request(url=next_url, callback=self.parse)