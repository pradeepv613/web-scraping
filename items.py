# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Task1Item(scrapy.Item):
    product_url=scrapy.Field()
    product_name=scrapy.Field()
    product_image=scrapy.Field()
    product_brand=scrapy.Field()
    product_price=scrapy.Field()
    
   