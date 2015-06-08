import lxml
from lxml import etree
import urllib2
import lxml.html as lh
from bs4 import BeautifulSoup as BS
import requests
import json
import simplejson
import mechanize


def find_brand_mfn(doc):
    















def main():
    f=open('/home/aknauhwar/Desktop/ebay testing/ebay_match/test.txt' , "w")  

    #keyword ="Timken SP580310"
    #keyword ="Genuine%20W0133-1853114"
    keyword="Airtex%20E3500M"
    
    #url="http://www.ebay.com/itm/"+item_id
    #url1="http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=arunkuma-47b1-467b-a87e-0528caad791f&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&outputSelector%280%29=SellerInfo&outputSelector%281%29=StoreInfo&keywords="+keyword
    url = "http://svcs.ebay.com/services/search/FindingService/v1"
    url += "?OPERATION-NAME=findItemsByKeywords"
    url += "&SERVICE-VERSION=1.0.0"
    url += "&SECURITY-APPNAME=arunkuma-47b1-467b-a87e-0528caad791f"
    url += "&GLOBAL-ID=EBAY-US"
    url += "&RESPONSE-DATA-FORMAT=JSON"
    #url += "&callback=_cb_findItemsByKeywords"
    url += "&REST-PAYLOAD"
    url += "&categoryId=100" #// video game  
    url += "&keywords=%s"%keyword            #Timken%20SP580310// change value to game title 
    url += "&paginationInput.entriesPerPage=100" 
    print url
    #r = requests.get(url1)
    #data = r.json()
    '''response = urllib.urlopen(url1);
    data = json.load(response)  #loads will return string for json use load'''

    #print data
    #print data["findItemsByKeywordsResponse"]
    #request = urllib2.Request(url1)
 
    #response = json.load(urllib2.urlopen(request))
    data = json.load(urllib2.urlopen(url))
    response =json.dumps(data,indent=2)
    #print json.dumps(data,indent=2)
    print type(data)
    print type(response)
    f.write(response)
    oo=data
    
    daata=oo["findItemsByKeywordsResponse"]
    #print type(daata)
    ooo= daata[0]
    #print type(ooo)
    #print ooo
    daaata=ooo["paginationOutput"]
    a=daaata[0]["totalEntries"][0]
    #print int(a)
    count=0
    if int(a)==0 :
        
        print "product not found in the search result "
        
    else :
        if int(a)>5 :
            count=5
        else :
            count=int(a)
    
    print count
    url_list=[]
    if count :
        j=0
        while j<count :
            b=oo["findItemsByKeywordsResponse"][0]["searchResult"][0]["item"][j]["itemId"]
            #print type(b[0])
            
                
            url_list.extend([int(b[0])])
            j=j+1
            
    
    #print url_list[3]
    #print type(url_list[3])
    
    if url_list :
        for k in url_list :
            
            url="http://www.ebay.com/itm/"+k
            doc = lh.parse(url)
            
            
            
    
    
    
    
    
    
    
    
    
    
    
    
main()
    
    
    
    