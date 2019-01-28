# chapter
"""
id 获取 all 下的列表
"""
import os
import scrapy
import json
import re

from tutorial.utils import HtmlUtil


class ChapterSpider(scrapy.Spider):
    novel_id = 'bqge197313' 
    novel_path = "../allnovel/"
    name = 'chapter'
    allowed_domains = ['m.biqudao.com']
    start_urls = ['https://m.biqudao.com/'+novel_id+'/all.html']

    def getAllChapterLink(self):
        if os.path.exists(self.novel_path+self.novel_id):
            pass
        else:
            os.mkdir(self.novel_path+self.novel_id)

    def parse(self, response):
        path = "../allnovel/"+self.novel_id+"/"
        
        # htmlUtil = HtmlUtil()
        items = response.css("#chapterlist a::attr(href)").extract()
        # if os.path.exists(path):
        #     pass
        # else:
        #     os.mkdir(path)
        if len(items)>0:
            items = items[1:]
            print(items)
            for item in items:
                filename = ".json"
                print(item.split("/")[2].split(".")[0])
                chapter_id  = item.split("/")[2].split(".")[0]
                filename = path+chapter_id+filename
                file = open(filename, 'w+')
                file.write("")
                file.close()
        else:
            pass
   
