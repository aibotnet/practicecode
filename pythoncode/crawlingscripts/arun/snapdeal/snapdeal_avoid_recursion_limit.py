
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


def tail_rec(fun):
   def tail(fun):
      a = fun
      while callable(a):
         a = a()
      return a
   return (lambda x: tail(fun(x)))   
   

def extral_product_page_urls(url , k , file):
    
    try:
        doc = lh.parse(url)

        urls=doc.xpath('//div[@id="products-main4"]//div[@class="product-title"]/a/@href')
        
    except: 
        return
    
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
    #lambda: extral_product_page_urls(next_page_url , k , file) 
    
    

def for_each_thread(category_list , file_name):

    count=0
    k=0
    
    for i in category_list :
        #print i 
        #count +=1
        #print count
        extral_product_page_urls(i , k , file_name)
        #tail_rec(extral_product_page_urls)
   
   

 

def main():
    file1=open('/home/aknauhwar/Desktop/snapdeal/category1.txt' , 'a')

    url='http://www.snapdeal.com/info/sitemap'

    categories_urls=extract_categories_urls(url)

    #print categories_urls
    urls1=categories_urls[2:9]
    urls2=categories_urls[9:18]
    urls3=categories_urls[18:27]
    urls4=categories_urls[27:36]
    urls5=categories_urls[36:]
    
    for_each_thread(urls1 , file1)
 

        
main()

    
    
    
