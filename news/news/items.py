# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    mztj_title        = scrapy.Field()
    mztj_href         = scrapy.Field()
    mztj_article      = scrapy.Field()
    mztj_author       = scrapy.Field()
    mztj_writing_time = scrapy.Field()
