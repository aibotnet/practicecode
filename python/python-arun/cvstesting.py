import csv
 
f = csv.reader(open("/home/aknauhwar/Desktop/BottomLineDelivery_7.1.csv", "rb"), delimiter = ',')
#f = open('/home/aknauhwar/Desktop/BottomLineDelivery_7.1.csv').readlines()
for l in f:
        print l
        pid,ptitle_id,product_name, product_url , shrt_line,longline = l.split(',')
        shrt_line = shrt_line.rstrip('"').lstrip('"').strip()
        longline = longline.rstrip('"').lstrip('"').strip()
        content = {"body":longline,"bottom_line": shrt_line,"bullets":[]}
        print content 
