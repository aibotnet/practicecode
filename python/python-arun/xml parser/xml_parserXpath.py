from lxml import etree 
f = etree.parse('/home/aknauhwar/Desktop/catalog_dump_20130205_004017/catalog_ptitle_dump.xml') 
root=f.getroot() 

output = open('/home/aknauhwar/Desktop/catalog_dump_20130205_004017/product____id4.txt' , "w")
#for tags in f.xpath('/product/product_id/text()'):
    #if tags.tag== "product_id" : 
    #print tags.text ,tags.tag
     #output.write(tags.text + char(10)),  #   output.write(tags.text+"\n"),
     
     
r=f.xpath('//product_id/text()') #r contains all the selated data as list i think or tuple so using for loop we printed that data

for pid in r :
    output.write(pid +"\n")
     
    
    
output.close()