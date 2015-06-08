'''from pyquery import PyQuery as pq    
url = "https://www.decide.com/search?q={name}"
name = 'Panasonic 50" ST60'
response = pq(url=url.format(name=name))
print html("a").filter(lambda e: pq(this).text().startswith("Track")).text()'''


import urllib
MGIName = 'Panasonic 50" ST60'
text = urllib.urlopen("https://www.decide.com/search?q="+ MGIName ).read()

print text 

from bs4 import BeautifulSoup as BS
'''protein='Panasonic 50" ST60'
text = requests.get('https://www.decide.com/search?q=' + protein).text'''
soup = BS(text)


'''MGI = soup.find(name='a', onclick="UniProt.analytics('DR-lines', 'click', 'DR-MGI');").text
MGI = MGI[4:]
print protein +' - ' + MGI'''

titleTag = soup.html.head.title
print titleTag 
