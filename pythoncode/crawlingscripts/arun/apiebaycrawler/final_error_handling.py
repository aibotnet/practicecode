'''
Created on 05-Dec-2013

@author: aknauhwar
'''

import lxml
from lxml import etree
import urllib
import lxml.html as lh
from bs4 import BeautifulSoup as BS




#parse the page for various 


def Find_pid( doc) :
    
    #text=doc.xpath('//*[id("w1-8epid")]/div[1]/text()')
    text=doc.xpath('//div/div/div/div/div/div/div/div/div/text()')
    p_eid = -1
    for i in text : 
        #print i
        if "eBay Product ID: EPID" in i :
            id = i.split("EPID")
            p_eid=id[1]
            break
        
        
    return p_eid

def Find_cid(doc) :
    # not worthy
    text=doc.xpath('//div/div/a[text()="Print"]/@href')
    c_id= -1
    for i in text : 
        print i
        if "category=" in i :
            id = i.split("category=")
            c_id=id[1]
            break
        
 
    return c_id


def Pagecount(doc1 , doc2):

    #get jsonpage and fing pagecount
    soup = BS(doc2)
    t=soup.findAll('body')
    m=str(t[0])
    k=m.split('"pageInfo":')
    if "null" in k[1] :
        soup3=BS(doc1)
        
        j=soup3.findAll('body')
        
        n=str(j[0])
        l=n.split('"totalPageCount":')
        #print l[0]
        r=l[1]
        s=r.split(',"pageRecordCount"')
        id =int(s[0])+100000
    else :
        id1=m.split('"totalPageCount":')
        id2=id1[1]
        id3=id2.split(',"pageRecordCount"')
        print
        id=int(id3[0])
        
    return id   
    

def Compabilitylist(doc):
    text = doc.xpath('//*[id("seeCompLnk")]/text()')
    if "See compatible vehicles" in text :
        return 1
    else :
        return  0 
    

def APIreq2call(item_id , page_count , f): 
    i=1
    while i <= page_count :
        
        call_url= "http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.3967430352423186&site=100&req=2&cid=33567&item="+item_id+"&ct=20&pn=&page=%d&cb=jQuery"%i
        doc4 = urllib.urlopen(call_url).read()
        soup = BS(doc4)
        t=soup.findAll('body')
        m=str(t[0])
        print m 
        
        f.write("\n\n\n\n")
        f.write("%d"%i+chr(10)+ m )
        i=i+1
    print "api2 is the gospel truth right now"
    f.write("\n\n\n\n"+"api2 is the gospel truth right now")
    
def APIreq1call(item_id , page_count , pid , f): 
    i=1
    while i <= page_count :
        
        call_url="http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.3635987357117708&site=100&req=1&cid=33567&pid="+pid+"&item="+item_id+"&ct=20&page=%d&cb=jQuery"%i
        doc5 = urllib.urlopen(call_url).read()
        soup = BS(doc5)
        t=soup.findAll('body')
        m=str(t[0])
        print m 
        
        f.write("\n\n\n\n")
        f.write("%d"%i+"\n" +chr(10)+ m )
        i=i+1
    print "api1 is the gospel truth right now"
    f.write("\n\n\n\n"+"api1 is the gospel truth right now")
                              


def main():

    item_id ="110900855342"
    url="http://www.ebay.com/itm/"+item_id
    f=open('/home/aknauhwar/Desktop/ebay testing/ebaytext.txt' , "w")
    input=open('/home/aknauhwar/Desktop/ebay testing/eBaySample-5000-Parts.txt' , "r")
    doc = lh.parse(url)   
    cid = "33567"
    pid=  str(Find_pid(doc))
    url2 = "http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.3967430352423186&site=100&req=2&cid="+cid+"&item="+item_id+"&ct=20&pn=&page=1&cb=jQuery"
    url1 = "http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.3635987357117708&site=100&req=1&cid="+cid+"&pid="+pid+"&item="+item_id+"&ct=20&page=1&cb=jQuery"   
    doc2 = urllib.urlopen(url2).read()
    doc1 = urllib.urlopen(url1).read()
    
    page_count=Pagecount(doc1 , doc2)
    
    
    if (page_count > 10000 ) :
        page_count=page_count-100000
        api_request_number= 1
        
    else :
        api_request_number= 2
    
    #check if compability list is present or not 
    check_list=Compabilitylist(doc)
    
    if check_list :
        
        if(api_request_number==2) :          
            APIreq2call(item_id , page_count , f)
            
            
        
        elif (api_request_number==1) :
            APIreq1call(item_id , page_count , pid , f)
            
        else :
            print "need to review "
            
            
            
        
        
        
    else :
        #write in a file 
        print "do some manual work"
    
    f.close()
         
    
main()
    
    
    
    
    
    
    
    




 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



