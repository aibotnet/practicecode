import re


input=open('/home/aknauhwar/Desktop/amazon_url_3.txt', "r")
output1=open('/home/aknauhwar/Desktop/amazon_test_url.txt', "r")
output2=open('/home/aknauhwar/Desktop/amazon_updateurllsql.txt', "w")
output3=open('/home/aknauhwar/Desktop/amazon_updateuidsqll.txt', "w")
flag=0
lines= output1.readlines()

for line in input:
    
    #line=input.readline()
    
        
    
        if flag :
                        if "uid:" in line :
                            id=line.split(":")
                            finalid=id[1]
                            #print finalid
                            output3.write('%s'%(finalid.split()[0])+"\n")
                            flag=0
        if "url:" in line :
            url= line.split(" ")
            i=url[1]
            #print i
            
            
            
            if i not in lines :
                output2.write(i)
                flag=1
                

                            

        
    
        


input.close() 
output1.close()
output2.close()
output3.close()