import scrapy
from scrapy.utils.response import open_in_browser


class UolSpider(scrapy.Spider):

    name = "Uol"

    start_urls = { 'https://www.uol.com.br/' }
    
    def parse(self, response):
        dolar = response.css('.currency_quote__down::text').extract_first()
        #open_in_browser(response)

        print('A cotação do Dólar é: '+dolar)
        
        #EXECUTAR COMANDO SEM LOG >>  scrapy runspider Questao2.py --nolog