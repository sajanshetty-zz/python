import scrapy

class QuoteSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/'
        ]

        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        #page = response.url.split("/")[-2]
        #filename = 'quotes-%s.html' % page   
        #with open(filename, 'wb') as f:
            #f.write(response.body)
        #self.log('Saved file %s' % filename) 
        for quote in response.css('div.quote'):
            yield {
                'text' : quote.css('span.text::text').get(),
                'author' : quote.css('small.autor::text').get(),
                'tags' : quote.css('div.tags a.tag::text').getall()            
            }
        #next_page = response.css('li.next a::attr(href)').get()
        """
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
        """
        """
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        """
        """
        for href in response.css('ul.pager a::attr(href)'):
            yield response.follow(href, callback=self.parse)
        """
        """
        for a in response.css('ul.pager a'):
            yield response.follow(a, callback=self.parse)
        """
        """
        anchors = response.css('ul.pager a')
        yield response.follow_all(anchors, callback=self.parse)
        """
        yield response.follow_all(css='ul.pager a', callback=self.parse)