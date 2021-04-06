# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import mysql.connector
import datetime
import hashlib

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class NewsPipeline(object):

    def process_item(self, item, spider):
        mydb = mysql.connector.connect(host="121.4.191.75", user="root", passwd="!Zz1995711", database="spider")
        mycursor = mydb.cursor()

        titleMd5 = hashlib.md5(item['mztj_title'].encode(encoding='UTF-8')).hexdigest();

        sql = "SELECT * FROM cnforex_bjdp where md5=%s"

        mycursor.execute(sql,(titleMd5,))

        myresult = mycursor.fetchall()

        if len(myresult) <= 0:
            thisTime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

            sql = "INSERT INTO cnforex_bjdp (title,author, body,md5,create_time,update_time) VALUES (%s, %s, %s, %s, %s, %s)"
            val = (item['mztj_title'], item['mztj_author'], item['mztj_article'],
                   hashlib.md5(item['mztj_title'].encode(encoding='UTF-8')).hexdigest(), thisTime, thisTime)
            mycursor.execute(sql, val)

            mydb.commit()

        # with open("my_meiju.txt", 'a', encoding='utf-8') as fp:
        #     fp.write('title:' + item['mztj_title'] + 'href:' + item['mztj_href'] + '\n' + item['mztj_article'] + '\n')
