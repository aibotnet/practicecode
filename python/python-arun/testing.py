import csv
i=0 
reader = csv.reader(open("/home/aknauhwar/Desktop/BottomLineDelivery_7.1.csv", "rb"), delimiter = ',')
for l in reader :
        i=i+1 
        
        print l
        for s in l :
                print s+'\n'
                
                
        print i 
        if i>2 :
                break 
        