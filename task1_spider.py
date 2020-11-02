
import scrapy
from ..items import Task1Item
class Bluespider(scrapy.Spider):
    
    name='task1_spider'
    i=2
    #download_delay = 5.0
    start_urls={
        
        'https://www.farfetch.com/de/shopping/men/shoes-2/items.aspx?view=90&sort=1&scale=282'
       
         }
    
    def parse(self, response):
         
         items=Task1Item()
         product_url=response.xpath('//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li/a/@href').extract()
         product_name=response.xpath('//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li/a/div/p/text()').extract()
         product_image=response.xpath('//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li/a/meta/@content').extract()
         product_brand=response.xpath('//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li/a/div/h3/text()').extract()
         product_price=response.xpath('//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li/a/div[2]/div/span').re(r'[\d.,]+')
         
        
         for items in zip(product_name,product_price,product_image,product_url,product_brand):
            #create a dictionary to store the scraped info
            scraped_info = {
                'product_name':items[0],
                'product_price':items[1],
                'product_image':items[2],
                'product_url':items[3],
                'product_brand':items[4]
                
                
            }
             #yield or give the scraped info to scrapy
            yield scraped_info
         next_page ='https://www.farfetch.com/in/shopping/men/shoes-2/items.aspx?page='+ str(Bluespider.i) +'&view=90&sort=4&scale=283'
         if Bluespider.i<=189:
             Bluespider.i+=1
             yield response.follow(next_page,callback=self.parse)
        
    
            
    
        

         
#//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li[1]/a/div[1]/img
#//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li[1]/a/div[1]/img
# //*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li[1]/a/div[2]/p
#//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li[1]/a/div[1]/img
#//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li[1]/a/div[1]/img
#//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li[1]/a/meta[1]
#//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li[1]/a/div[2]/h3
#//*[@id="slice-container"]/div[3]/div/div[2]/div/div[1]/ul/li[1]/a/div[2]/div/span