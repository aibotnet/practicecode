#from bs4 import BeautifulSoup as BS
#import xml.dom.minidom
#from lxml import etree
#import re
f1=open('/home/aknauhwar/Desktop/compare/output.txt' , "r")

f2=open('/home/aknauhwar/Desktop/compare/clean_output.txt' , "w")

lines=f1.readlines()
count=0
count1=0
for line in lines :
    
    if "merchant_cpc" in line :
        
        l= line.split("|")
        
        if l[3].strip("\n")+".0"==l[4].strip("\n"):
            print l[3] , l[4].strip("\n") , l[3].strip("\n")+".0" , l[4].strip("\n")
            count=count+1
            print "count   :::" ,  count
            pass
        else :
            
            f2.write(line)
            count1=count1+1
            print "count1   :::" ,  count1
        
    elif "merchant_vat_new" in line :
            
        l= line.split("|")
        
        if l[3].strip("\n")+".0"==l[4].strip("\n"):
            print l[3] , l[4].strip("\n") , l[3].strip("\n")+".0" , l[4].strip("\n")
            count=count+1
            print "count   :::" ,  count
            pass
        else :
            
            f2.write(line)
            count1=count1+1
            print "count1   :::" ,  count1
            
            
    elif "merchant_billing_address_email"  in line :
      
        l= line.split("|")
        
        if l[3].strip("\n")=="" and l[4].strip("\n")=="null":
            print l[3] , l[4].strip("\n") , l[3] , l[4].strip("\n")
            count=count+1
            print "count   :::" ,  count
            #break
            pass
        else :
            
            f2.write(line)
            count1=count1+1
            print "count1   :::" ,  count1

    
    else :
        f2.write(line)
        count1=count1+1
        print "count1   :::" ,  count1
        
print "#$%^^^&*"*20

print "count1   :::" ,  count1
print "count   :::"  , count

f1.close()

f2.close()



f3=open('/home/aknauhwar/Desktop/compare/clean_output.txt' , "r")

f4=open('/home/aknauhwar/Desktop/compare/more_clean_output.txt' , "w")


u=[]
liness=f3.readlines()

for i in liness :
    
    if i in u : 
        pass
    
    else :
        
        f4.write(i)
        u.append(i)











     
            
        
        
    
        