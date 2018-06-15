# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field,Item

class TutorialItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    image_url = Field()
    image_path = Field()
    # image_urls = scrapy.Field()
    # images = scrapy.Field()
    # image_path = scrapy.Field()