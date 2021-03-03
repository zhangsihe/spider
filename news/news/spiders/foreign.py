import scrapy

from news.items import NewsItem

class ForeignSpider(scrapy.Spider):
    name = 'foreign'
    allowed_domains = ['cnforex.com']
    start_urls = ['http://www.cnforex.com/comment/person/']

    def parse(self, response):
        item = NewsItem()
        print(response.xpath('//title/text()'))

        item['title'] = response.xpath('//title/text()')
        yield item
