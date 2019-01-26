# -*- coding: utf-8 -*-
import os,scrapy,json,re

from tutorial.items import TutorialItem
from tutorial.utils import HtmlUtil

class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['m.biqudao.com']
    start_urls = ['https://m.biqudao.com/bqge197313/10070017.html']
    #bqge197313/all.html 主页面 
    #详情页面 content 里 p元素大于2 才是有内容的
    #

   
    
    def parse(self, response):
        tmpStr = ""
        path = "../allnovel/bqge197313"
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

        print("--------------------start")
        print(item)
        print("--------------------")
        file = open(filename,'w+')
       
        tmpStr = json.dumps(item)
        
        file.write(tmpStr)
        
        file.close();
