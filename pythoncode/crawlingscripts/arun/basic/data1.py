from contextlib import nested
from decorator import decorator
import os.path
import string
from urlparse import urljoin
from xml.dom.minidom import Document

from paste import httpexceptions
from paste.deploy.converters import asbool
from pylons import tmpl_context as c, config, request, response, url

from veetwo.lib import affiliates, constants, emailnotification, helpers as h, product_lib, snippets as snippets_lib, topics
from veetwo.lib.base import BaseController, releasing
from veetwo.lib.cache import cache_response
from veetwo.models.navigation import NAVIGATION_CATEGORY_ROOT_ID
from veetwo.lib.search import solr as solr_search
from veetwo.lib.utils.xml import append_new_element
from veetwo.models import db, betawize,betasite #for api machine for other m/c change to wize and site n do corresponding changes

from xml.dom import minidom
import time
import sys
from apifunctionchanged.py import *

assert len(sys.argv) > 1, "Pass directory name as a parameter"
file_path= sys.argv[1]



def start_Operations():
    betawize.init("mysql://root@127.0.0.1:3306/betawize?charset=utf8")   #wize2 change dns too
    betasite.init("mysql://root@127.0.0.1:3306/betasite?charset=utf8")#site
    print "Connection set-up with DB"
    
    inputfile =open(file_path , 'r')
    t=time.time() 
    
    output = open('xml.%s.xml'%t , "w")
    i=0


    with nested(betawize.Session(autoflush=False, autocommit=False),betasite.Session(autoflush=False, autocommit=False)):
	#Now start running the loop for 10K products each
	
	
                    
            for line  in output :
                
                if(!line) :
                    output.close() 
                    break
                    
                if(i<10000) :
                    
                    apifunctionchanged._0_1_get_product_reviews(output , line)
                    i++
                else :
                    
                    output.close()
                    t=time.time()
                    output = open('xml.%s.xml'%t , "w")
                    apifunctionchanged._0_1_get_product_reviews(output , line)
                    i=1
                    
                    
            input.close()
            
            
start_Operations() 
            
            
	
	
	
	
	
	
	
	