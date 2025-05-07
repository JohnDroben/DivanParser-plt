
import scrapy
from scrapy import signals


class DivannewparsSpider(scrapy.Spider):
    name = "divannewparser"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]
    custom_settings = {
        'FEED_FORMAT': 'csv',
        'FEED_URI': 'divan_prices.csv',
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        # Парсинг данных о диванах
        for sofa in response.css('div._Ud0k'):
            price_text = sofa.css('span[data-testid="price"]::text').get()

            # Обработка и очистка цены
            price = None
            if price_text:
                price = price_text.replace(' ', '').replace('₽', '').strip()
                if price.isdigit():
                    price = int(price)

            yield {
                'name': sofa.css('span[itemprop="name"]::text').get(),
                'price': price,
                'url': response.urljoin(sofa.css('a::attr(href)').get())
            }

        # Обработка пагинации
        next_page = response.css('a[data-testid="pagination-next"]::attr(href)').get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)


    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super().from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        spider.logger.info("Spider closed: %s" % spider.name)