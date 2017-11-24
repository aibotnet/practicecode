import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


spectrum = np.loadtxt("/home/aknauhwar/Desktop/ebay testing/EbayFinal/list1.txt")
pl.hist(spectrum , bins=1000)  # will plot a histogram


pl.xlabel('value')
pl.ylabel('frequency')
pl.title('histogram_ebay')
pl.xlim(0, 1000)
pl.ylim(0, 1000)

x= np.array(range(20))
y=3+0.5*x + np.random.randn(20)
pl.plot(x,y ,'r*')

print np.sum(spectrum)
print np.mean(spectrum)


count_zero =0
#pl.show()
count_thousand =0
pages=0 
for i in spectrum :
    
    if int(i)==1000 or int(i)==980 :
      count_thousand +=1
      
    d=int(i)/20 
    
    pages +=d
    
    if int(i)==0:
        count_zero +=1
    
    
print pages
print count_thousand
print count_zero
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

