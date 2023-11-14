import json
import re
import scrapy
class MySpider(scrapy.Spider):
    name = 'shop'
    handle_httpstatus_list = [403]
    
    #custom_settings = { 'CONCURRENT_REQUESTS': '1' }
    def start_requests(self):
        headers = {
            'Accept': '*/*',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://shopee.vn/mall/',
            'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36'
        }
        
        yield scrapy.Request(f'https://shopee.vn/sp.btw2',self.parse,headers=headers)
        # for page in range (int(9528/30)*0,int(9528/30)*1+1):
        #     yield scrapy.Request(f'https://www.tripadvisor.com/Attractions-g293921-Activities-c42-oa{page*30}-a_sort.TRAVELER__5F__FAVORITES-Vietnam.html',self.parse)
        #yield scrapy.Request(f'https://www.tripadvisor.com/Attractions-g293921-Activities-oa{60}-Vietnam.html',self.parse)
    def parse(self, response):
        print("Print header")
        print(response.text)
        print("Print end")
        headers = {
            'Accept': 'application/json',
            'Accept-Language': 'en-US,en;q=0.9',
            'Sec-Ch-Ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'Sec-Ch-Ua-Mobile': '?0',
            'Sec-Ch-Ua-Platform': "Windows",
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'X-Requested-With' : 'XMLHttpRequest',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'af-ac-enc-dat' : 'AAczLjEuMC0yAAABi0ijs90AAA/0AzAAAAAAAAAAAiSDMis8Yhxb1KIEkKdQcN5HZUh18MS3gD4Lv0cZsWDYYHdpR1c3Np8BzcsRRPm/ZZgFLUngG5gdglPRlokHaBO6riuJzOhSEoCDq8ldg+RcTmGj6lzRcbx+u+wuFArvx+zvDDCzMOdK2xGN7mdKcf0ai/FxzOhSEoCDq8ldg+RcTmGj6lzRcbx+u+wuFArvx+zvDDBGV2Ia3yab8r/0vvuJ/GyfpohFHsEFTkPArlIVDn5bBVRiZeaLJCVJU0SfG5dRLyXEplSWPkm3eMEC3t+KLNlvGAt58mjadOCSqdJGJMljclRiZeaLJCVJU0SfG5dRLyWN0M2z/8ohMd7DMqMKXl80HvJ7N52r4m0D8jIqw9a6iRBPodmt4EdszHIcF4opk6bijaoH3ZWucrUHIf6trdKlsc2Xbfdc2gpt/+aJUOqVPH+RElVIBn5MeXS/LyLxjKlz89ZoMkHNa3/5dWKMg5jKXR0XEHp7nMd/yK6jJfN2mv439vzknrcdleW6J26R8SlgUIRBDXTXr7nYsbBk4Wfdl/82EyfDx/bVRcPaaRvYm+C1D3U0QfLCyBhv2heEmwlVFW0VvWLOYRXkeGOccQE6eVtks1BST6eLSS4Vm6Mzx0gD9O1aYGgjmjuYbekv+r9vs85v4y7AEcXy7ddZlL1tNWyHOinDzdXMaUck8rc/k3F24b63UOzELVTSo9tyLjHEpgszJ8O1hpaItnjFuz8WuLlcnv+Y0Qu5qz3dAtcJhEGH+oXBvfWeA9jFDI9ilXuhZCjTdp11V8Sq9P3lUKujQpDkHUiYI4aXpqFUFwvd2sBnXBIUt69oIpFJPkiBxhthluGaSDuXWX0jGK26AxlbzanHquMZUUau9k5d4rorJbmbCOeGPT37BpcUJiV1wFf+VWsnQlUEQxl2zbg0zFZ8weLOxp9vgqjT+0hBzk2QDjrijd9bxiK0/S0zhPpEdqfcTvPhy698R791eWXhZXUel/82EyfDx/bVRcPaaRvYm6YYQrr5kgrd9GoJ5bFfZaDM3hNgdZRMZ4aP59tl7z/g4uCgisFY7om8kJPXrmzIjssBBivj12tjEth/z9aaKIE=',
            'Af-Ac-Enc-Sz-Token' : 'EUyg68ofMjdKF4ebG2SvWA==|UwOqHxgEP4vAKuuqg9AsT10swOhbFNxYHcHsJgBlq8yOfYNtUsx0R5sbbWNOY8YvuAMdeakJX4SPEQ==|w6MX2m1PZf3Pq1Gm|08|3',
            'X-Api-Source' : 'pc',
            'X-Csrftoken' : '9d76zgVHbCvMQZg1sM94GYLFBTcBqrZ1'

        }
        yield scrapy.Request(f'https://shopee.vn/api/v4/shop/rcmd_items?bundle=shop_page_category_tab_main&limit=30&offset=0&shop_id=40342563&sort_type=1&upstream=',self.parse2,headers=headers)
    def parse2(self, response):
        print("Print header")
        print(response.request.headers)
        print("Print text")
        print(response.text)
        print("Print end")
        # sections= response.xpath("//section").getall()
        # sections=[scrapy.Selector(text=i) for i in sections]
        # if sections : 
        #     attraction_url = []
        #     rank=[]
        #     name=[]
        #     by = []
        #     rate = []
        #     num_rv = []
        #     tour =[]
        #     duration = []
        #     price = []
        #     for i in sections : 
        #         temp = i.xpath("//a/@href").getall()
        #         matching = [s for s in temp if "AttractionProductReview" in s]
        #         if matching:
        #             attraction_url.append(matching[0])
        #             rank.append(i.xpath("//a//span[@name='title']//span/text()").get())
        #             name.append(i.xpath("//a//span[@name='title']/div/text()[2]").get())
        #             matching = [s for s in temp if "Attraction_Review" in s]
        #             if matching :
        #                 by.append(matching[0])
        #             else :
        #                 by.append(None)
        #             rate.append(i.xpath("//a//svg[contains(@aria-label,'bubbles')]//@aria-label").get())
        #             num_rv.append(i.xpath("//a//svg[contains(@aria-label,'bubbles')]/../span/text()").get())
        #             tour.append(i.xpath("//header/../div[1]//div/text()").get())
        #             duration.append(i.xpath("//header/../div[1]//div[3]//div/text()").get())
        #             price.append(i.xpath("//header/../div[1]//div/text()/../../div/div/text()").get())

        #     url_rank={'rank':rank,'name':name,'attraction_url':attraction_url,'by':by,'rate':rate,'num_rv':num_rv,
        #                     'tour':tour,'duration':duration,'price':price}
        #     url_rank=[dict(zip(url_rank,t)) for t in zip(*url_rank.values())]
            
        #     for i in url_rank : yield i

