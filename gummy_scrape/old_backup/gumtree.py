# -*- coding: utf-8 -*-
from urllib.request import Request

import scrapy
import datetime
import os
import csv
import glob

from scrapy.utils import spider





class GumtreeSpider(scrapy.Spider):
    name = 'gummy_scrape'
    #allowed_domains = ['https://gumtree.co.za/']
    start_urls = ['https://gumtree.co.za/s-cars-bakkies/v1c9077p1']


    # def start_requests(self):
    #     yield Request(
    #         'https://gumtree.co.za/s-cars-bakkies/v1c9077p1',
    #         headers={
    #             'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"})



    def parse(self, response):
        # Province links - from the main page in "Cars and Bakkies"

        for province in response.xpath('//*[@class="finalsub inventoryView more"]/li/span[@class="text"]/a/@href').extract()[:9]:
            print("inv province")
            absolute_province_url = 'https://www.gumtree.co.za' + province
            print("absolute_province_url:"+absolute_province_url)
            yield scrapy.Request(absolute_province_url)

            # list of location links per province 
            for location in response.xpath('//div[@class="foldableList"]/ul[contains(@class,"finalsub")]/li/span/a/@href').extract()[1:]:
                absolute_location_url = 'https://www.gumtree.co.za' + location
                yield scrapy.Request(absolute_location_url)

                # Car add links per page -  for a specific location
                car_links = response.xpath('//*[@class="related-ad-title"]/@href').extract() 
                for car in car_links:
                    absolute_car_url = 'https://www.gumtree.co.za' + car
                    yield scrapy.Request(absolute_car_url,callback= self.parse_car2)
                    #yield from self.parse_car2(absolute_car_url)
                    #yield from self.parse_car2(absolute_car_url)



                #
                # next_page_url =  response.xpath('//*[@class=" icon-pagination-right"]/@href').get()

                # if next_page_url:
                #     absolute_next_page_url = 'https://www.gumtree.co.za' + next_page_url
                #     yield scrapy.Request(absolute_next_page_url)





    def parse_car2(self,response):
        item = GummyScrapeItem()
        item['link'] = response.url
        print("123")
        print("123")
        print("123")
        city = response.xpath('//*[@class="location"]/a[2]/text()').extract()
        item['city'] = city
        print("123")

        title = response.xpath('///h1/text()').get()
        price = response.xpath('//*[@class="ad-price"]/text()').get()
        print("123")
        print("123")
        suburb = response.xpath('//*[@class="location"]/a[1]/text()').extract()
        city = response.xpath('//*[@class="location"]/a[2]/text()').extract()
        item['city'] = city



    def parse_car(self,response):


        item = GummyScrapeItem()
        print("inside parse_car")
        item['car_url'] = response.url
        link = response.url
        title = response.xpath('///h1/text()').get()
        price = response.xpath('//*[@class="ad-price"]/text()').get()
        #Clean price text: 
        # price =  price.splitlines()[1].split('R')[1]
        # province = response.xpath('//h2/span/span/a/span/text()').extract()[0]
        # suburb = response.xpath('//*[@class="location"]/a[1]/text()').extract()
        # city = response.xpath('//*[@class="location"]/a[2]/text()').extract()
        #
        # # the next items are obtained with a function (top of page)
        # make = make_info(response,'Make')
        # model = make_info(response,'Model')
        #
        # # the next items are obtained with a function (top of page)
        # for_sale_by = car_info(response,'For Sale By')
        # kilometers = car_info(response,'Kilometers')
        # transmission = car_info(response,'Transmission')
        # fuel_type = car_info(response,'Fuel Type')
        # colour = car_info(response,'Colour')
        #
        # # the next items are obtained with a function (top of page)
        # power = description_info(response,'Power')
        # torque = description_info(response,'Torque')
        # economy  = description_info(response,'Economy')
        # gears  = description_info(response,'Gears')
        # length  = description_info(response,'Length')
        # seats  = description_info(response,'Seats')
        # tank_capacity  = description_info(response,'Fuel Tank Capacity')
        # service_intervals = description_info(response,'Service Intervals')

        yield item
        #
        # yield{
        #     'add_date':datetime.datetime.now(),
        #     'title':title,
        #     'price':price,
        #     'suburb':suburb,
        #     'city':city,
        #     'province':province,
        #     'make':make,
        #     'model':model,
        #     'for_sale_by':for_sale_by,
        #     'kilometres':kilometers,
        #     'transmission':transmission,
        #     'fuel_type':fuel_type,
        #     'colour':colour,
        #     'power':power,
        #     'torque':torque,
        #     'economy':economy,
        #     'gears':gears,
        #     'length ':length,
        #     'seats':seats,
        #     'tank_size':tank_capacity,
        #     'service_intervals':service_intervals,
        #     'link': link,
        #     }
        #
        #


