import mechanize 

import socks

import socket


socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5 ,'178.20.55.16' ,22526)

socket.socket =socks.socksocket

br=mechanize.Browser() 

#url = 'http://www.whatismyip.com/'
#url='http://www.whatismyip.com/'

#url='http://www.whatsmyip.org/'
url= 'http://ebay.com/'
#br.addheaders =  {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Connection': 'keep-alive'}
#br.addheadsers =[('user-agent' ,'Mozilla/5.0')]

html = br.open(url)

data =html.read()



print data