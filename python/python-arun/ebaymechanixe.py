import lxml
from lxml import etree
import urllib
import lxml.html as lh
from bs4 import BeautifulSoup as BS
import json
import simplejson
import ast




call_url="http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.3967430352423186&site=100&RESPONSE-DATA-FORMAT=XML&req=2&cid=33567&item=360830071518&ct=20&pn=&page=1&cb=jQuery"

'''doc = urllib.urlopen(call_url)
doc4=doc.read()
soup = BS(doc4)
t=soup.findAll('body')

m=str(t[0])
print doc.headers['content-type']
#print urllib.quote(m)
print m'''

import mechanize
b = mechanize.Browser()

# Set any header you like:
b.addheaders = [('Content-Type', 'text; charset=utf-8')]
response = b.open(call_url)
data = response.read()
#print data

lin = data.strip('jQuery(')
line=lin.strip(');')

#print line 
oo = json.loads(line)
#print type(oo)

daata= oo['data']
for rs in daata :
            if 'FitmentComments' not in rs.keys() :
                FitmentComments=""
            else :
                FitmentComments=rs['FitmentComments'][0]
                print FitmentComments
            if 'Model' not in rs.keys() :
                Model=""
            else :
                Model=rs['Model'][0]
                print Model
            if 'Year' not in rs.keys() :
                Year=""
            else :
                Year=rs['Year'][0]  
                print Year
            if 'Make' not in rs.keys() :
                Make=""
            else :
                Make=rs['Make'][0]
                print Make
            if 'Trim' not in rs.keys() :
                Trim="ALL"
            else :
                Trim=rs['Trim'][0]
                print Trim
            if 'Engine' not in rs.keys() :
                Engine="ALL"
            else :
                Engine=rs['Engine'][0] 
                print Engine
                
                























