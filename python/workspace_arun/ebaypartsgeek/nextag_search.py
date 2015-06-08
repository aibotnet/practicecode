import lxml
from lxml import etree
import urllib
import lxml.html as lh
#from bs4 import BeautifulSoup as BS
#import mechanize


def Find_Count(url , output , error):
    print url
    try :
        doc = lh.parse(url)
        print "url working"
        
    except:
        print "page unable to load ::::::::::: " +url+ "\n "
        error.write("url not working or unable to open :: "+url+"\n")
        
        
    try :
        total=doc.xpath('//*[@id="breadcrumbs-container"]/span/text()')
        
        print total[0]
        output.write(url+"|"+total[0]+"\n")
        
    except :
        print "wrong xpath"
        error.write("unable to fetch count from url maybe no search result :: "+url+"\n")
        
    output.flush()
    error.flush()


def main(): 
    
    input=open('/home/aknauhwar/Desktop/dog_beds.txt' , "r")
    output=open('/home/aknauhwar/Desktop/dog_beds_search_count1.txt' , "w")
    error=open('/home/aknauhwar/Desktop/dog_beds_error_log1.txt' , "w")
    urls=input.readlines()
    
    print urls
    for i in urls :
        
        url=i.rstrip()
        Find_Count(url , output , error)
        
        
    input.close()
    output.close()
    error.close()   
        
main()
        
    