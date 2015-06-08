import re


input=open('/home/aknauhwar/Desktop/amazonnov1final.sql', "r")
output1=open('/home/aknauhwar/Desktop/amazonnov1final1.txt', "w")

count=0
lines= input.readlines()

for line in lines :
    uid=line.split("uid=")
    uid1=uid[1]
    url= line.split("/")
    if "exec" in url :
        url1=line.split("%2F")
        
        if "offer-listing" in url1 :
            i=url1.index('offer-listing')
            asin=url1[i+1][0:10] 
            count=count+1
            print asin  , count         
            output1.write('update url_queue set url="http://www.amazon.com/product-reviews/'+'%s"'%(asin)+ ' where uid= %s'%uid1)
        elif "ASIN" in url1 :
            i=url1.index('ASIN')
            asin=url1[i+1][0:10] 
            count=count+1  
            print asin   , count   
            output1.write('update url_queue set url="http://www.amazon.com/product-reviews/'+'%s"'%(asin)+ ' where uid= %s'%uid1)
        else :
            print line    
            
input.close() 
output1.close()
    