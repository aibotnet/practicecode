
import lxml.html as lh
import sys

sys.setrecursionlimit(50000)


def extract_categories_urls(url):

    doc = lh.parse(url)

    urls=doc.xpath('//div[@class="sitemap-cont"]/div/div/a/@href')

    #print urls

    list=[]
    count=0
    
    for i in urls :
        count +=1
        #print count
        #print i
        list.append(i+"?sort=plrty&")
        #print list[count-1]
        
        
    return list

def extral_product_page_urls(url , k , file):
    
    doc = lh.parse(url)

    urls=doc.xpath('//div[@id="products-main4"]//div[@class="product-title"]/a/@href')
    
    for i in urls : 
        #print i
        k +=1
        #print k
        file.write(str(url)+"|"+str(i)+"|"+str(k)+"\n")
        
    next_page=doc.xpath('//div[@class="pageWrapper"]//noscript/div/a[@class="next"]/@href')
    if not next_page :
        return
    
    next_page_url= 'http://www.snapdeal.com'+str(next_page[0])
    extral_product_page_urls(next_page_url , k , file)
    

def for_each_thread(category_list , file_name):

    count=0
    k=0
    
    for i in category_list :
        #print i 
        #count +=1
        #print count
        extral_product_page_urls(i , k , file_name)
    

def main():
    file3=open('/home/vkthakur/Desktop/snapdeal/category3.txt' , 'w')

    url='http://www.snapdeal.com/info/sitemap'

    categories_urls=extract_categories_urls(url)

    #print categories_urls
    urls1=categories_urls[0:9]
    urls2=categories_urls[9:18]
    urls3=categories_urls[18:27]
    urls4=categories_urls[27:36]
    urls5=categories_urls[36:]
    
    for_each_thread(urls3 , file3)
 
    

       
        
        
main()

    
    
    
