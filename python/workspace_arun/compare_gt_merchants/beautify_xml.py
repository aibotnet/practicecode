import xml.dom.minidom
f=open('/home/aknauhwar/Desktop/compare/new.xml' , "w")

xml = xml.dom.minidom.parse('/home/aknauhwar/Desktop/compare/gt_merchant_data_.xml') # or xml.dom.minidom.parseString(xml_string)
pretty_xml_as_string = xml.toprettyxml()

f.write(pretty_xml_as_string)

print "finish"

f.close()

