import re
import lxml
import urllib
MGIName = 'HP Officejet Pro  8600'
text = urllib.urlopen("http://www.amazon.com/s/ref=nb_sb_noss_1?url=search-alias%3Daps&field-keywords="+ MGIName ).read()
f=open('/home/aknauhwar/Desktop/amazon_testingxzxzxx' , "w")
from bs4 import BeautifulSoup as BS
j=0
soup = BS(text)
#print soup

#t=soup.findAll('div', attrs={'class' : 'image-imageContainer'})
#print soup.html.body.div.div.div.div.div.div.div.h3.a.span
#print t
t=soup.findAll('a' , href=True)


for r in t :

#     print 
    print('\n\n\n\n')
    f.write(str(r)+'\n\n\n\n\n')
    
  
    
    
f.close() 