
'''f2=open('/home/aknauhwar/Desktop/bizrate/nextag_merchant.txt.csv' , "r")

f1=open('/home/aknauhwar/Desktop/bizrate/bizrate_merchant.txt' , "r")

out1=open('/home/aknauhwar/Desktop/bizrate/commonname.txt' , "w")

#out2=open('/home/aknauhwar/Desktop/bizrate/difference.txt' , "w")


in1= f1.readlines()
count1=0
count2=0
count=0
in2= f2.readlines()
list=[]
for i in in1 :
        flag=0
        count=count+1
        print "total count=  "+str(count)
        #break
        for j in in2[0:] :
            
            
            
            if "NO store URL found,check manually"  in i : 
                
                if str(i.split("|No store")[0]).strip("\n") in j: 
                    
                    out1.write(str(j.split("|")[0])+"|"+i)
                    #print "yes name"
                    count1=count1+1
                    #print "name count=  "+str(count1)
                    #falg=1
                    #print i
                    break
                else :
                    pass
                
                
            else : 
                
                if  (str(i.split("|www")[1]).split("|")[0]).strip("\n") in j :
                    
                    #print "url in the string !!!!!!!"
                    #count2=count2+1
                    #print "url count= "+str(count2)
                    #print i
                    #out1.write(str(j.split("|")[0])+"|"+i)
                    flag=2
                    break
                
                else :
                    
                    pass
                    
               
        if flag==0 :
            out1.write("|"+i)
        print count1         
            
out1.close()      
     '''
    




































































f1=open('/home/aknauhwar/Desktop/bizrate/common.txt' , "r")

in1= f1.readlines()
count=0
for i in in1 :
    
    m=i.split("|")
    
    if m[0] == "" :
        
        count +=1
        
        print count
        
 
print count
                
                
                
                
                
                
                
                