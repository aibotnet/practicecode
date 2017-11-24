
f1=open('/home/aknauhwar/Desktop/bizrate/output2.txt' , "r")

f2=open('/home/aknauhwar/Desktop/bizrate/output1.txt' , "r")

out1=open('/home/aknauhwar/Desktop/bizrate/output3.txt' , "w")

out2=open('/home/aknauhwar/Desktop/bizrate/output4.txt' , "w")


in1= f1.readlines()

in2= f2.readlines()
list=[]
for i in in1 :
    flag=0
    if str(i.split("|")[0]).strip("\n") not in list :
    
        for j in in2[0:] :
            flag=2
            if  str(i.split("|")[0]).strip("\n") ==str(j.split("|")[0]).strip("\n") :
                #print i.strip("\n")+j.strip("\n")
                out1.write(i.strip("\n")+j.strip("\n")+"\n")
                list.append(str(i.split("|")[0]).strip("\n"))
                flag=1
                break
            
    else : 
        flag=1
            
    if flag==2 :
            out2.write(i)
            
            
        
        
    
    



