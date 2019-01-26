# -*- coding: utf-8 -*-
import os,scrapy,json,re

from tutorial.items import TutorialItem

class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['m.biqudao.com']
    start_urls = ['https://m.biqudao.com/bqge197313/10070017.html']
    #bqge197313/all.html 主页面 
    #详情页面 content 里 p元素大于2 才是有内容的
    #

    """
    # 过滤字符串 html标签
    """
    def filter_tags(self,htmlstr):
        last_str = "*v本文*"
        first_str = "『章节错误,点此举报』"
        re_cdata = re.compile('//<!\[CDATA\[[^>]*//\]\]>', re.I)  # 匹配CDATA
        re_script = re.compile(
            '<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)  # Script
        re_style = re.compile(
            '<\s*style[^>]*>[^<]*<\s*/\s*style\s*>', re.I)  # style
        re_br = re.compile('<br\s*?/?>')  # 处理换行
        re_h = re.compile('</?\w+[^>]*>')  # HTML标签
        re_comment = re.compile('<!--[^>]*-->')  # HTML注释
        s = re_cdata.sub('', htmlstr)  # 去掉CDATA
        s = re_script.sub('', s)  # 去掉SCRIPT
        s = re_style.sub('', s)  # 去掉style
        s = re_br.sub('\n', s)  # 将br转换为换行
        s = re_h.sub('', s)  # 去掉HTML 标签
        s = re_comment.sub('', s)  # 去掉HTML注释

        # 去掉多余的空行
        blank_line = re.compile('\n+')
        s = blank_line.sub('\n', s)
        #
        s = re.compile('\r\n').sub('', s)
        s = s.replace(first_str, '')
        ls_index = s.index(last_str)
        s = s[:ls_index]
        # s = replaceCharEntity(s)  # 替换实体
        return s

    
    def parse(self, response):
        tmpStr = ""
        path = "../allnovel/bqge197313"
        filename = "../allnovel/bqge197313/10070017.json"
        
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
            
        item['content'] = self.filter_tags(item['content'])

        print("--------------------start")
        print(item)
        print("--------------------")
        file = open(filename,'w+')
       
        tmpStr = json.dumps(item)
        
        file.write(tmpStr)
        
        file.close();
