import urllib2
from StringIO import StringIO
from lxml.cssselect import CSSSelector
from lxml import etree
import lxml.html
MGIName = 'HP Officejet Pro  8600'
url =  "http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords="+ MGIName
response = urllib2.urlopen(url)
data=response.read()

htmlparser = etree.HTMLParser()

doc1 = lxml.html.document_fromstring (data )

x=doc1.xpath('id("result_0")/h3/a/span/text()')

print x

tree = etree.parse(data, htmlparser)

output = open('/home/aknauhwar/Desktop/amazonxml.txt' , "w")

     
#r=f.xpath('//product_id/text()') #r contains all the selated data as list i think or tuple so using for loop we printed that data
r=tree.xpath('id("result_0")/h3/a/span/text()')
print str(r)
for pid in r :
    print pid
    output.write(pid +"\n\n\n\n\n")
     
    
    
output.close()
