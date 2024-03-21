
# Mid_Term_Assignment_Scrapy

Assigned to scraping data from a website using Scrapy. This Python framework facilitates the extraction of desired information efficiently 


## Code to Scrapy 
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


#Intall scrapy and import, Nameing the spider as hollywood. For start URL, I have taken 4 cases with 4 different URL of same a website to scrap different cases.
 






## Response and Source Code 
    def parse(self, response):
        #Below are the names of the scraped items of website
        #css selector - where if condition used with css and title text
        title = response.css('title::text').extract()
        Rank = response.css('a.a-link-normal::text').extract()response.css('td.mojo-field-type-money::text').extract()
        Revenue = response.css('td.mojo-field-type-money::text').extract()
        combine = response.css('a.a-link-normal::text, td.mojo-field-type-money::text').extract()
        cast_crew =  response.css('a.a-link-normal::text').extract()
        release_region_avtaar = response.css('th::text,td::text').extract()

## create a Method  called parse- It requires 2  things - self instance/self-reference and  response which contains the source code of our website which we want to scrap
## Yield / Return
## Yield means it returns the data scraped from the URL and required source code from the website 
 yield {
            'titletext': title, #gettig Title of movies
            'ranktext': Rank, #getting top ranked movies
            'revenuetext': Revenue, #Getting top box offlice collection
            'movieyeartext': combine, #Getting movie, year and revenue
            'cast_crew': cast_crew, #Getting detail of cast and crew of Avtaar movie
            'release_region_avtaar': release_region_avtaar, #demogrpahic detail of avtaar movie
        }



## Terminal and Cases to extract
(.venv) (base) mrityunjay@Mrityunjays-MacBook-Pro assignment % cd assignment_scrapy 
(.venv) (base) mrityunjay@Mrityunjays-MacBook-Pro assignment_scrapy % scrapy crawl hollywood
####The above code in Terminal means that first we need to go to our folder by cd file name , then we need to run our crawler to scrape the complete website by running the code scrapy crawl hollwyood 
(.venv) (base) mrityunjay@Mrityunjays-MacBook-Pro assignment_scrapy % scrapy shell "https://www.boxofficemojo.com/chart/top_lifetime_gross/?area=XWW"
##Repeat the process everytime for new case with new URL
####scrapy shell means scraping specific URL which gives response>200, means scraped successfully. 
response.css("title::text").extract()   
##Case1           
  ## To extract the exact title in Terminal - This is the Exact Title 
['Top Lifetime Grosses - Box Office Mojo']       
 
 >>>response.css('td.mojo-field-type-money::text').extract() - ## Scraping all the revenue of all listed movies 

##Case 2 
>>>response.css('a.a-link-normal::text, td.mojo-field-type-money::text').extract()
##Scrpaing movie, year and revenue combined 

##Case 3
>>> response.css('a.a-link-normal::text').extract() 
##Scraping cast and crew of avatar movie 
>>>response.css('th::text,td::text').extract() 
  ##Scraping By release, region, rank data of avatar movie 

##Case 4 Scraping all 2009 movies list
>>>response.css('a.a-link-normal::text').extract() 


scrapy crawl hollywood -o output.json/csv
##exporting all the data into json and csv ( Run exit() )     