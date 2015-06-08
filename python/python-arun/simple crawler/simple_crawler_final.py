from lxml import etree
import sys
import time
import pycurl



urls = ["http://www.amazon.com/product-reviews/B007SBGF12","http://www.amazon.com/product-reviews/B008MPMNFK"]
#id('productReviews')/tbody/tr/td[1]/div[1]/div[2]/span[2]/nobr/text()

class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf
#output=open('/home/aknauhwar/Desktop/crawler_data6.2', "w")
output1=open('/home/aknauhwar/Desktop/crawler_data6.2.2', "w")

#def start_operations():
    #crawl the given webpage taking one url at-a-time from urls


def crawl(uri):
    t = Test()
    c = pycurl.Curl()
    print "Crawling ", uri
    c.setopt(c.URL, uri)
    c.setopt(c.WRITEFUNCTION, t.body_callback)
    c.setopt(pycurl.FOLLOWLOCATION,1)
    c.setopt(pycurl.CONNECTTIMEOUT, 120)
    c.setopt(pycurl.MAXREDIRS, 5)
    c.setopt(pycurl.TIMEOUT, 300)
    c.setopt(pycurl.NOSIGNAL, 1)
    c.perform()
    c.close()
    #output.write(t.contents)
    #output.close()   
    #print t.contents
    r= t.contents
    data=etree.HTML(r)
    #p = data.xpath("//nobr/text()")
    #print p
    for i in range(1,11) :
        
        
        
        
        a="//*[@id='productReviews']//tr[1]/td[1]/div[%d]/div[3]/div[1]/div[2]/a[1]/span/text()"%(i)
        #print a
        #p=data.xpath("//*[@id='productReviews']//tr[1]/td[1]/div["+str(i)+"]/div[3]/div[1]/div[2]/a[1]") 
        p=data.xpath(a)
        #print p
        r = p[0]
        #print r
        #print r      #author
        output1.write('%d  '%(i) +r+'\n')
        
        
        a="//*[@id='productReviews']//tr[1]/td[1]/div[%d]/div[2]/span[2]/b"%(i)
        p=data.xpath(a)  
        r = p[0].text
        #print r 
        output1.write('title : '+r+'\n')
        
        
        
        a="//*[@id='productReviews']//tr[1]/td[1]/div[%d]/div[2]/span[2]/nobr"%(i)
        p=data.xpath(a) 
        r= p[0].text       #date 
        output1.write('Date: '+r+'\n')
        
        
        
        a= "substring-before(//*[@id='productReviews']//tr[1]/td[1]/div[%d]/div[2]/span[1]/span,'out')"%(i)
        #print a
        #i=substring-before(a,"out")
        p=data.xpath(a)
        #print p               #review rating
        r=p
        output1.write('review rating out of 5.0: '+r+'\n')
        
        
        
        
        a="//*[@id='productReviews']//tr[1]/td[1]/div[%d]/text()"%(i)
        p=data.xpath(a)
        k="".join(p)
        #print r
        r=k.lstrip()               #to remove white spaces initially in text
        #print r
        output1.write('Rieview :'+r+'\n') 
                             #review contents
        output1.flush()
    





 
 
for url in urls :
       crawl(url)



output1.close() 
       





