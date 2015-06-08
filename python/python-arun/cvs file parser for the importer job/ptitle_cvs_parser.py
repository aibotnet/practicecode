import csv
writer = csv.writer(open("/home/aknauhwar/Desktop/DBQuery43699928-08-06-13_noquotes", "wb"), quoting=csv.QUOTE_NONE)
reader = csv.reader(open('/home/aknauhwar/Desktop/DBQuery43699928-08-06-13.csv' , "rb"), skipinitialspace=True)
writer.writerows(reader)