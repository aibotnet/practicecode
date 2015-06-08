from xml.dom.minidom import parse


doc =parse('/home/aknauhwar/Desktop/xml41.xml')


value=doc.getElementsByTagName("response ").item(0)

element = doc.createElement("iamgeetingnowhere")
value.insertBefore(element)


print doc.toxml()
