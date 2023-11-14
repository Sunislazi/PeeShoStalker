# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.
import scrapy
import pandas as pd
import json
class MySpider(scrapy.Spider):
    name = 'MissingDetail'

    url='https://www.tripadvisor.com/Attraction_Review-g293926-d24940231-Reviews-Asianway_Travel-Hue_Thua_Thien_Hue_Province.html'
    
    #custom_settings = { 'ROBOTSTXT_OBEY': False }
    def start_requests(self):
        
        f=open("./dataset/missing.json")
        try:
            url=json.load(f)
        except Exception as e: 
            print(e)
        f.close()
        url=url['missing']
        for i in url :
            yield scrapy.Request(i,self.parse)
    def parse(self, response):
        Detail_dict = {}
        Detail_dict['attraction'] = response.xpath("//div[@data-test-target='fusion-screen-detail']//h1/text()").get()
        Detail_dict['province'] = response.xpath("//main/div/div/div/div//a/span/span/text()").getall()
        Detail_dict['rate'] = response.xpath("//a[@href='#REVIEWS']//svg/../../div[contains(@aria-label,'bubbles')]/@aria-label").get()
        kind=response.xpath("//main//section//div[@data-automation='WebPresentation_PoiOverviewWeb']//div[@class='kUaIL']/div/div/div//text()").getall()
        try : 
            kind.remove('Read more')
        except : 
            pass
        Detail_dict['kind']=''.join(kind).replace(' ',' ')
        Detail_dict['url'] = response.url
        yield Detail_dict

