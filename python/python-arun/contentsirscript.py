input=open('/home/aknauhwar/Desktop/content.txt', "r")
output=open('/home/aknauhwar/Desktop/contentfinalids.txt', "w")
input1=open('/home/aknauhwar/Desktop/xml1.txt', "r")
input2=open('/home/aknauhwar/Desktop/xml2.txt', "r")
input3=open('/home/aknauhwar/Desktop/xml3.txt', "r")
input4=open('/home/aknauhwar/Desktop/xml4.txt', "r")
outputfinal =open('/home/aknauhwar/Desktop/pureids.txt', "w")

lines= input.readlines()
for line in lines :
    
    hashid= line.split("hashId=")
    
    id = hashid[1] 
    output.write(id)
    
input0=open('/home/aknauhwar/Desktop/contentfinalids.txt', "r")


lines= input.readlines()
line in lines :
   for i in input1 :
        
      if '<id>' in i :
        a= i.split(">")
        id = a[1][12]
        if id == lines :
          continue 
          
      elif :
        for i in input2 :
        
            if '<id>' in i :
                a= i.split(">")
                id = a[1][12]
                if id == lines :
                  continue
    
  
  
  
      elif :
        for i in input3 :
        
            if '<id>' in i :
                a= i.split(">")
                id = a[1][12]
                if id == lines :
                  continue
  
      elif:
        for i in input4 :
        
            if '<id>' in i :
                a= i.split(">")
                id = a[1][12]
                if id == lines :
                  continue
                  
                  
  
      else :
          
           outputfinal.write(line)
           
           
           
           
input.close()
output.close()
input1.close()
input2.close()
input3.close()
input4.close()
outputfinal.close()

input0.close()
  
  
  
  
    

      

