from lxml import etree

file = "/home/aknauhwar/Desktop/Amazon.com: HP Officejet Pro 8600.html" # can be a http URL too
doc = etree.parse(file)

print doc.xpath('.//div/h3/a/span/text()')