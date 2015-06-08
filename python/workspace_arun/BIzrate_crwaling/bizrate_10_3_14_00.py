import lxml
from lxml import etree
import urllib
import lxml.html as lh
from bs4 import BeautifulSoup as BS
import mechanize
#import json
#import simplejson
#import ast
#import random 
#import decimal
#import time


def Find_Departments():
                        url="http://www.bizrate.com/ratings_guide/guide/"
                        print "123"
                        try :
                            doc = lh.parse(url)
                        
                        except:
                            print "page unable to load ::::::::::: http://www.bizrate.com/ratings_guide/guide/  \n "
                            
                        try :
                            #text=doc.xpath('//*[id("search_header")]/table/tbody/tr/td/div/div/ul/li/a/text()')
                            text=doc.xpath('//li/a/text()')                            
                            #print text
                            return text
                            
                        except :
                            
                            print "NO department inforation check for the xpath \n"
                            
def Browse_Category(category):
    
    url="http://www.bizrate.com/"+category+"/ratings_guide/listing/"
    
    try :
        doc = lh.parse(url)
        print "url working"
    except:
        print "page unable to load ::::::::::: " +url+ "\n "
        
    i=1
    try :
            text=doc.xpath('//div/div[@class="merch_name"]/a/span/text()')   #//div[i]/div/div[@class="merch_name"]/a/span/text()  this one is for iterattion
            urls_dict=doc.xpath('//div/div/div[@class="merch_name"]/a/@href')
            print urls_dict
            print len(urls_dict)
            urls_dict
    except :
        print url 
        print "xpath wrong" 
    
def main():   
    
    
    f=open('/home/aknauhwar/Desktop/bizrate_text.txt' , "w")
    #departments=Find_Departments()
    #print departments[1]
    
    departments=['appliances']
    
    for department in departments :
        Browse_Category(department)
        
    
    f.close()


main() 

