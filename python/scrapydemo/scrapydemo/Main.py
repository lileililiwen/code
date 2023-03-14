from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

# 1. 创建一个 CrawlerProcess 对象
setting = get_project_settings()
dir(setting)
print("aaaaaaaaaaa")
process = CrawlerProcess(setting)

# 2. 添加需要运行的 Spider
process.crawl('example')

# 3. 启动爬虫
process.start()        