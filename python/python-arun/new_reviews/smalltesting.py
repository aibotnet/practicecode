import lxml
from lxml import etree
import urllib2
import lxml.html as lh
from bs4 import BeautifulSoup as BS

item_id="111233588699"
url="http://www.ebay.com/itm/"+item_id

doc = lh.parse(url)


text=doc.xpath('//div/div/a[text()="Print"]/@href')

print text
for i in text :
    print i
    if "category=" in i :
            id = i.split("category=")
            c_id=id[1]
            print type(c_id)
            k= int(c_id)
            print  c_id
            
            print k
            print type(k)
            break