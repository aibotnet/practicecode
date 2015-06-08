import lxml
from lxml import etree
import re
import lxml
import urllib
MGIName = 'HP Officejet Pro  8600'
text = urllib.urlopen("http://www.ebay.com/itm/2004-2011-Mazda-RX-8-Sun-Visor-Left-Driver-Side-GENUINE-OEM-/261366532009").read()
f=open('/home/aknauhwar/Desktop/ebay testing/ebaytext.txt' , "w")
from bs4 import BeautifulSoup as BS
j=0
soup = BS(text)
#print soup

#print type(soup)

#print text

f.write(text)

f.close
    
