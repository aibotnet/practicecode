import lxml
from lxml import etree
import urllib
import lxml.html as lh
#from bs4 import BeautifulSoup as BS
#import mechanize


def Find_Count(url , output ):
    print url
    try :
        doc = lh.parse(url)
        print "url working"
        
    except:
        print "page unable to load ::::::::::: " +url+ "\n "
        output.write(url+"|"+"0"+"|"+"url not working or unable to open" + "\n")
        
                
    try :
                total=doc.xpath('//*[@id="breadcrumbs-container"]/span/text()')
                #total=doc.xpath('//div/div/div/div[@id="breadcrumbs-container"]/span/text()')
                #total=doc.xpath('//div/div/div/div/span/text()')
                
                print total
                output.write(url+"|"+total[0]+"\n")
                
    except :
                print "wrong xpath"
                output.write(url+"|"+"0"+"|"+"unable to fetch count from url maybe no search result" +"\n")
        
    output.flush()
    #error.flush()


def main(): 
    
    input=open('/home/aknauhwar/Desktop/dog_beds.txt' , "r")
    output=open('/home/aknauhwar/Desktop/dog_beds_search_count.txt' , "w")
    #error=open('/home/aknauhwar/Desktop/dog_beds_error_log.txt' , "w")
    urls=input.readlines()
    
    for i in urls :
        
        url=i.rstrip()
        Find_Count(url , output )
        
        
    input.close()
    output.close()
 
        
main()
        
    