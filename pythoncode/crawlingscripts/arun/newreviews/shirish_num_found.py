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
from lxml.etree import tostring
from lxml.cssselect import CSSSelector



def url_result(i):
    
        keyword=i.split("|")[0]
        node_id=i.split("|")[1].strip("\n")
        url1="http://sv-solr1.pv.sv.nextag.com/solr/ns01/select?qt=productSearch&kw=%s&nodeId=%s"%(keyword , node_id)
        
        url2="http://sv-solr1.pv.sv.nextag.com/solr/ns01/select?qt=productSearch&kw=%s"%(keyword)
        
        doc1 = lh.parse(url1)
        doc2 = lh.parse(url2)
        a=lh.tostring(doc1)   
        b=lh.tostring(doc2)   
        
        #print a
        p=a.split('numfound=')[1].split(" start")[0]
        q=b.split('numfound=')[1].split(" start")[0]
        
        return p , q
        
        
        

def main(): 
    
    input=open('/home/aknauhwar/Desktop/shirish/pet.txt' , "r")
    output=open('/home/aknauhwar/Desktop/shirish/petlane_final.txt' , "w")
    
    data=input.readlines()
    count=0
    for i in data :
        a,b=url_result(i)
        count +=1
        print count
        i=i.strip("\n")
        output.write(i+"|"+a+"|"+b+"\n")
        
        
        
    input.close()
    output.close()
        
        
        
        
main()
        
        
     