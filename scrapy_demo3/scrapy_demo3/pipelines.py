# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
import pymysql

class ScrapyDemo3Pipeline(object):

    def __init__(self):
        setting = get_project_settings()
        self.user = setting['DB_USER']
        self.passwd = setting['DB_PASSWORD']
        self.charset = setting['DB_CHARSET']
        self.db_name = setting['DB_NAME']

    def process_item(self, item, spider):
        self.conn = pymysql.connect(user=self.user,
                                     password=self.passwd,
                                     db=self.db_name,
                                     charset=self.charset)

        with self.conn.cursor() as c:
            item = dict(item)
            sql = 'insert into people(name, position, img_src) values(%s, %s, %s);'
            c.execute(sql, (item['name'], item['position'], item['img_src']))
            self.conn.commit()
