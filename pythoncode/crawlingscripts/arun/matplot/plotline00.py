import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


spectrum = np.loadtxt("/home/aknauhwar/Desktop/ebay testing/EbayFinal/list1.txt" ,dtype = int)
plot1 = pl.hist(spectrum , bins=1000 , color ='c')  # will plot a histogram
print type(spectrum)



'''x= np.array(range(20))
y=3+0.5*x + np.random.randn(20)
pl.plot(x,y ,'r*')'''

sum=np.sum(spectrum)
mean=np.mean(spectrum)

y= np.bincount(spectrum)  # for frequency n value
#print y[0]


line=0
print len(np.bincount(spectrum))
for i in np.bincount(spectrum) : 
    #print i
    #pl.axvline(x=line ,ymin=0.25 , ymax=0.75 ,color='r')
    #x=[line , line]
    #y=[0 , i]
    x=[line]
    y=[i]
    pl.plot(x , y , 'ro')
    line +=1
    #break
pl.xlabel('value')
pl.ylabel('frequency')
pl.title('histogram_ebay')
pl.xlim(-10 , 1050)
pl.ylim(-10 , 50)

plot3 =pl.axhline(y=mean, xmin=0, xmax=1000 , color='g')

pl.legend([plot3], ('mean'), 'best', numpoints=1)

pl.show()
    
    
    
    
    
    
    
    
    
    
    
    

