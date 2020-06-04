from scrapy import Item, Field
import scrapy

class GummyScrapeItem(scrapy.Item):
    # add_date.Field()
    # title.Field()
    # price.Field()
    # suburb.Field()
    # city.Field()
    # province.Field()
    # make.Field()
    # model.Field()
    # for_sale_by.Field()
    # kilometers.Field()
    # transmission.Field()
    # fuel_type.Field()
    # colour.Field()
    # power.Field()
    # torque.Field()
    # economy.Field()
    # gears.Field()
    # length.Field()
    # seats.Field()
    # tank_capacity.Field()
    # service_intervals.Field()
    # link.Field()
    add_date = Field()
    title = Field()
    price = Field()
    suburb = Field()
    city = Field()
    province = Field()
    make = Field()
    model = Field()
    for_sale_by = Field()
    kilometers = Field()
    transmission = Field()
    fuel_type = Field()
    colour = Field()
    power = Field()
    torque = Field()
    economy = Field()
    gears = Field()
    length = Field()
    seats = Field()
    tank_capacity = Field()
    service_intervals = Field()
    link = Field()


