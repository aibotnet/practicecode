import re
theFile = open('/home/aknauhwar/Desktop/a.txt','r')
output =open('/home/aknauhwar/Desktop/pititles_aug.txt' ,'w')
FILE = theFile.readlines()
theFile.close()

for line in FILE:
    
            output_string = re.sub(r'[^\d\s-]', '', line)
            output.write(output_string)
    

output.close()