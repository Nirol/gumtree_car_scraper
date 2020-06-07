# -*- coding: utf-8 -*-
import time

import scrapy
from scrapy import Selector, Spider
from scrapy.http import Response

from scrapy.linkextractors import LinkExtractor


from items import GummyHouseForSale, HOUSE_SELECTOR
from parsing.parse_house_for_sale import get_field_raw_output, \
    process_raw_output, save_to_item

HOUSE_LINK_RE = "\/p\/property-for-sale\/"

class GumtreeSpider(Spider):
    name = 'gummy_scrape_single_house'
    allowed_domains = ['gumtree.com']
    #start_urls = ['https://www.gumtree.com/search?search_category=property-for-sale&seller_type=trade&q=&distance=15&max_price=156000&min_property_number_beds=1&max_property_number_beds=4&photos_filter=true&search_scope=true']

    def start_requests(self):
        a = 'https://www.gumtree.com/search?featured_filter=false&q=house+for+sale&property_number_beds=4&search_category=property-for-sale&urgent_filter=false&property_type=house&sort=date&search_scope=false&photos_filter=false&search_location=London&tl=&distance=0.0001'
        b = "https://www.gumtree.com/search?featured_filter=false&q=house+for+sale&property_number_beds=4&search_category=property-for-sale&urgent_filter=false&property_type=house&sort=date&search_scope=false&photos_filter=false&search_location=London&tl=&distance=0.0001"
        yield scrapy.Request(b,
                             callback=self.parse, errback=self.handle_error )


    def parse(self, response):

        le = LinkExtractor(allow = HOUSE_LINK_RE)
        links = le.extract_links(response)
        for link in links:
            time.sleep(3)
            print(link.url)
            yield scrapy.Request(link.url, callback=self.analyze_house, errback=self.handle_error )




    def back_to_parsing(self, url):
        print("did i get here?")
        yield scrapy.Request(url, callback=self.parse, errback=self.handle_error)


    def handle_error(self, response: Response):
        print("encounter error:")
        print(response)
        print(response.value.response.status)
        print(response.value.response.url)
        print(response.request.url)
        from selenium import webdriver
        driver = webdriver.Firefox()
        driver.get(response.value.response.url)

        html_source = driver.page_source

        print("a")
        self.analyze_house(html_source)


    def analyze_house(self, response):
        # response = pickle.load(open("gummy_scrape/save_response.p", "rb"))
        selector = Selector(text=response.body)
        item = GummyHouseForSale()
        for field_key in HOUSE_SELECTOR:
            print(field_key)

            raw_output = get_field_raw_output(selector, field_key)
            clean_string_output = process_raw_output(field_key, raw_output)
            save_to_item(item, field_key, clean_string_output)
        yield item

