from lxml import etree



parser = etree.XMLParser(encoding='utf-8' ,recover =True ,remove_blank_text=True)
tree = etree.parse('/home/aknauhwar/Desktop/beta_reviews_0.xml', parser)
root=tree.getroot()


f = open('/home/aknauhwar/Desktop/reviewws_0.xml', 'w')
f.write(etree.tostring(root, pretty_print=True))
f.close()