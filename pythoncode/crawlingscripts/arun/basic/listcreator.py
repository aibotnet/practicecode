output =open('/home/aknauhwar/Desktop/datalogparsed.txt' ,'r')
file  = output.readlines()
input=open('/home/aknauhwar/Desktop/datalogparsedlist.txt' ,'w')
printList = []
for line in file  :
            a= line[0:9]
            printList.append(line[0:9] )
            input.write(a+',')




print printList 

input.close()