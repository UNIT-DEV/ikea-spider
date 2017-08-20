# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy  

class ProductItem(scrapy.Item):
    category = scrapy.Field()    
    name = scrapy.Field()
    broad = scrapy.Field()
    price = scrapy.Field()
    feature = scrapy.Field()
    new = scrapy.Field()
    discount = scrapy.Field()    
    link = scrapy.Field()    
