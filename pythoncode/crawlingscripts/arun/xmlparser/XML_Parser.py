from lxml import etree 
f = etree.parse('/home/aknauhwar/Desktop/catalog_dump_20130205_004017/catalog_ptitle_dump.xml') 
root=f.getroot() 

output = open('/home/aknauhwar/Desktop/catalog_dump_20130205_004017/product____id.txt' , "w")
for tags in root.iter():
   if tags.tag== "product_id" : 
      #print tags.text ,tags.tag
      output.write(tags.text+chr(10)),  #   output.write(tags.text+"\n"),

output.close()