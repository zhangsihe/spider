import scrapy

from news.items import NewsItem
from scrapy.http import HtmlResponse

class ForeignSpider(scrapy.Spider):
    name = 'foreign'
    allowed_domains = ['cnforex.com']
    start_urls = ['http://www.cnforex.com/comment/person/']
    #start_urls = ['http://www.woquxuexi.com/1527.html']
    def parse(self, response):
        item = NewsItem()
        item['title'] = response.xpath('//title/text()').extract()[0]
        yield item
