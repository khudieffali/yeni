import scrapy


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quote = response.xpath(".//span[@class='text']/text()").extract()
        author= response.xpath(".//small[@class='author']/text()").extract()
        link =  response.css("a::attr('href')").extract()
        tag = response.xpath(".//a[@class='tag']/text()").extract()
        
        
        for item in zip(quote, author, link, tag):
            Post= {
                "Quotes": quote[0],
                "Müəlliflər": author[1],
                "Linkler": link[2],
                "Tagler": tag[3]
                }
            yield Post
