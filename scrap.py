# 1.首先安装Python3.3版本
# 2.配置好PYTHON_HOME环境变量，指向Python33目录，假定C:\Python33
# 3.安装以下包，请注意如果是64位系统，下列某些包官方不提供64位版本，自己查找其64位版本，因此32位系统最简单了
# 	install lxml python package
# 	install curl python package
# 	install grab python package
# 4.修改keyword变量搜索指定的百度搜索关键词
# 5.命令行运行 python C:\scrap.py 即可（此操作会在scrap.py文件同级目录生成记录了含有href属性超链接内容的scrap.txt文件）

from grab.spider import Spider, Task
from grab.error import DataNotFound
import logging

class ExampleSpider(Spider):
    def task_generator(self):
        # for keyword in ('QQ', 'python', 'ruby', 'perl'):
        # 百度一下 http://www.baidu.com/s?ie=utf-8&mod=2&cqid=cbe75d040002f579&pstg=5&istc=14121&ver=RgkaGwZXOu4aje7d6_4X639X20V5XyuUDY3&chk=53e241f8&isid=2B932B6CE6144341&wd=QQ&ie=utf-8&tn=baiduhome_pg&rsv_spt=1&issp=1&rsv_bp=0&rsv_sug3=7&rsv_sug4=563&rsv_sug1=5&inputT=14613&rsv_sug=2&_ck=1827.1.148.52.5.13.5.963.271
        # 百度一下最简搜索方式 http://www.baidu.com/s?wd=QQ
        # 百度一下最简带分页编码搜索方式 http://www.baidu.com/s?wd=qq&pn=10&oq=QQ&ie=utf-8&usm=10
        # url = 'https://www.google.com/search?q=%s' % keyword
        keyword = 'qq'
        url = 'http://www.baidu.com/s?wd=%s' % keyword
        yield Task('search', url=url)

    def task_search(self, grab, task):
    	archors = grab.doc.select('//div[@id="content_left"]//a')
    	for a in archors:
    		try:
    			# print(grab.make_url_absolute(a.attr("href"), resolve_base=True))
    			with open("scraped.txt", "a") as f:
    				f.write(grab.make_url_absolute(a.attr("href"), resolve_base=True)+"\n")
    			f.close();
    		except DataNotFound as e:
    			print(e)


logging.basicConfig(level=logging.DEBUG)
bot = ExampleSpider()
bot.run()