import scrapy
# from bs4 import BeautifulSoup
# from scrapy.http import Request
from ..items import ZufengItem
# import requests
# import re
class ZufengSpider(scrapy.Spider):
	name="zufeng"
	start_urls=["http://bj.ganji.com/fang1/"]
	def parse(self,response):
		zf=ZufengItem()
		title_name=response.xpath(".//*[@class='f-list-item ']/dl/dd[1]/a/text()").extract()
		monet_name=response.xpath(".//*[@class='f-list-item ']/dl/dd[5]/div[1]/span[1]/text()").extract()
		for i,j in zip(title_name,monet_name):
			zf['title']=i
			zf['rental']=j
			yield zf 
			# 这是赶集网的租房信息
	# allowed_domains=['sz.lianjia.com']

	# def start_requests(self):
	# 	thems_url='http://sz.lianjia.com/zufang/luohuqu/pg1/'
	# 	html=requests.get(theme_url)
	# 	content=BeautifulSoup(html.text,'lxml')

	# 	urls=[]
	# 	links=content.find('div',class_='option-list').find_all('a')
	# 	for link in links:
	# 		i=re.findall(r'g/(.*)/', link['href'])
	# 		if i:
	# 			urls.extent(i)
	# 	all_url=['http://sz.lianjia.com/zufang/{}/pg1/'.format(i) for i in urls]
	# 	for url in all_url:
	# 		print(url)
	# 		yield Request(url,self.parse)

	# def parse(self, response):
	# 	page = BeautifulSoup(response.text, 'lxml').find('div', class_='page-box house-lst-page-box')
	# 	max_page = re.findall('Page":(\d+)."cur', str(page))[0]
	# 	bashurl = str(response.url)[:-2]
	# 	for num in range(1,int(max_page)+1):
	# 		url = bashurl+str(num)+'/'
	# 		yield Request(url,callback=self.get_message)
	# def get_message(self, response):
	# 	item=ZufengItem()
	# 	content=BeautifulSoup(response.text,'lxml')
	# 	house_list = content.find_all('div', {'class': 'info-panel'})
	# 	for li in house_list:
	# 		item['title'] = li.find('h2').find('a').attrs['title']
	# 		item['rental'] = li.find('div', class_='price').find('span').get_text()
	# 		yield item
