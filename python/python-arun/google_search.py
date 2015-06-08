import re,urllib,urllib2
class GoogleHarvester:
    re_links = re.compile(r'<a class=l href="(.+?)"',re.IGNORECASE|re.DOTALL)
    def __init__(self):
            pass
    def harvest(self,terms):
        '''Searchs Google for these terms. Returns only the links (URL).
        Input: terms (string) -- one or several words to search.
        Output: A list of urls (strings).
        Duplicates links are removed, links are sorted.
        Example: print GoogleHarvester().harvest('monthy pythons')
        '''
        print "Google: Searching for '%s'" % terms
        links = {}
        currentPage = 0
        while True:
                    print "Google: Querying page %d (%d links found so far)" % (currentPage/100+1, len(links))
                    address = "http://www.google.com/search?q=%s&num=100&hl=en&start=%d" % (urllib.quote_plus(terms),currentPage)
                    request = urllib2.Request(address, None, {'User-Agent':'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1)'} )
                    urlfile = urllib2.urlopen(request)
                    page = urlfile.read(200000)
                    urlfile.close()
                    for url in GoogleHarvester.re_links.findall(page):
                        links[url] = 0
                    if "</div>Next</a></table></div><center>" in page: # Is there a "Next" link for next page of results ?
                        currentPage += 100 # Yes, go to next page of results.
                    else:
                        break
        # No, break out of the while True loop.
        print "Google: Found %d links." % len(links)
        return sorted(links.keys())
        
        
links = GoogleHarvester().harvest('amazon')
open("/home/aknauhwar/Desktop/links.txt","w+b").write("\n".join(links))

