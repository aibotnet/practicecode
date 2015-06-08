file1 = open('/home/aknauhwar/Desktop/final_count.txt', "r")
fo1= file1.readlines()
n=0
sum=0 
for i in fo1[1:238:2] :
    x=i[0:10] 
    print int(x)
    n=n+1
    sum = sum+int(x)
    print sum
    
    
print sum 
    
