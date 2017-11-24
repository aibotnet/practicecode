import socks
import socket
def create_connection(address, timeout=None, source_address=None):
    sock = socks.socksocket()
    sock.connect(address)
    return sock
 
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 9050)
 
socket.socket = socks.socksocket
socket.create_connection = create_connection
 
import urllib2
 
try:
    # Check IP
    print urllib2.urlopen("http://almien.co.uk/m/tools/net/ip/").read()
    # Change and check user-agent which is normally Python-Urllib2
    req = urllib2.Request("http://whatismyuseragent.dotdoh.com/")
    req.add_header('User-agent', 'Mozilla 5.10')
    res = urllib2.urlopen(req)
    print res.read()
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.args