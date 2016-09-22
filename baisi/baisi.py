
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re
class QSBK:
    #初始化方法
    def __init__(self):
        self.page = 1

        self.user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
        # 初始化header
        self.headers = {'User-Agent': self.user_agent}
        # 存放段子的变量，每一个元素是每一页的段子们
        self.stories = []
        # 存放程序是否继续运行的变量
        self.enable = False

    # 传入某一页的索引获得页面代码
    def getPage(self,indexPage):
        url = 'http://www.qiushibaike.com/hot/page/' + str(indexPage)

        try:
            request = urllib2.Request(url,headers=self.headers)
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8')
            return content
            # print content





        except urllib2.URLError, e:
            if hasattr(e ,"code"):
                print e.code
            if hasattr(e ,"reason"):
                print e.reason

    def getPageItems(self, pageIndex):
        pageCode = self.getPage(pageIndex)
        if not pageCode:
            print '加载页面失败'
            return None

        pattern = re.compile('<a href=".*?" target=".*?" title=".*?">.*?' +
                             '<h2>(.*?)</h2>.*?</a>.*?<div class=".*?">' +
                             '*?</div>.*?</div>.*?<a .*?>' +
                             '.*?<div class="content">.*?<span>(.*?)</span>.*?</div>'
                             , re.S)
        items = re.findall(pattern, pageCode)
        return items

    def loadPage(self):
        if self.enable == True:
            if len(self.stories) <2:
                pageStories = self.getPageItems(self.page)
                if pageStories:
                    self.stories.append(pageStories)
                    self.page += 1


    def getOneStory(self, pageStories, page):
        # 遍历一页的段子
        for story in pageStories:
            # 等待用户输入
            input = raw_input()
            # 每当输入回车一次，判断一下是否要加载新页面
            self.loadPage()
            # 如果输入Q则程序结束
            if input == "Q":
                self.enable = False
                return
            print story[1] + '\n' + story[0] + '~'
            print '---------------------------------'


            # 开始方法

    def start(self):
        print u"正在读取糗事百科,按回车查看新段子，Q退出"
        # 使变量为True，程序可以正常运行
        self.enable = True
        # 先加载一页内容
        self.loadPage()
        # 局部变量，控制当前读到了第几页
        nowPage = 0
        while self.enable:
            if len(self.stories) > 0:
                # 从全局list中获取一页的段子
                pageStories = self.stories[0]
                # 当前读到的页数加一
                nowPage += 1
                # 将全局list中第一个元素删除，因为已经取出
                del self.stories[0]
                # 输出该页的段子
                self.getOneStory(pageStories, nowPage)


spider = QSBK()
spider.start()