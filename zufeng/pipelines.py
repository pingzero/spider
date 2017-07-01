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
# class Slq(object):
#     def select_title(cu,title):
#         sql="select exists(select 1 from tenement_message where title=$s)"
#         value=[title]
#         cu.execute(sql,value)
#         return cu.fetchall()[0]
class ZufengPipeline(object):
    def open_spider(self,spider):
        self.con = pymysql.Connect(user='root',password="zero",db="tests",charset="UTF8")
        self.cu = self.con.cursor()

    def process_item(self, item, spider):
        title=item['title']
        rental=item['rental']
        insert_sql = "replace into lianjia (title, rental) values(%s,%s)"
        # print(insert_sql)
        value=[title,rental]
        self.cu.execute(insert_sql,value)
        self.con.commit()
        return item

    # def select_item(self,item,spider):
    #     select_sql="select title from lianja group by title"
    #     self.cu.execute(select_sql)
    #     self.con.commit()

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
