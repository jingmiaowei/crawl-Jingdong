# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JdphoneItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    title = scrapy.Field()  

    price = scrapy.Field()  

    comment_num = scrapy.Field()  

    url = scrapy.Field()  

    info = scrapy.Field()  
