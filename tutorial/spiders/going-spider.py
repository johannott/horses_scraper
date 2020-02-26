import scrapy
from scrapy.loader import ItemLoader
from tutorial.items import GoingItem


class GoingSpider(scrapy.Spider):
    name = "going"

    start_urls = [
        'http://maps.turftrax.co.uk/latestgoingreport.asp?course=Cheltenham'
    ]

    def parse(self, response):
        
        going = response.css('td.mapinfoheader div::text')[2].get()
        track = 'Cheltenham'
        loader = ItemLoader(item=GoingItem(), response=response)
        loader.add_value('track', track)
        loader.add_value('going', going)
        yield loader.load_item()

        # yield {
        #     'going': response.css('td.mapinfoheader div::text')[2].get()
        # }