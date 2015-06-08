import os
os.system('sort -u -n  /home/aknauhwar/Desktop/bline_updated.txt> /home/aknauhwar/Desktop/bline_updatedsorted.txt')
os.system('sort -u -n /home/aknauhwar/Desktop/bline8.txt > /home/aknauhwar/Desktop/bline8sorted.txt')
i1 = open('/home/aknauhwar/Desktop/bline_updatedsorted.txt', 'r')
i2 = open('/home/aknauhwar/Desktop/bline8.txt', 'r')
try:
    d1 = i1.next()
    d2 = i2.next()
    while True:
        if (d1 < d2):
            d1 = i1.next()
        elif (d2 < d1):
            d2 = i2.next()
        else:
            print d1,
            d1 = i1.next()
            d2 = i2.next()
except StopIteration:
    pass