import lxml
from lxml import etree
import urllib2
import lxml.html as lh
from bs4 import BeautifulSoup as BS
import requests
import json
import simplejson


def main():
    keyword ="Timken SP580310"
    #url="http://www.ebay.com/itm/"+item_id
    url1="http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=arunkuma-47b1-467b-a87e-0528caad791f&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&outputSelector%280%29=SellerInfo&outputSelector%281%29=StoreInfo&keywords="+keyword
    print url1
    #r = requests.get(url1)
    #data = r.json()
    '''response = urllib.urlopen(url1);
    data = json.load(response)  #loads will return string for json use load'''

    #print data
    #print data["findItemsByKeywordsResponse"]
    #request = urllib2.Request(url1)
 
    #response = json.load(urllib2.urlopen(request))
    data = json.load(urllib2.urlopen(url1))
    print json.dumps(response,indent=2)
    
main()
    
    
    
    