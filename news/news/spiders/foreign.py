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

            item['mztj_article'] = scrapy.Request(url=item['mztj_href'],callback=self.parse_article)

            yield item
            break

    def parse_article(self,response):
        return response.xpath('//div[@clas="divContent"]').extract()[0]
