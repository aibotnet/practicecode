import lxml
from lxml import etree
import urllib2
import lxml.html as lh
import urllib
from bs4 import BeautifulSoup as BS
import requests
import json
import simplejson
import mechanize
import random

def gen_random_decimal(i,d):
    return decimal.Decimal('%d.%d' % (random.randint(0,i),random.randint(0,d)))

i=str(gen_random_decimal(0,9999999999999999))
j=str(gen_random_decimal(0,9999999999999999))
#print i
#print j

a=[1,2,3,4222,5,6,78,9]

for i in a[0:4] :
    print i 

'''url="http://www.ebay.com/itm/380804806738"
doc = lh.parse(url)
#text=doc.xpath('//*[id("vi-desc-maincntr")]/div/div/table/tbody/tr/td/text()')
doc2 = urllib.urlopen(url).read()
soup = BS(doc2)
#t=soup.findAll('table')
t=soup.findAll('div' ,attrs={'id':'vi-desc-maincntr'})
m=str(t[0])

#print m
a=m.split('itemprop="name">')
#print a[1]
b=a[1]
c=b.split('<')
#print type(c)
d=c[0]

print d

a1=m.split('itemprop="mpn">')
b1=a1[1]
c1=b1.split('<')
d1=c1[0]
print d1


j=0 '''

        