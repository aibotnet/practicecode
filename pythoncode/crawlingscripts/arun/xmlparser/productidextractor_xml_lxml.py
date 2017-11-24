from lxml import etree 
f = etree.parse('/home/aknauhwar/Desktop/catalog_dump_20130205_004017/catalog_ptitle_dump.xml') 
root=f.getroot() 
for tags in root.iter():
   if tags.tag== "product_id" : 
      print tags.text      