from xml.dom import minidom
import time
import sys
sys.path.append("/home/aknauhwar/python")
from apifunctionchanged.py import *

fstart() :

    inputfile =open(file_path , 'r')
    t=time.time() 
    
    output = open('xml.%s.xml'%t , "w")
    i=0
    
    
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
    
    