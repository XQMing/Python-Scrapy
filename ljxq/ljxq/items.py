# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class LjxqItem(scrapy.Item):
    name = scrapy.Field()     # 项目名称
    address = scrapy.Field()  # 地址
    district = scrapy.Field() # 区域
    plate = scrapy.Field()    # 板块