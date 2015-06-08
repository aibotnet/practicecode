import lxml
from lxml import etree
import urllib2
import lxml.html as lh
from bs4 import BeautifulSoup as BS
import requests
import json
import simplejson
import urllib


'''url="http://svcs.ebay.com/services/search/FindingService/v1?OPERATION-NAME=findItemsByKeywords&SERVICE-VERSION=1.0.0&SECURITY-APPNAME=arunkuma-47b1-467b-a87e-0528caad791f&RESPONSE-DATA-FORMAT=JSON&REST-PAYLOAD&outputSelector%280%29=SellerInfo&outputSelector%281%29=StoreInfo&keywords=Timken SP580310"

response = urllib.urlopen(url);
print type(response)
data = json.loads(response.read())
#print data
#print  type(data)
print type(data)
ourResult = data['findItemsByKeywordsResponse'][0]['searchResult'][0]['item']
#print ourResult
for rs in ourResult:
    print rs['itemId'][0]'''
    
#import nltk

import nltk
#from nltk import word_tokenize
print "1"
sentence = """At eight o'clock on Thursday morning Arthur didn't feel very good."""
tokens = nltk.word_tokenize(sentence)

print tokens
tagged = nltk.pos_tag(tokens)
print tagged[0:6]
