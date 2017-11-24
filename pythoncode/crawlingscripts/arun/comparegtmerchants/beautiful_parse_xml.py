from bs4 import BeautifulSoup as BS
import xml.dom.minidom
import re
f1=open('/home/aknauhwar/Desktop/compare/gt_merchant_data_.xml' , "r")

f2=open('/home/aknauhwar/Desktop/compare/gt_merchant_data_old.xml' , "r")

f3=open('/home/aknauhwar/Desktop/compare/new_gt_id.txt' , "r")

f4=open('/home/aknauhwar/Desktop/compare/old_gt_id.txt' , "r")

test=open('/home/aknauhwar/Desktop/compare/test.xml' , "r")


#str1=f1.read()
#str2=f2.read()
str=test.read()
new_id=f3.readlines()
old_id=f4.readlines()





#print str

#x=BS(str1)
#y=BS(str2)
z=BS(str)


#print z.html.body.merchants.findAll("name")[0:]

print z.html.body.merchants.merchant(gt_id="999999999999").findAll("name")




