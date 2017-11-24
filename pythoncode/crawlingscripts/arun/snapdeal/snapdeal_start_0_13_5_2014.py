
from bs4 import BeautifulSoup
import urllib2

url='http://www.snapdeal.com/products/mobiles-mobile-phones/?q=Brand:Nokia'
data = urllib2.urlopen(url).read()

page = BeautifulSoup(data,'html.parser')
count=0
for link in page.findAll('a'):
       l = link.get('href')
       count +=1
       print l

print count