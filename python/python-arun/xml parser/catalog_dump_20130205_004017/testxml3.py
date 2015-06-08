
fo= open("/home/aknauhwar/Desktop/p_id.txt" ,"r")
line = fo.readlines()
for i in line[0:]:
    
    
    
    print i
    
    
    
    
    

fo.close() 



'''import fileinput

fo=fileinput.input(["/home/aknauhwar/Desktop/p_id.txt"])

print type(fo)
print type(fileinput.input(["/home/aknauhwar/Desktop/p_id.txt"]))
for line in  fo :                               # fileinput.input(["/home/aknauhwar/Desktop/p_id.txt"]):
     print line 
     break 
'''
   