import lxml
from lxml import etree
import urllib2
import urllib
import lxml.html as lh
from bs4 import BeautifulSoup as BS
import requests
import json
import simplejson
import mechanize
import re
import lxml.etree as ET
from lxml.etree import tostring
import lxml.html
from lxml.cssselect import CSSSelector

# get some html
import requests

r = requests.get('http://www.amazon.com/product-reviews/1591846013/')

# build the DOM Tree
tree = lxml.html.fromstring(r.text)

# print the parsed DOM Tree
print lxml.html.tostring(tree)

# construct a CSS Selector
sel = CSSSelector('div.foo li a')

# Apply the selector to the DOM tree.
results = sel(tree)
print results

# print the HTML for the first result.
match = results[0]
print lxml.html.tostring(match)

# get the href attribute of the first result
print match.get('href')

# print the text of the first result.
print match.text

# get the text out of all the results
data = [result.text for result in results]
