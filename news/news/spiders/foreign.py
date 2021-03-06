import scrapy

from news.items import NewsItem

class ForeignSpider(scrapy.Spider):
    name = 'foreign'
    allowed_domains = ['cnforex.com']
    start_urls = ['http://www.cnforex.com/comment/person/default.aspx?shwqg=1']

    def parse(self, response):

        trResource = response.xpath('//div[@id="d_left"]/table/tbody/tr')
        for ecahTr in trResource:
            item = NewsItem()
            item['mztj_href']         = ecahTr.xpath('./td/a[@target="_blank"]/@href').extract()[0]
            item['mztj_title']        = ecahTr.xpath('./td/a[@target="_blank"]/text()').extract()[0].strip()
            item['mztj_author']       = ecahTr.xpath('./td/a[@style="font-weight:bold;"]/text()').extract()[0].strip()
            item['mztj_writing_time'] = ecahTr.xpath('./td[@style="width: 15%;"]/text()').extract()[0].strip()

            yield scrapy.Request(url=item['mztj_href'],callback=self.parse_article,meta={'item':item})

    def parse_article(self,response):
        item = response.meta['item']
        item['mztj_article'] = response.xpath('//div[@class="divContent"]').extract()[0]
        yield item
