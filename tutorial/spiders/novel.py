# -*- coding: utf-8 -*-
import os,scrapy,json,re

from tutorial.items import TutorialItem
from tutorial.utils import HtmlUtil

class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['m.biqudao.com']
    chapter_path = '../allnovel/bqge197313'
    chpater_id = 'bqge197313'
    start_urls = []
    #读取目录
    
    item_list = os.listdir(chapter_path)
    for i in range(0, len(item_list)):
        path = os.path.join(chapter_path, item_list[i])
        if os.path.isfile(path) and os.path.basename(path).find("novel_info") == -1:
            start_urls.append("https://"+allowed_domains[0]+"/"+chpater_id+"/"
                              + os.path.basename(path).split(".")[0]+".html")
    print("--------------start-----------")
    print(start_urls)
    print("---------------end------------")
    def parse(self, response):
        tmpStr = ""
        path = "../allnovel/bqge197313/"
        filename = "../allnovel/bqge197313/10070017.json"
        htmlUtil = HtmlUtil()
        #item = TutorialItem()
        item = {}
        
        item['content'] = response.css("#chaptercontent").extract_first()
        item['title'] = response.css(".title::text").extract_first()
        item['page_prev'] = response.css("#pb_prev::attr(href)").extract_first()
        item['page_next'] = response.css("#pb_next::attr(href)").extract_first()
        if os.path.exists(path):
            pass
        else:
            os.mkdir(path)
            
        item['content'] = htmlUtil.filter_tags(item['content'])

        page = response.url.split("/")[-1].split(".")[0]  # 根据上面的链接提取分页,如：/page/1/，提取到的就是：1
        filename = '%s.json' % page

        file = open(path+filename, 'w+')
       
        tmpStr = json.dumps(item)
        
        file.write(tmpStr)
        
        file.close();
