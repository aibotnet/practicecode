'''
Created on 05-Dec-2013

@author: aknauhwar
'''

import lxml
from lxml import etree
import urllib2
import lxml.html as lh
#from bs4 import BeautifulSoup as BS




#parse the page for various 


def Find_pid( doc) :
    
    text=doc.xpath('//*[id("w1-8epid")]/div[1]/text()')
    
    for i in text : 
        if "eBay Product ID: EPID" in i :
            id = i.split("EPID")
            p_eid=id[1]
            break
        
        
    return p_eid

def Find_cid(doc) :
    
    text=doc.xpath('//div/div/a[text()="Print"]/@href')

    
    for i in text : 
        if "category=" in i :
            id = i.split("category=")
            c_id=id[1]
            break
        
        
    return c_id

def main():
    item_id ="271362049663"
        
    url="http://www.ebay.com/itm/"+item_id
    #url_req2 = "http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.3967430352423186&site=100&req=2&cid="+cid+"&item="+item_id+"&ct=20&pn=&page="+current_page+"&cb=jQuery"
    #url_req1 = "http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.3635987357117708&site=100&req=1&cid="+cid+"&pid="+pid+"&item="+item_id+"&ct=20&page="+current_page+"&cb=jQuery"   
    
    doc = lh.parse(url)   
    cid = Find_cid(doc)
    pid=  Find_pid(doc)
    
    #find page count
    url2 = "http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.3967430352423186&site=100&req=2&cid="+cid+"&item="+item_id+"&ct=20&pn=&page=1&cb=jQuery"
    url1 = "http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.3635987357117708&site=100&req=1&cid="+cid+"&pid="+pid+"&item="+item_id+"&ct=20&page=1&cb=jQuery"   
    
    print cid 
    print pid
    print url1
    print url2
    
    
    
    
    
    
    
    




 
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    



