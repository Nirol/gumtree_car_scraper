# -*- coding: utf-8 -*-
import scrapy
import datetime

def make_info(response,value):
    return response.xpath('//div[@class="attribute"]/span[text()="'+ value +':"]/following-sibling::a/span/text()').get()  

def car_info(response,value):
    return response.xpath('//div[@class="attribute"]/span[text()="'+ value +':"]/following-sibling::span/text()').get()      

def description_info(response,value):
    return response.xpath('//div[@class="description-content"]/b[text()="'+ value +'"]/following-sibling::text()').get()  



class GumtreeSpider(scrapy.Spider):
    name = 'gumtree'
    # allowed_domains = ['https://gumtree.co.za/']
    start_urls = ['https://gumtree.co.za/s-cars-bakkies/v1c9077p1']

    def parse(self, response):
        car_links = response.xpath('//*[@class="related-ad-title"]/@href').extract() 
        for car in car_links:
            absolute_url = 'https://www.gumtree.co.za' + car
            yield scrapy.Request(absolute_url,callback= self.parse_car)

        next_page_url =  response.xpath('//*[@class=" icon-pagination-right"]/@href').get() 

        if next_page_url:
            absolute_next_page_url = 'https://www.gumtree.co.za' + next_page_url
            yield scrapy.Request(absolute_next_page_url)

    def parse_car(self,response):
        title = response.xpath('///h1/text()').get()
        price = response.xpath('//*[@class="ad-price"]/text()').get()
        #Clean price text: 
        price =  price.splitlines()[1].split('R')[1]
        suburb = response.xpath('//*[@class="location"]/a[1]/text()').extract()
        city = response.xpath('//*[@class="location"]/a[2]/text()').extract()

        # the next items are obtained with a function (top of page)
        make = make_info(response,'Make')
        model = make_info(response,'Model')

        # the next items are obtained with a function (top of page)
        for_sale_by = car_info(response,'For Sale By')
        kilometers = car_info(response,'Kilometers')
        transmission = car_info(response,'Transmission')
        fuel_type = car_info(response,'Fuel Type')
        colour = car_info(response,'Colour')

        # the next items are obtained with a function (top of page)
        power = description_info(response,'Power')
        torque = description_info(response,'Torque')
        economy  = description_info(response,'Economy')
        gears  = description_info(response,'Gears')
        length  = description_info(response,'Length')
        seats  = description_info(response,'Seats')
        tank_capacity  = description_info(response,'Fuel Tank Capacity')
        service_intervals = description_info(response,'Service Intervals')



        yield{
            'date':datetime.datetime.now(),
            'title':title,
            'price':price,
            'suburb':suburb,
            'city':city,
            'make':make,
            'model':model,
            'for_sale_by':for_sale_by,
            'kilometres':kilometers,
            'transmission':transmission,
            'fuel_type':fuel_type,
            'colour':colour,
            'power':power,
            'torque':torque,
            'economy':economy,
            'gears':gears,
            'length ':length ,
            'seats':seats,
            'tank_capacity':tank_capacity,
            'service_intervals':service_intervals,
        }







