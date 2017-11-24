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
import re
import lxml.etree as ET
from lxml.etree import tostring
from lxml.cssselect import CSSSelector
#print lh.tostring(doc)   to print the html content

url="http://www.amazon.com/product-reviews/1591846013"

#url='http://www.snapdeal.com/products/mobiles-mobile-phones/?q=Brand:Nokia'
#url='http://www.snapdeal.com/products/lifestyle-watches?sort=plrty&start=15'

#url='http://www.snapdeal.com/products/e-learning?sort=plrty&'
#url="http://www.amazon.com/product-reviews/B005OCZN2O"
#url="http://www.newegg.com/Product/Product.aspx?Item=N82E16830120615"
#url="http://www.newegg.com/Product/Product.aspx?Item=N82E16830120615"
#url='http://www.amazon.com/Canon-PowerShot-A2500-Stabilized-2-7-Inch/dp/B00B5HE2UG/'
#url='http://www.rakuten.com/sr/searchresults.aspx?qu=NIKON+D3200+CAMERA'
doc = lh.parse(url)

#xml=tostring(doc, pretty_print=True , encoding='html').strip()

#next_page_url=doc.xpath('//div/span[@class="paging"]/a[text()[contains(.,"Next ")]]/@href')  # matching some part
next_page_url=doc.xpath('//div/span[@class="paging"]/a[.="2"]/@href')
#next_page_url=doc.xpath('.//a[starts-with(text(), "Next")')

author=doc.xpath('.//a[contains(@href, "/profile/")]/span/text()')
date=doc.xpath('//div[@style="margin-bottom:0.5em;"]//nobr/text()')
rating=doc.xpath('.//span[contains(text(), \"out of 5 stars\")]/text()')
summary=doc.xpath('//div[@style="margin-bottom:0.5em;"]/span/b[not(@class)]/text()')

external_id=doc.xpath('.//a[contains(@href, \"/profile/\")]/@href'[0])
title= doc.xpath('//div[@id="title_feature_div"]//span[@id="productTitle"]/text()')
title2=doc.xpath('//div[@class="a-container"]/div[@data-feature-name="title"]//span/text()')
#print lh.tostring(doc)


testios=doc.xpath('.//a[contains(@href, "/profile/")]/span/text()')


#reviews=doc.xpath('.//table[@id="productReviews"]/tr/td[1]/div/div[@class="reviewText"]/descendant-or-self::*[not(ancestor-or-self::script or ancestor-or-self::noscript or ancestor-or-self::style)]/text()')
#reviews=doc.xpath('.//table[@id=\"productReviews\"]//div[@class=\"reviewText\"]/string()')


#print lh(url)
#text=doc.xpath('//span[@class="paging"]/a[.="2"]/@href')   # matching exact text

#text=doc.xpath('//div[@class="hReview bz-model-review"]//div[@class="bz-model-review-date-inner"]/span[@class="month"]/text()  | //div[@class="hReview bz-model-review"]//div[@class="bz-model-review-date-inner"]/span[@class="day"]/text() ')

#text= doc.xpath('//div[@id="bz-model-review-16733929"]//div[@class="bz-model-review-date-inner"]//descendant::*/text()')

#text= doc.xpath('//*[ preceding-sibling::div[@class="bz-model-review-comments-container"]  and following-sibling::div[@class="bz-clearfix"] ]/text()')

#text=doc.xpath('//div[@id="bz-model-review-20258630"]//text()')


#print lh.tostring(doc)

#input = open('/home/aknauhwar/Desktop/amazon_title_test.txt' , "w")

#input.write(lh.tostring(doc))

#title3=doc.xpath('//div[@class="wrapper"]/h1/span[not(@style)]/text()')

#title=doc.xpath('//span[@id="btAsinTitle"]/text()')

reviews_expr1=doc.xpath('.//table[@id="productReviews"]/tr/td[1]/div/div[@class="reviewText"]/text()')

reviews_expr=doc.xpath('.//table[@id=\"productReviews\"]/tr/td[1]/*[.//nobr/text()]/text()')


testo =doc.xpath('//div[@id="detail-bullets"]//li//text()')
testo1=doc.xpath('//div[@id="detail-bullets"]//li/b[text()[contains(.,"     Product Dimensions:      ")]]/text()')
#testo2=doc.xpath('substring-after(//div[@id="detail-bullets"]//li/following-sibling::text()[1]," inche ")')
'''print testo


    
    
indices = [i for i, s in enumerate(testo) if 'Product Dimensions:' in s]

print testo[indices[0]+1]'''


#cssselect  div~ div+ div div div > a span[style*="font-weight: bold;"]
example=doc.xpath('//div//div//div//div//a//span[style="font-weight: bold;"]/text()')


test=doc.xpath('.//div[@class=\"reviewText\"]/text()')
test=doc.xpath('.//table[@id="productReviews"]/tr/td[1][.//nobr/text()]/*')


test=doc.xpath('.//table[@id="productReviews"]/tr/td[1]/*[.//nobr/text()]')

test=doc.xpath('.//table[@id="productReviews"]/tr/td[1][.//nobr/text()]/*')
test=doc.xpath('.//table[@id=\"productReviews\"]/tr/td[1]/div/div[@class=\"reviewText\" ]')


snap=doc.xpath('//div[@class="pageWrapper"]//noscript/div/a[@class="next"]/@href')

#snap=doc.xpath('//div[@id="products-main4"]//div[@class="product-title"]/a/@href')


print snap

print len(snap)

for i in snap :
    print i
    
    
    


''''k=0
for i in reviews_expr :
    k +=1
    print k
    print i
    print "\n"*10  '''




'''import urllib2
response = urllib2.urlopen(url)
html1 = response.read()

print html1 '''


