import pymysql
# from settings import settings
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# cnx=pymysql.Connect(user='root',password="zero",db="tests")
# cur=cnx.cursor()
# class Sql:
# 	def insert_tenement_message(title,rental):
# 		sql='INSERT INTO lianjia(title,rental)VALUES(%(title)s,%(rental)s)'
# 		value={
# 			'title':title,
# 			'rental':rental
# 		}
# 		cur.execute(sql,value)
# 	def select_title(cls,title):
# 		sql='SELECT EXISTS(SELECT 1 FROM tenement_message WHERE title=%(title)s)'
# 		value={
# 			'title':title
# 		}
# 		cur.execute(sql,value)
# 		return cur.fetchall()[0]

class ZufengPipeline(object):
    def open_spider(self,spider):
        self.con = pymysql.Connect(user='root',password="zero",db="tests")
        self.cu = self.con.cursor()

    def process_item(self, item, spider):
        print(spider.name,'pipelines')
        insert_sql = "insert into lianjia (title, rental) values('{}', '{}')".format(item['title'], item['rental'])
        print(insert_sql)
        value={
			'title':title,
			'rental':rental
		}
        self.cu.execute(insert_sql,value)
        self.con.commit()
        return item

    def spider_close(self, spider):
        self.con.close()
     # 这是赶集网租房信息
    # def process_item(self,item,spider):
    # 	title=item['title']
    # 	ret=Sql.select_title(title)
    # 	if ret[0] ==1:
    # 		print('房子已经存在')
    # 	else:
    # 		rental=item['rental']
    # 		Sql.insert_tenement_message(title,rental)
    # 		print('开始存租房信息')
