# -*- coding: utf-8 -*-
import scrapy
from ljxq.items import LjxqItem

class XqdzSpider(scrapy.Spider):
    name = "xqdz"
    start_urls = ['https://sh.lianjia.com/xiaoqu/pg%scro11/' % p for p in range(1, 3)]
    #start_urls = ['https://sh.lianjia.com/xiaoqu/pg2scro11/',
    #              'https://sh.lianjia.com/xiaoqu/pg1scro11/']

    def parse(self, response):
        #yield scrapy.Request(response.url, callback=self.parse_next)
        house_page = '//ul[@class="listContent"]/li/div[1]/div[1]/a'
        for info in response.xpath(house_page):
            house_page_href = info.xpath('@href').extract()[0]
            yield scrapy.Request(house_page_href, callback=self.parse_next, dont_filter=True)

    def parse_next(self, response):
            item = response.xpath('//div[@class="detailHeader fl"]')
        #for item in response.xpath('//div[@class="detailHeader fl"]'):
            house = LjxqItem()
            house['name'] = item.xpath('h1[@class="detailTitle"]/text()').extract()[0]
            house['address'] = item.xpath('div[@class="detailDesc"]/text()').extract()[0]
            #yield house
            yield scrapy.Request(response.request.url,callback=self.parse_next_page,dont_filter=True,meta={'items':house})


    def parse_next_page(self, response):
        house = response.request.meta['items']
        item1 = response.xpath('//div[@class="fl l-txt"]')
        house['district'] = item1.xpath('a[3]/text()').extract()[0]
        house['plate'] = item1.xpath('a[4]/text()').extract()[0]
        yield house
    #https://sh.lianjia.com/xiaoqu/pg2cro11/ class="detailHeader fl"
    #/html/body/div[4]/div/div[1]/h1
    #/html/body/div[4]/div/div[1]/div /html/body/div[5]/div[1]/a[3]