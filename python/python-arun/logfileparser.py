theFile = open('/home/aknauhwar/Desktop/data25log.txt','r')
output =open('/home/aknauhwar/Desktop/datasetwithnormalisederror.txt' ,'w')
FILE = theFile.readlines()
theFile.close()
printList = []
for line in FILE:
    if ('INFO: raw_content id' in line):
        data=line.split(' ')
        
        a=data[9][0:9]
        print a
        
        if(a not in printList):
            printList.append(data[9][0:9])
            output.write(a+'\n')
'''for item in printList:
    print item '''
    
    
print len(printList)
output.close()