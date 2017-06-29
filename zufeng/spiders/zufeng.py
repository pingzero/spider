import scrapy

from ..items import ZufengItem
class ZufengSpider(scrapy.Spider):
	name="zufeng"
	start_urls=["http://bj.ganji.com/fang1/"]
	def parse(self,response):
		zf=ZufengItem()
		title_name=response.xpath(".//*[@class='f-list-item ']/dl/dd[1]/a/text()").extract()
		monet_name=response.xpath(".//*[@class='f-list-item ']/dl/dd[5]/div[1]/span[1]/text()").extract()
		for i,j in zip(title_name,monet_name):
			zf['title']=i
			zf['money']=j
			yield zf