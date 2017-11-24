import lxml
from lxml import etree
import urllib2
import urllib
import lxml.html as lh
from bs4 import BeautifulSoup as BS
import requests
import json
import simplejson
import mechanize


def find_brand_mfn(doc2):
        list=[]
        soup = BS(doc2)
        #t=soup.findAll('table')
        t=soup.findAll('div' ,attrs={'id':'vi-desc-maincntr'})
        try :
            m=str(t[0]) 
        except :
            print "No item_specifications found "
            return list
            
        a=m.split('itemprop="name">')
           
        try :
            b=a[1]
            if a[1] :                     
                c=b.split('<')
                if c :
                    d=c[0]
        except :
            d="" 
                
        a1=m.split('itemprop="mpn">')
                        
        try :               
            b1=a1[1]
            if a1[1] :
                 c1=b1.split('<')
                 if c1 :
                    d1=c1[0]
                                            
        except :
            d1=""
        #if brand is not present at times we have part brand 
        a2=m.split('Part Brand:')
        d3=""
        try :
            #pass
            b2=a2[1]
            b3=b2.split('</h')
            c3=b3[0].split('>')
            d3=c3[-1]
            print d3
        except :
            pass
        
            
        if d :
            list.extend([d])
        if d1 :
            list.extend([d1])
        if d3 :
            list.extend([d3])
        print list
        return list
            

def main():
    f=open('/home/aknauhwar/Desktop/ebay testing/ebay_match/test.txt' , "w")  

    #keyword ="Timken SP580310"
    #keyword ="Genuine%20W0133-1853114"
    #keyword="Airtex%20E3500M"
    #keyword="Timken%20HA590046"
    #keyword="Action%20Crash%20FO1320233"
    #keyword="Rancho%20RS999910"
    #keyword="LUK%2007-175"  #look its result again .
    #keyword="GMB%20W0133-1615866"
    keyword="Dorman%20973-019"
    
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
    url += "&paginationInput.entriesPerPage=20" 
    print url
    
    #r = requests.get(url1)
    #data = r.json()
    '''response = urllib.urlopen(url1);
    data = json.load(response)  #loads will return string for json use load'''

    #print data
    #print data["findItemsByKeywordsResponse"]
    #request = urllib2.Request(url1)
    #response = json.load(urllib2.urlopen(request))
    
    try :
        data = json.load(urllib2.urlopen(url)) #data is dict datatype 
        response =json.dumps(data,indent=2)    # response is string
    
    except :
        print "can\'t load the json object "
        #in main program skip to next entry from the file
    
    #print json.dumps(data,indent=2)
    #print type(data)
    #print type(response)
    try :
        f.write(response)
        oo=data
        
    except :
        print " was unable to get data and reponse "
        #in main program no need for this beacause if page is unable to load or bad json it wouldnt be reaching here it will be out of loop already
    
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
            check=[]
            url="http://www.ebay.com/itm/"+str(k)
            #url=""
            #doc = lh.parse(url)
            doc2 = urllib.urlopen(url).read()
            print url 
            check=find_brand_mfn(doc2)
                  
    f.close()        
   
main()
    
    
    
    
    
    
    