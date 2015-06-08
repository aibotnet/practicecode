from xml.dom import minidom
import time









t=time.time()
output =open('/home/aknauhwar/Desktop/api.%s.xml'%t ,"w")
#output =open('/home/aknauhwar/Desktop/apitest1.xml' ,"w")                                       
xmldoc = minidom.parse('/home/aknauhwar/Desktop/sample.xml')  
xmldoc                                                               
#<xml.dom.minidom.Document instance at 010BE87C>
#print xmldoc.toxml()
a= xmldoc.toxml()
print a 
output.write(a)
output.close()