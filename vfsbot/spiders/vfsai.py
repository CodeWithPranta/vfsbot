import scrapy


class VfsaiSpider(scrapy.Spider):
    name = "vfsai"
    allowed_domains = ["visa.vfsglobal.com"]
    start_urls = ["https://visa.vfsglobal.com/npl/en/ltp/login"]

    def parse(self, response):
        pass
