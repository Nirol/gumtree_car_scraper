import pymysql
from scrapy.exceptions import NotConfigured

from items import GummyHouseForSale
TABLE_NAME = "`houses`"
TABLE_FIELDS = "(`Ad_ID`, `Name`, `County`, `City`, `Price`, `Seller`, `ConcealedPhone`, `RevealURL`, `Posted`, `SellerType`, `Bedrooms`, `PropertyType`, `Description`, `VatNum`)"
INSERT_SQL_COMMAND = "INSERT INTO " + TABLE_NAME +"  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"




class GumtreePipelineSql(object):
    def __init__(self,db,user,password,host): 
        self.db = db
        self.user = user
        self.password = password
        self.host = host

    @classmethod
    def from_crawler(cls,crawler):
        db_settings = crawler.settings.getdict("DB_SETTINGS")
        if not db_settings:
            raise NotConfigured
        db = db_settings["db"]
        user = db_settings["user"]
        password = db_settings["password"]
        host = db_settings["host"]
        return cls(db,user,password,host)

    def open_spider(self,spider):
        spider.logger.info("open_spider method in pipeline")
        self.conn = pymysql.connect(db=self.db,
                                    user=self.user, password = self.password,
                                    host=self.host,
                                    charset = 'utf8', use_unicode=True)
        self.cursor = self.conn.cursor()




    def process_item(self,item: GummyHouseForSale,spider):
        spider.logger.info('Processing a new item:')
        spider.logger.info("AD ID:" + item.get("ad_id"))
        sql = (INSERT_SQL_COMMAND)
        self.cursor.execute(sql,
                             (
                                 int(item.get("ad_id")),
                                item.get("name"),
                                item.get("county"),
                                int(item.get("price")),
                                item.get("seller"),
                                int(item.get("concealed_phone")),
                                item.get("reveal_url"),
                                item.get("posted"),
                                item.get("seller_type"),
                                int(item.get("bedrooms")),
                                item.get("property_type")

                              )
                            )
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()

