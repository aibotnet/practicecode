

f = open('rare.txt')

m = {}

for line in f:
    for char in line:
	if char in m.keys():
	    temp = m[char]
	    temp+=1
	    m[char]=temp
	else:
	    m[char]=1

minm = 999999
mkey='4'
for key in m.keys():
    if m[key] ==1:
	print key
