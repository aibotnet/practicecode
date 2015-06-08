from lxml import etree
import sys
import time
import pycurl



urls = ["http://www.amazon.com/product-reviews/B007SBGF12","http://www.amazon.com/product-reviews/B008MPMNFK"]
#id('productReviews')/tbody/tr/td[1]/div[1]/div[2]/span[2]/nobr/text()

class Test:
    def __init__(self):
        self.contents = ''

    def body_callback(self, buf):
        self.contents = self.contents + buf

def start_operations():
    #crawl the given webpage taking one url at-a-time from urls


def crawl(uri):
        t = Test()
        c = pycurl.Curl()
        print "Crawling ", uri
        c.setopt(c.URL, uri)
        c.setopt(c.WRITEFUNCTION, t.body_callback)
        c.setopt(pycurl.FOLLOWLOCATION,1)
        c.setopt(pycurl.CONNECTTIMEOUT, 120)
        c.setopt(pycurl.MAXREDIRS, 5)
        c.setopt(pycurl.TIMEOUT, 300)
        c.setopt(pycurl.NOSIGNAL, 1)
        c.perform()
        c.close()

	#Now check if reviews are present in t.contents
		#convert the page into html format so that xpaths can be applied use etree.HTML for this purpose
		#then run loop to extract 10 data sets from the  given page
		#apply the xpaths on the html page tree to extract author,date,review,title,rating for each data set
		#write the data in the text file.
