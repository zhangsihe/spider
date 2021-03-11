# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

class NewsPipeline(object):
    def process_item(self, item, spider):
        with open("my_meiju.txt",'a',encoding='utf-8') as fp:
            fp.write('title:' + item['mztj_title'] + 'href:' + item['mztj_href'] + '\n' + item['mztj_article'] + '\n')
            #fp.write(item['title'].encode("utf-8") + '\n')
