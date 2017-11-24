from xml.dom import minidom   
output =open('/home/aknauhwar/Desktop/sampletest.xml' ,"w")                                       
xmldoc = minidom.parse('/home/aknauhwar/Desktop/sample.xml')  
xmldoc                                                               
#<xml.dom.minidom.Document instance at 010BE87C>
#print xmldoc.toxml()
a= xmldoc.toxml()
print a 
output.write(a)
output.close()