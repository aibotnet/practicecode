import re

input=open('/home/aknauhwar/Desktop/input.txt', "r")
output=open('/home/aknauhwar/Desktop/output.txt', "w")

lines= input.readlines()
b=re.sub(r"\\t", '', str(lines))
#print lines 
#print b
a=re.sub(r'\([^)]*\)', '\n', b)

c=re.sub(r"\\n", '', a)

print type(c) 
print c

d=c.split("\n")

#print d






'''s = '   A  bd cde   '
s=s.strip()
print s

s =s.lower()
print s
'''