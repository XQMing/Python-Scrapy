# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class LjxqPipeline(object):
    def process_item(self, item, spider):
        info = item['address'].split(')')
        #if len(info)==2:
        item['address'] = info[1]
        #elif len(info)>2:
         #   item['address'] = info[1]
        item['district'] = item['district'].replace(u'小区','')
        item['plate'] = item['plate'].replace(u'小区','')
        return item