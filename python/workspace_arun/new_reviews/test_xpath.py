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


url="http://www.amazon.com/product-reviews/B00DM8R866"

#url="http://www.amazon.com/Sony-DSC-RX100M-Cyber-shot-Digital-Camera/product-reviews/B00DM8R866/ref=cm_cr_pr_btm_link_13?ie=UTF8&pageNumber=13&showViewpoints=0&sortBy=byRankDescending"
#url="http://www.buzzillions.com/reviews/panasonic-dmr-eh59ga-k-multi-zone-250gb-hdd-dvd-recorder-reviews"
doc = lh.parse(url)

#text=doc.xpath('//span[@class="paging"]/a[text()[contains(.,"Next ")]]/@href')  # matching some part

#text=doc.xpath('//span[@class="paging"]/a[.="2"]/@href')   # matching exact text

#text=doc.xpath('//div[@class="hReview bz-model-review"]//div[@class="bz-model-review-date-inner"]/span[@class="month"]/text()  | //div[@class="hReview bz-model-review"]//div[@class="bz-model-review-date-inner"]/span[@class="day"]/text() ')

#text= doc.xpath('//div[@id="bz-model-review-16733929"]//div[@class="bz-model-review-date-inner"]//descendant::*/text()')

#text= doc.xpath('//*[ preceding-sibling::div[@class="bz-model-review-comments-container"]  and following-sibling::div[@class="bz-clearfix"] ]/text()')

text=doc.xpath('//div[@class="reviewText"]/text()')




#text[1]
print text[1]