import re
import urllib
MGIName = 'Panasonic 50" ST60'
text = urllib.urlopen("https://www.decide.com/search?q="+ MGIName ).read()

from bs4 import BeautifulSoup as BS
j=0
soup = BS(text)
#print soup
#titleTag =soup.html.body.section[2].div.section.section[2].div.ol.li[1].div[1].a[1]
#titleTag = soup.html.head.title

#titleTag=soup.html.body.section.div.section.section.div.ol.li.div.a
#print titleTag 
t=soup.findAll('a',attrs={'class':'background'})
url=[]
for r in t :
    #print str(r)
    x=str(r).split('"')
    url.append('https://www.decide.com'+x[3])
    
f=open('/home/aknauhwar/Desktop/reviews_decide' , "w")
    
#print a ;


for urls in url :
    print urls
    text=urllib.urlopen(urls).read()
    soup=BS(text)
    t=soup.findAll('span',attrs={'itemprop':'description'})
    reviews=[]
    f.write(urls+'\n')
    for i in t :
        #print i
        x=str(i).split('>')
        y=x[1].split('</span')
        #print y[0]
        
        reviews.append(y[0])
        f.write(y[0]+'\n\n\n\n\n\n')
        j=j+1
        print j
    
    
    m=soup.findAll('li' , attrs={'class':'page'})
    newurls=[]
    for r in m :
        #print str(r)
        x=str(r).split('"')
        #print x[5]
        newurls.append('https://www.decide.com'+x[5])
        
    
    for urls in newurls :
            text=urllib.urlopen(urls).read()
            soup=BS(text)
            t=soup.findAll('span',attrs={'itemprop':'description'})
            reviews=[]
            f.write(urls+'\n')
            for i in t :
                #print i
                x=str(i).split('>')
                y=x[1].split('</span')
                #print y[0]
                
                reviews.append(y[0])
                f.write(y[0]+'\n\n\n\n\n\n')
                j=j+1
                print j 
    
    
    

#print reviews
    
f.close()



    