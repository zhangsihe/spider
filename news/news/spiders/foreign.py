import scrapy

from news.items import NewsItem

class ForeignSpider(scrapy.Spider):
    name = 'foreign'
    allowed_domains = ['cnforex.com']
    start_urls = ['http://www.cnforex.com/comment/person/author/?a=tEJU-lEk3dlCg6mm0kMZsw__']
    #start_urls = ['http://www.woquxuexi.com/1527.html']
    def parse(self, response):

        trResource = response.xpath('//td[@class="first"]')
        for ecahTr in trResource:
            item = NewsItem()
            item['mztj_href']  = ecahTr.xpath('./a/@href').extract()[0]
            item['mztj_title'] = ecahTr.xpath('./a/text()').extract()[0].strip()

            yield scrapy.Request(url=item['mztj_href'],callback=self.parse_article,meta={'item':item})

    def parse_article(self,response):
        item = response.meta['item']
        item['mztj_article'] = response.xpath('//div[@class="divContent"]').extract()[0]
        yield item
