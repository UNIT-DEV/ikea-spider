# -*- coding: utf-8 -*-

import sys
reload(sys)
import json
#sys.setdefaultencoding('utf-8')
import scrapy
from ikea.items import *

class IkeaSpider(scrapy.Spider):
    name = "ikea"
    allowed_domains = ["ikea.com"]
    start_urls = [
        "http://www.ikea.com/cn/zh/catalog/allproducts/department"
    ]

    def parse(self, response):
        req = []
        for sel in response.xpath(('//*[@class="textContainer"]/a')):
            item = ProductItem()
            item['category'] = sel.xpath('text()').extract_first().strip()
            link = 'http://www.ikea.com' + sel.xpath('@href').extract_first().strip()
            #r = scrapy.Request(link, meta={'item': item}, callback=self.parse_product)
            #req.append(r)
            yield scrapy.Request(link, meta={'item': item}, callback=self.parse_product)
        #return req

    def parse_product(self, response):
        item = response.meta['item']
        for sel in response.css('.product'):
            item['broad'] = sel.css('.productTitle::text').extract_first()
            if item['broad'] != None:
                item['broad'] = item['broad'].strip()
            item['name'] = sel.css('.productDesp::text').extract_first()
            if item['name'] != None:
                item_name = item['name'].strip()
                if u'，' in unicode(item_name):
                    (item['name'], item['feature']) = unicode(item_name).split(u'，')
            price = sel.css('.price::text').extract_first()
            if price != None:
                item['price'] = price.strip()
            low_price = sel.css('.productBtiFront>.price::text').extract_first()
            if low_price != None:
                item['price'] = low_price.strip()
                item['discount'] = True
            else:
                item['discount'] = False
            new_img = sel.css('.newImgSmall').extract_first()
            if new_img != None:
                item['new'] = True
            else:
                item['new'] = False
            link = 'http://www.ikea.com' + sel.xpath('//*[@class="image"]/a').xpath('@href').extract_first()
            item['link'] = link
            if item['name'] != None:
                yield item
