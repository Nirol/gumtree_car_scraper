import pymysql
from scrapy.exceptions import NotConfigured


class GumtreePipeline(object):
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
        print("\n THE spider of mens \n")
        self.conn = pymysql.connect(db=self.db,
                                    user=self.user, password = self.password,
                                    host=self.host,
                                    charset = 'utf8', use_unicode=True)
        self.cursor = self.conn.cursor()

    def process_item(self,item,spider):
        print("\n SQL TIME BEBE \n")
        sql = ("INSERT INTO gumtree VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")
        self.cursor.execute(sql,
                             (
                                item.get("add_date"),
                                item.get("title"),  
                                item.get("price"),  
                                item.get("suburb"),  
                                item.get("city"),  
                                item.get("province"),  
                                item.get("make"),  
                                item.get("model"),  
                                item.get("for_sale_by"),  
                                item.get("kilometers"),  
                                item.get("transmission"),  
                                item.get("fuel_type"),  
                                item.get("colour"),  
                                item.get("power"),  
                                item.get("torque"),  
                                item.get("economy"),  
                                item.get("gears"),  
                                item.get("length"),  
                                item.get("seats"),  
                                item.get("tank_size"),  
                                item.get("service_intervals"),  
                                item.get("link"),                   
                              )
                            )
        self.conn.commit()
        return item

    def close_spider(self,spider):
        self.conn.close()

