import scrapy


class VfsaiSpider(scrapy.Spider):
    name = "vfsai"
    allowed_domains = ["visa.vfsglobal.com"]
    start_urls = ["https://visa.vfsglobal.com/npl/en/ltp/login"]

    def parse(self, response):
        # Extract the cookie popup element
        cookie_popup = response.css('.ot-sdk-row').get()

        if cookie_popup:
            self.log(f"Cookie popup found: {cookie_popup[:100]}")  # Log the first 100 characters
            yield {"cookie_popup": cookie_popup}  # Return the data as an item
        else:
            self.log("No cookie popup found.")
            yield {"cookie_popup": None}  # Return None if no popup is found
