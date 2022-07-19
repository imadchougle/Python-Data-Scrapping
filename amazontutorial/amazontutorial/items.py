# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonScrapperItem(scrapy.Item):
    # define the fields for your item here like:
    A_Product_Title = scrapy.Field()
    B_Product_Price = scrapy.Field()
    C_Image_Url = scrapy.Field()