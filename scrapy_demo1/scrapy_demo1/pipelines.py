# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
from scrapy.utils.project import get_project_settings

class ScrapyDemo1Pipeline(object):
    def __init__(self):
        self.f = open("itcast.json", "w")

    def process_item(self, item, spider):
        content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
        self.f.write(content)
        return item

    def close_spider(self):
        self.f.close()


class ItcastMysqlPipeline(object):
    def __init__(self):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.db_name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']
        self.connect()

    def connect(self):
        self.conn = pymysql.connect(user=self.user,
                                    password=self.password,
                                    db=self.db_name,
                                    charset=self.charset)
        self.cursor = self.conn.cursor()


    def close_spider(self):
        self.conn.close()
        self.cursor.close()

    def process_item(self, item, spider):
        dt = dict(item)
        sql = 'insert into itcast(name, title, info) values (%s, %s, %s);'
        self.cursor.execute(sql, (dt['name'], dt['title'], dt['info']))
        self.conn.commit()