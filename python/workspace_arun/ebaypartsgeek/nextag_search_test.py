import lxml
from lxml import etree
import urllib
import lxml.html as lh

def main():

    url="http://www.nextag.com/serv/main/buyer/OutPDir.jsp?node=2702007&page=0&wsearch=Kenel&la=1&ls=3"
    #url="http://www.nextag.com/serv/main/buyer/OutPDir.jsp?node=2702007&page=0&wsearch=Double Donut&la=1&ls=3"
    
    try :
            doc = lh.parse(url)
            
            print "url working"
            
    except:
            print "page unable to load ::::::::::: " +url+ "\n "
            
                    
    try :
                    #total=doc.xpath('//*[@id="breadcrumbs-container"]/span/text()')
                    #total=doc.xpath('//div/div/div/div[@id="breadcrumbs-container"]/span/text()')
                    #total=doc.xpath('//div/div/div/div/span/text()')
                    #total=doc.xpath("//div/div/a/text()")
                    
                    print total
                    
    except : 
        pass
                    
                    
main()