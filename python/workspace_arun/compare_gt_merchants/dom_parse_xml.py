
import xml.dom.minidom
import re
f=open('/home/aknauhwar/Desktop/compare/gt_merchant_data_old.xml' , "r")



xmldoc = xml.dom.minidom.parse('/home/aknauhwar/Desktop/compare/test.xml') # or xml.dom.minidom.parseString(xml_string)


itemlist = xmldoc.getElementsByTagName('name')


#print xmldoc.toxml()

print xmldoc.merchants