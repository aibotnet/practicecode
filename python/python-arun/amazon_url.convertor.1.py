import re


input=open('/home/aknauhwar/Desktop/amazon_url_3.txt', "r")
output1=open('/home/aknauhwar/Desktop/amazon_test_url.txt', "r")
output2=open('/home/aknauhwar/Desktop/amazon_updateurlsql.txt', "w")
output3=open('/home/aknauhwar/Desktop/amazon_updateuidsql.txt', "w")

lines= output1.readlines()

while(1):
    
    line=input.readline()
    
    
    if(line) :
        if "url:" in line :
            url= line.split(" ")
            i=url[1]
            #print i
            
            
            
            if i not in lines :
                output2.write(i)
                
                line=input.readline()
                line=input.readline()
                if "uid:" in line :
                            id=line.split(":")
                            finalid=id[1]
                            #print finalid
                            output3.write('%s'%(finalid.split()[0])+"\n")
                            

        
    else :
        break
        


input.close() 
output1.close()
output2.close()
output3.close()