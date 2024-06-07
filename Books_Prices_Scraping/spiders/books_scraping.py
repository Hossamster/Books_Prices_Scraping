import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksScrapingSpider(CrawlSpider):
    name = "books_scraping"
    allowed_domains = ["books.toscrape.com"]
    # start_urls = ["https://books.toscrape.com"]
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Safari/605.1.15"
    def start_requests(self):
        yield scrapy.Request(url = 'https://books.toscrape.com',headers={'User-Agent': self.user_agent})
        return super().start_requests()
    rules = (
        Rule(LinkExtractor(restrict_xpaths='//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]/article/h3/a'), callback="parse_item", follow=True,process_request='set_user_agent'),
        Rule(LinkExtractor(restrict_xpaths='////li[@class="next"]/a'), process_request='set_user_agent'),
        )

    def set_user_agent(self, request, spider):
        request.headers['User-Agent']= self.user_agent
        return request
    def parse_item(self, response):
        yield {
            'Title':response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get(),
            'Price':response.xpath('//div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()').get(),
            'Availablity':response.xpath('normalize-space((//div[@class="col-sm-6 product_main"]/p[2]/text())[2])').get(),
            'url':response.url,
        }
