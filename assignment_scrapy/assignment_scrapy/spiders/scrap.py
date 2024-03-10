import scrapy
class boxoffice_collection(scrapy.Spider):
    name = 'hollywood'
    start_urls = [
        'https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW'
        'https://www.boxofficemojo.com/title/tt0499549/credits/?ref_=bo_tt_tab#tabs'
        'https://boxofficemojo.com/title/tt0499549/?ref_=bo_tt_tab#tabs'
        'https://www.boxofficemojo.com/year/world/2009/?ref_=bo_cso_table_1'
    ]
    #response = source code
    def parse(self, response):
        #we just want title so put double colon and text
        #css selector - where if condition used with css and title text
        title = response.css('title::text').extract()
        #yield result
        yield {'titletext': title}



