file1 = open('/home/aknauhwar/Desktop/not_promoted_ids_08-2013.txt', "r") #creating a file handle
file2=open('/home/aknauhwar/Desktop/datalogparsed.txt',"r") #creating a file handle to read
file3 =open("/home/aknauhwar/Desktop/notunique.txt","w") #creating a file handle to write
fo1= file1.readlines() #read the lines and store in the list
fo2= file2.readlines()

'''for i,j in zip(test1list,test2list): #zip is used to iterate the variablea in 2 lists simultaneoously   
    if i !=j:
        test3filehandle.write("Line Number:" +str(k)+' ')
        test3filehandle.write(i.rstrip("\n") + ' '+ j)
    k=int(k)
    k=k+1;'''
    
    
for line1 in fo1:
     for line2 in fo2 :
         if line1==line2 :
            file3.write(line1 +'\n')
         
         
file1.close()
file2.close()
file3.close()
         

         