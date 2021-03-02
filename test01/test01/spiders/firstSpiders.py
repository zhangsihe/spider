import scrapy
from test01.items import Test01Item 

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    allowed_domains = ["cnforex.com"]
    start_urls = [
        'http://www.cnforex.com/comment/person/'
    ]

    def parse(self, response):
        list_a = response.xpath('/td[@class="first"]/a[@target="_blank"]/@href').extract()
        for quote in list_a:
            item = Test01Item()
            item['url'] = quote
            print(quote)
            yield item
