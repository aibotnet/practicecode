'''import re, urllib
htmlSource = urllib.urlopen("http://www.amazon.com/Samsung-HPT5064-50-Inch-Plasma-HDTV/dp/B000NEFVM0/ref=sr_1_1?ie=UTF8&qid=1380866175&sr=8-1&keywords=Samsung+HPT5064").read(200000)
linksList = re.findall('<a href=(.*?)>.*?</a>',htmlSource)
for link in linksList:
    print link
    
    
print len(linksList)'''
import urllib2
import re
 
#connect to a URL
website = urllib2.urlopen("http://www.amazon.com/Samsung-HPT5064-50-Inch-Plasma-HDTV/dp/B000NEFVM0/ref=sr_1_1?ie=UTF8&qid=1380866175&sr=8-1&keywords=Samsung+HPT5064")
 
#read html code
html = website.read()
 

#links = re.findall('"((http|ftp)s?://.*?)"', html)
links = re.findall('"id('result_1')/h3/a/span"', html)
 
print links 