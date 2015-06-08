
#!/usr/bin/python
import re

input=open('/home/aknauhwar/Desktop/input.txt', "r")
output=open('/home/aknauhwar/Desktop/output.txt', "w")

lines= input.readlines()


for a in lines :

#print a

            b=re.sub(r"\t", '', a)
            #print lines 
            #print b
            a=re.sub(r'\([^)]*\)', '\n', b)
            
            c=a.lower()
            
            d=c.strip()
            
            
            
            output.write(d+'\n')




output.close()
input.close()


input2=output=open('/home/aknauhwar/Desktop/output.txt', "r")
output2=open('/home/aknauhwar/Desktop/outputfinal.txt', "w")
line=input2.readlines()

for i in line:
    j=i.strip()
    output2.write(j+"\n")
    
output2.close()
input2.close()

