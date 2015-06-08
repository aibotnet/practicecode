import lxml
from lxml import etree
import urllib2
import lxml.html as lh

doc = lh.parse("http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords=HP%20Officejet%20Pro%20%208600")
#text = doc.xpath('.//*[id("result_0")]/h3/a/span/text()')
k=0


text = doc.xpath('//div/h3/a/@href')
print len(text)
for i in text :
    doc = lh.parse(i)
    text1 = doc.xpath('//*[@id="seeAllReviewsUrl"]/@href')
    for j in text1 :
        print j
        doc = lh.parse(j)
        k=k+1
        print k 
    
    
