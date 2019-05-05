import scrapy
from scrapy.utils.response import open_in_browser


class MercadoLivreSpider(scrapy.Spider):
    name = "mercadolivre"

    def __init__(self, pesquisa='', *args, **kwargs):
        super(MercadoLivreSpider, self).__init__(*args, **kwargs)
        self.start_urls = [
          'https://lista.mercadolivre.com.br/%s' % pesquisa
        ]

    def parse(self, response):
        #open_in_browser(response)

        produtos = zip(response.css(".main-title::text").extract(),
                       response.css(".price__fraction::text").extract(),
                       response.css(".price__decimals::text").extract())

        for produto in produtos:
            yield {
                "titulo" : produto[0],
                "preco" : produto[1] + "," + produto[2]
            }
        
        if response.css(".andes-pagination__arrow-title::text").extract()[-1] == "Próxima":
            yield scrapy.Request(url=response.xpath('//a[@class="andes-pagination__link prefetch"]/@href').extract_first(), callback=self.parse)
    


