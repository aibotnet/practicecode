import lxml
from lxml import etree
import urllib2
import lxml.html as lh
from bs4 import BeautifulSoup as BS

k=0
#f=open('/home/aknauhwar/Desktop/ebay testing/ebaytext.txt' , "w")

doc = lh.parse("http://www.ebay.com/itm/Front-Rear-Kit-POWERSPORT-DRILLED-SLOTTED-Brake-Rotors-CERAMIC-Pads-BL10937-/190727030653?pt=Motors_Car_Truck_Parts_Accessories&hash=item5ae90a348a&vxp=mtr")

text = doc.xpath('//*[id("seeCompLnk")]/text()')

#print type(text)
#print text
#print len(text)

if "See compatible vehicles" in text :
    print "yes"
    k=1
else :
    print "bad request"
    #getProductDetails
    
if k==1 :
    doc1=  lh.parse("http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.5956277663330161&site=100&req=2&cid=33564&item=390456816778&ct=20&pn=&page=1&cb=jQuery")
    
    print doc1
    text2=doc1.xpath('/body')
    
    print len(text2)
    for i in text2 :
        #f.write(i)
        print i
        
        
    doc2 = urllib.urlopen("http://frame.ebay.com/ebaymotors/ws/eBayISAPI.dll?GetFitmentData&rand=0.5956277663330161&site=100&req=2&cid=33564&item=190727030653&ct=20&pn=&page=1&cb=jQuery").read()
    
    soup = BS(doc2)
    
    t=soup.findAll('body')


    for r in t :
    
    #     print 
        #print('\n\n\n\n')
        #f.write(str(r)+'\n\n\n\n\n')
        print r
#f.close

    