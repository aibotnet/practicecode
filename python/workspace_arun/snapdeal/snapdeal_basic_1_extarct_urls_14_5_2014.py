
import lxml.html as lh
from threading import Thread



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
        print i
        k +=1
        print k
        file.write(str(url)+"|"+str(i)+"\n")
        
    next_page=doc.xpath('//div[@class="pageWrapper"]//noscript/div/a[@class="next"]/@href')
    if not next_page :
        return
    
    next_page_url= 'http://www.snapdeal.com'+str(next_page[0])
    extral_product_page_urls(next_page_url , k , file)
    

def for_each_thread(category_list , file_name):

    count=0
    k=0
    
    for i in category_list :
        print i 
        count +=1
        print count
        extral_product_page_urls(i , k , file_name)
    

def main():
    file1=open('/home/vkthakur/Desktop/snapdeal/category1.txt' , 'w')
    file2=open('/home/vkthakur/Desktop/snapdeal/category2.txt' , 'w')
    file3=open('/home/vkthakur/Desktop/snapdeal/category3.txt' , 'w')
    file4=open('/home/vkthakur/Desktop/snapdeal/category4.txt' , 'w')
    file5=open('/home/vkthakur/Desktop/snapdeal/category5.txt' , 'w')
    
    
    url='http://www.snapdeal.com/info/sitemap'
    categories_urls=extract_categories_urls(url)

    print categories_urls
    urls1=categories_urls[0:9]
    urls2=categories_urls[9:18]
    urls3=categories_urls[18:27]
    urls4=categories_urls[27:36]
    urls5=categories_urls[36:]
    

    '''t1 = Thread(target = for_each_thread(urls1 , file1))
    t2 = Thread(target = for_each_thread(urls2 , file2))
    t3 = Thread(target = for_each_thread(urls3 , file3))
    t4 = Thread(target = for_each_thread(urls4 , file4))
    t5 = Thread(target = for_each_thread(urls5 , file5))
    
    
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()'''
    
    
    
    '''    Thread.start_new_thread(for_each_thread,(urls1 , file1))
    Thread.start_new_thread(for_each_thread,(urls2 , file2))
    Thread.start_new_thread(for_each_thread,(urls3 , file3))
    Thread.start_new_thread(for_each_thread,(urls4 , file4))
    Thread.start_new_thread(for_each_thread,(urls5 , file5))'''
    
    '''Process(target=for_each_thread(urls1 , file1)).start()
    Process(target=for_each_thread(urls2 , file2)).start()
    Process(target=for_each_thread(urls3 , file3)).start()
    Process(target=for_each_thread(urls4 , file4)).start()
    Process(target=for_each_thread(urls5 , file5)).start()'''

    

    for i in range(1,6):
        print i

        if i==1 :
            l=urls1
            j=file1
            
        elif i==2 :
            l=urls2
            j=file2
        elif i==3 :
            l=urls3
            j=file3
            
        elif i==4 :
            l=urls4
            j=file4
            
        else :
            l=urls5
            j=file5
            
        t = Thread(target=for_each_thread , args=(l,j))
        t.start()   

main() 

    
    
    

    
    
    
    