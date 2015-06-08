import lxml.html
from lxml.cssselect import CSSSelector

# get some html
import requests

url="http://www.amazon.com/product-reviews/1591846013"
#url='http://www.abt.com/product/62163/Samsung-UN32EH4003.html#tab2'
r = requests.get(url)

# build the DOM Tree
tree = lxml.html.fromstring(r.text)

# print the parsed DOM Tree
#print lxml.html.tostring(tree)

# construct a CSS Selector
sel = CSSSelector('.reviewText')
#sel=CSSSelector('div~ div+ div div div > a span[style*="font-weight: bold;"]')

#sel=CSSSelector('span+ span b')

#sel=CSSSelector('#rhf_container , div~ div+ div div div a:nth-child(1) span')


#sel=CSSSelector('.pr-comments')

#sel=CSSSelector('.pr-review-main-wrapper')

# Apply the selector to the DOM tree.
results = sel(tree)
print results

print "&&&&$$$$$$$%%%%%"*10

# print the HTML for the first result.
match = results[0]
print match.text
a=lxml.html.tostring(match)

#print a

# get the href attribute of the first result
#print match.get('href')

# print the text of the first result.
#print match.text

# get the text out of all the results
data = [result.text for result in results]
'''print data

for i in data :
    print i
    print "&&&&$$$$$$$%%%%%"*10 '''
 
 
 
 
for i in results :
    a=lxml.html.tostring(i)
    print i.text
    print a
    print "&&&&$$$$$$$%%%%%"*10



     
 
 
 
   