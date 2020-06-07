import scrapy


HOUSE_SELECTOR = {
    "name" : '//h1[@itemprop="name"]/text()',
    "location" : '//*[@class="ad-location truncate-line set-left"]//span[@itemprop="address"]/text()',
    "price_currency" :  '//*[@class="set-right space-mvn"]//meta[@itemprop="priceCurrency"]/@content',
    "price_value" : '//*[@class="set-right space-mvn"]//meta[@itemprop="price"]/@content',
    "seller" : '//h2[@class=" truncate-line space-mbn"]/text()',
    "concealed_phone" : '//*[@class="txt-large txt-emphasis form-row-label"]/text()',
    "reveal_url" :  '//div[@class="space-pas"]/div[@class="clearfix"]/a/@href',
    "description" :  '//p[contains(@class,"ad-description") and contains(@itemprop,"description")]/text()',
    "ad_id" : '//*[contains(@class,"txt-emphasis") and contains(@itemprop,"sku")]/text()',
    "vat_num" : '//p[@data-q="vip-vat"]//span[@class="txt-emphasis"]/text()',
    "posted" : '//*[@class="dl-attribute-list attribute-list1"]/dd[1]/text()',
    "seller_type" :  '//*[@class="dl-attribute-list attribute-list1"]/dd[2]/text()',
    "bedrooms" :  '//*[@class="dl-attribute-list attribute-list2"]/dd[2]/text()',
    "property_type" : '//*[@class="dl-attribute-list attribute-list2"]/dd[1]/text()'
 }

HOUSE_SELECTOR_EXTRACT_FIRST = { "reveal_url": True,
                                 "concealed_phone" : True,
                                 "seller" : True
                                 }

class GummyHouseForSale(scrapy.Item):
    name = scrapy.Field()
    county = scrapy.Field()
    city = scrapy.Field()
    price_currency = scrapy.Field()
    price_value = scrapy.Field()
    seller = scrapy.Field()


    concealed_phone = scrapy.Field()
    reveal_url = scrapy.Field()


    posted = scrapy.Field()
    seller_type = scrapy.Field()
    bedrooms = scrapy.Field()
    property_type = scrapy.Field()


    description = scrapy.Field()
    ad_id = scrapy.Field()
    vat_num = scrapy.Field()


