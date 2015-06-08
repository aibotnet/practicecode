import lxml
from lxml import etree
import urllib2
import lxml.html as lh
#f=open('/home/aknauhwar/Desktop/ebay testing/ebaytext.txt' , "w")

#doc = lh.parse("http://www.ebay.com/itm/2004-2011-Mazda-RX-8-Sun-Visor-Left-Driver-Side-GENUINE-OEM-/200711646671")

doc = lh.parse("http://www.ebay.com/itm/57127-REMAN-AC-A-C-Compressor-89-96-FORD-MERCURY-THUNDERBIRD-MUSTANG-3-8-A-C/271338992729?_trksid=p2047675.m1985&_trkparms=aid%3D444000%26algo%3DSOI.CURRENT%26ao%3D1%26asc%3D13%26meid%3D3851370793090800688%26pid%3D100012%26prg%3D1014%26rk%3D1%26rkt%3D5%26sd%3D271362049663%26#vi-ilComp")
#text = doc.xpath('.//*[id("result_0")]/h3/a/span/text()')
k=0


#text = doc.xpath('//*[id("w1-23ctbl")]/tbody/tr/td/text()')
#text = doc.xpath('//*[id("vi-ret-accrd-txt")]/text()')

#text = doc.xpath('//*[id("w1-27ctbl")]/tbody/tr/td/text()')
#text= doc.xpath('//*[id("ICN0")]')
#text = doc.xpath('//*[id("vi-ilComp")]/div/h3/text()')

text = doc.xpath('//*[id("w1-8ctbl")]/tbody/tr/td')


print type(text)
#print text
print len(text)
for i in text :
        #f.write(i)
        print i

#f.close

    