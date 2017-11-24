from xml.dom import minidom
import time


fstart(file_path) :
    inputfile =open(file_path , 'r')
    t=time.time() 
    
    output = open('xml.%s.xml'%t , "w")
    i=0
    
    
    for line  in output :
        
        if(!line) :
            output.close() 
            break
            
        if(i<10000) :
            
            fuction(output , line)
            i++
        else :
            
            output.close()
            t=time.time()
            output = open('xml.%s.xml'%t , "w")
            function(output , line)
            i=1
            
            
    input.close()
    
    