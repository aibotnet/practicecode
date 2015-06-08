import csv
list=[]
i=0 
reader = csv.reader(open("/home/aknauhwar/Desktop/BottomLineDelivery_7.1.csv", "r"), delimiter = ',')
for row in reader: 

          
                    '''if ("application" in s) :
                              print row[2][0:10]
                              if(row[2][0:10] not in list):
                                  list.append(row[2][0:10])'''
                                  
                    i=i+1 
                    print row[0]
                    #print row[1]
                    #print row[4]
                    #print row[5]
                    #if(1):
                     #         print row[6]
                              
                              
                              
                    print i 
