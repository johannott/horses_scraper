import scrapy
from scrapy.loader import ItemLoader
from tutorial.items import TrackItem


class GoingSpider(scrapy.Spider):
    name = "going"

    start_urls = [
        'http://maps.turftrax.co.uk/latestgoingreport.asp?course=Cheltenham'
    ]

    def parse(self, response):
        
        going = response.css('td.mapinfoheader div::text')[2].get()
        track = 'Cheltenham(New)'
        loader = ItemLoader(item=TrackItem(), response=response)
        loader.add_value('track_name', track)
        loader.add_value('current_going', going)
        yield loader.load_item()

        # yield {
        #     'going': response.css('td.mapinfoheader div::text')[2].get()
        # }