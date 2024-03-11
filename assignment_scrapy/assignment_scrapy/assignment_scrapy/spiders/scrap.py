#Name: Mrityunjay Misra
#Library: Scrapy
#URL: https://docs.scrapy.org/en/latest/intro/install.html
#Description: Scrapy, Open source web-crawling framework in Python, that scrap website and give' the rquired data

import scrapy
class BoxOfficeCollection(scrapy.Spider):
    #name of scrapy
    name = 'hollywood'
    start_urls = [
        'https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW',
        'https://www.boxofficemojo.com/title/tt0499549/credits/?ref_=bo_tt_tab#tabs',
        'https://boxofficemojo.com/title/tt0499549/?ref_=bo_tt_tab#tabs',
        'https://www.boxofficemojo.com/year/world/2009/?ref_=bo_cso_table_1'
    ]
    #response = source code( takene from HTML of website to get specfic locaiton to scrap
    def parse(self, response):
        #Below are the names of the scraped items of website
        #css selector - where if condition used with css and title text
        title = response.css('title::text').extract()
        Rank = response.css('a.a-link-normal::text').extract()
        Revenue = response.css('td.mojo-field-type-money::text').extract()
        combine = response.css('a.a-link-normal::text, td.mojo-field-type-money::text').extract()
        cast_crew =  response.css('a.a-link-normal::text').extract()
        release_region_avtaar = response.css('th::text,td::text').extract()

        # yield result of the above css selectors statements
        yield {
            'titletext': title, #gettig Title of movies
            'ranktext': Rank, #getting top ranked movies
            'revenuetext': Revenue, #Getting top box offlice collection
            'movieyeartext': combine, #Getting movie, year and revenue
            'cast_crew': cast_crew, #Getting detail of cast and crew of Avtaar movie
            'release_region_avtaar': release_region_avtaar, #demogrpahic detail of avtaar movie
        }
