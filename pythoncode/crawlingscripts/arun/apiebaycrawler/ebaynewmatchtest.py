'''import urllib2
import json

url="http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=arunkuma-47b1-467b-a87e-0528caad791f&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&outputSelector%280%29=SellerInfo&outputSelector%281%29=StoreInfo&keywords=Timken SP580310"

req = urllib2.Request(url)
opener = urllib2.build_opener()
f = opener.open(req)
json = json.loads(f.read())
print json
#print json[0]['title']'''

import json
import urllib
import urllib2


url="http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=arunkuma-47b1-467b-a87e-0528caad791f&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&outputSelector%280%29=SellerInfo&outputSelector%281%29=StoreInfo&keywords=Timken SP580310"

#j = urllib2.urlopen(url)
j=urllib.quote(url)
response = json.load(urllib2.urlopen(j))
js = json.loads(j)
ourResult = js['findItemsByKeywordsResponse'][3]['searchResult']
for rs in ourResult:
    print rs['itemId']
