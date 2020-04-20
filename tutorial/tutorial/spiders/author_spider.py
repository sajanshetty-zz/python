import scrapy

class AuthorSpider(scrapy.Spider):
    name = 'author'

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        for a in response.css('small.author + a'):
            yield response.follow(a, callback=self.parse_author)
         
    def parse_author(self, response):
        yield {
            'name': response.css('h3.author-title::text').get(),
            'dob' : response.css('span.author-born-date::text').get(),
            'born_location' : response.css('span.author-born-location::text').get(),
            'description' : response.css('div.author-description::text').get()
        }


