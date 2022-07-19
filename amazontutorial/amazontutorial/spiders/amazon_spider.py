import scrapy
from ..items import AmazonScrapperItem

class AmazonBotSpider(scrapy.Spider):
    name = 'amazon_spider'
    count = 1
    start_urls = ['https://www.amazon.com/s?k=headphones&page=1&qid=1624791620&ref=sr_pg_3']

    def parse(self, response):
        product = AmazonScrapperItem()
        A_Product_Title = response.css(".a-size-medium.a-text-normal::text").extract()
        B_Product_Price = response.css(".sg-col-12-of-20 .a-price-whole::text").extract()
        C_Image_Url = response.css(".s-image-fixed-height .s-image").css("::attr(src)").extract()
        product["A_Product_Title"] = A_Product_Title
        product["B_Product_Price"] = B_Product_Price
        product["C_Image_Url"] = C_Image_Url
        yield product

        AmazonBotSpider.count += 1
        nxt_page = "https://www.amazon.com/s?k=heaphones&page=" + str(
            AmazonBotSpider.count) + "&qid=1624791620&ref=sr_pg_3"

        if AmazonBotSpider.count < 100:
            yield response.follow(nxt_page, callback=self.parse)

