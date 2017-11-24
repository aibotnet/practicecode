import matplotlib.pyplot as plt
import numpy as np
import pylab as pl


x= np.array(range(20))
print x
y=3+0.5*x + np.random.randn(20)
pl.plot(x,y ,'r*')  # will plot graph as given by x , y relationship
pl.xlabel('value')
pl.ylabel('frequency')
pl.title('histogram_ebay')
pl.xlim(0, 1000)
pl.ylim(0, 1000)

pl.show()

