fo = open("/home/aknauhwar/Desktop/test.txt", "r")
print "Name of the file: ", fo.name
#print len(fo.readlines())

while 1 :
    line = fo.readline()
    if line :
        print "Read Line: %s" % (line)

    else :break
    
print len(fo.readlines())

    

fo.close()