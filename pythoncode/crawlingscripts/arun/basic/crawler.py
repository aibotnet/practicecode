#__version__:0.3
'''
Features:

* Flush in real time the success, update, insert files enteries. 
* Upload in real time at the same time to SQS and S3

TODO:
Speed Test
Change the way db updates.

'''
#import sys
import pycurl
import thread
import upload as u
import traceback
import time
import config as cc
from threading import Thread
#dir = sys.argv[1]
success=open("success.log","w+") #list of uids with urls for which we need to set last_fetch=now() and next_fetch="2012-12-12"
failure=open("failure.log","w+") #list of uids with urls for which we need to set last_fetch=now() and is_disabled=1
update=open("update.log","w+")
insert=open("insert.log","w+")
invalid_domains=[]
thread_started=[] 
urls=open("urls").readlines()
class web_page:
    def __init__(self):
        self.contents = '' 

    def body_callback(self, buf):
        self.contents = self.contents + buf

class Crawler(Thread):
        def __init__(self,pid):
                Thread.__init__(self)
                self.crawl()

        def crawl(self):
           try:          
                thread_started.append("ok")
                try:
                  domain, filename, url, product_id = urls.pop().split("\t")
                  domain = domain.strip()
                  t = web_page()
                 if domain not in invalid_domains:
                        filename=int(filename.strip())
                        url=str(url.strip())
                        product_id=int(product_id.strip())
                        c = pycurl.Curl()
                        c.setopt(pycurl.FOLLOWLOCATION, 1)
                        c.setopt(pycurl.MAXREDIRS, 10)
                        c.setopt(pycurl.CONNECTTIMEOUT, 120)
                        c.setopt(pycurl.TIMEOUT, 300)
                        c.setopt(pycurl.NOSIGNAL, 1)
                        c.setopt(pycurl.URL, url)
                        c.setopt(c.WRITEFUNCTION, t.body_callback)
                        time.sleep(2)
                        c.perform()
                        original_url = str(url)
                        final_url = str(c.getinfo(pycurl.EFFECTIVE_URL))
                        if not c.errstr():
                                if(original_url==final_url):
                                        success.write(str(filename)+chr(10))
                                        success.flush()
                                else:
                                        update.write(str(filename)+":::"+final_url+chr(10))
                                        update.flush()
                                        insert.write(str(original_url)+":::"+str(product_id)+chr(10))
                                        insert.flush()
                        else:
                                print "oye"
                                response_code = str(c.getinfo(pycurl.HTTP_CODE))
                                pattern = filename+":::"+response_code+chr(10)
                                print "failure", pattern
                                failure.write(pattern)
                                failure.flush()
                  else:
                        failure.write(str(filename)+chr(10))
                        failure.flush()
                  u.uploader(str(filename), t.contents)

                except Exception, ex:
                        failure.write(str(filename)+chr(10))
                        print "Crawler Failure:", traceback.format_exc()
                        if(ex[0]==6):
                                #pass
                                invalid_domains.append(domain)
                        pass
                try:
                        thread_started.pop()
                except Exception, ex:
                        print "Error:", ex
                        pass
           except Exception, ex:
                print ex
#global c = 1
def run(pid, *args):
                print "Core thread", pid
                while True:
                        t=Crawler(cc.id)
                        t.start()
                        t.join()
                        #c+=1
                        cc.id+=1

x=0
while x<35:
        th="thread no:"+str(x)
        try:
            thread.start_new_thread(run,(th,2))
            x+=1
        except Exception,ex:
            print ex


while len(urls) > 10:
        time.sleep(10)
        pass
print "O got out of the loop", len(urls)

                                                                                                                                                        
