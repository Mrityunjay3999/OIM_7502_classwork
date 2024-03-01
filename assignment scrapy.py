pip install scrapy
import scrapy
class SP500Spider(scrapy.Spider):
    name = 'sp500'
    start_urls = ['https://www.slickcharts.com/sp500/performance']

    def parse(self, response):
        for row in response.xpath('//table[@id="performance"]//tr[position()>1]'):
            yield {
                'number': row.xpath('.//td[1]/text()').get(),
                'company': row.xpath('.//td[2]/text()').get(),
                'symbol': row.xpath('.//td[3]/text()').get(),
                'ytd_return': row.xpath('.//td[8]/text()').get()  # Fix index for ytd_return
            }
