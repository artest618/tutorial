# chapter
"""
id 获取 all 下的列表
"""
import os

class chapter():
    novel_id = 'bqge197313' 
    novel_path = "../allnovel/"
    name = 'chapter'
    allowed_domains = ['m.biqudao.com']
    start_urls = ['https://m.biqudao.com/bqge197313/10070017.html']

    def getAllChapterLink(self):
        if os.path.exists(self.novel_path+self.novel_id):
            pass
        else:
            os.mkdir(self.novel_path+self.novel_id)

    
