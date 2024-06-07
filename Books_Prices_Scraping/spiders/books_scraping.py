import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BooksScrapingSpider(CrawlSpider):
    name = "books_scraping"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com"]

    rules = (
        Rule(LinkExtractor(restrict_xpaths='//li[@class="col-xs-6 col-sm-4 col-md-3 col-lg-3"]/article/h3/a'), callback="parse_item", follow=True,),
        Rule(LinkExtractor(restrict_xpaths='////li[@class="next"]/a'), ),
        )
    def parse_item(self, response):
        yield {
            'Title':response.xpath('//div[@class="col-sm-6 product_main"]/h1/text()').get(),
            'Price':response.xpath('//div[@class="col-sm-6 product_main"]/p[@class="price_color"]/text()').get(),
            'Availablity':response.xpath('normalize-space((//div[@class="col-sm-6 product_main"]/p[2]/text())[2])').get(),
            'url':response.url,
        }
