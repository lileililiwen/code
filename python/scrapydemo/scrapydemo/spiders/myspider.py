import scrapy
import json

# 在Scrapy中，settings.py是默认的配置文件名，并且在项目中必须存在，因为Scrapy框架会自动加载该文件中的配置信息。如果你想要改变配置文件的名称，可以在项目中自定义一个配置文件，并在启动爬虫时指定该文件。

# 具体而言，可以通过在命令行中添加-s参数，指定自定义的配置文件。例如：
# scrapy crawl spider_name -s my_settings.py

class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['example.com']
    # 列表开始页
    start_urls = ['http://www.example.com/page1']

    def parse(self, response):
        # 处理列表页
        for sel in response.xpath('//div[@class="list-item"]'):
            item = {}
            item['title'] = sel.xpath('h2/a/text()').extract_first()
            item['link'] = sel.xpath('h2/a/@href').extract_first()
            # 跟进链接爬取详情页
            yield scrapy.Request(item['link'], callback=self.parse_detail, meta={'item': item})

        # 处理分页链接
        next_page_url = response.xpath('//a[@class="next-page"]/@href')
        if next_page_url:
            yield scrapy.Request(next_page_url.extract_first(), callback=self.parse)

    def parse_detail(self, response):
        # 处理详情页
        item = response.meta['item']
        item['content'] = response.xpath('//div[@class="content"]/text()').extract()
        yield item


