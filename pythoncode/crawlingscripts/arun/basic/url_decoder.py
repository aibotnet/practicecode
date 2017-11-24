import urllib 
import re


input=open('/home/aknauhwar/Desktop/Untitled Document 5', "r")
output1=open('/home/aknauhwar/Desktop/Untitled Document 5 urls.txt', "w")
output2=open('/home/aknauhwar/Desktop/Untitled Document 5 ids.txt', "w")

lines= input.readlines()
for line in lines :
    if "url:" in line :
        #print line
        url= line.split(" ")
        #print url[1]
        a= urllib.unquote(url[1]).decode('utf8')
        url=a.split("url=")
        print url[1]
        finalurl=url[1]
        output1.write('"%s"'%(finalurl.split()[0])+"\n")
        
    if "id:" in line :
        id=line.split(":")
        finalid=id[1]
        output2.write('%s'%(finalid.split()[0])+"\n")
        print finalid
        









input.close() 
output1.close()
output2.close()