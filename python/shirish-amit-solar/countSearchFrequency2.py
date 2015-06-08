import urllib2
import threading
import sys, traceback


def countResult(keyword_list, node_id_list, start, end, slr_link,slr_link1, i):

    filename ='/home/vkthakur/Desktop/shirish-amit-solar/cat/final%s.txt'%(i)
    out_file2 = open(filename, 'w')

    proxy = urllib2.ProxyHandler({'https':'172.23.89.187:3128'})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)

    cnt = 0
    for val in  range(start, end):
        node_id  = node_id_list[val].split('\n')[0]
        key = keyword_list[val].split('\n')[0]
        keyword = key.split('\n')[0].strip()
        keyword = keyword.replace(' ' , '+')
        keyword = keyword.replace('&' , '%26')
        keyword = keyword.replace('"' , '%22')

        final_link = slr_link % (keyword)
        final_link1 = slr_link1 % (keyword,node_id)

        try:
            string = urllib2.urlopen(final_link).read()
            count1= string.split('numFound=')[1].split(' ')[0]
        except Exception:
            count1 = 'None'
            cnt+=1

        try:
            string = urllib2.urlopen(final_link1).read()
            count2= string.split('numFound=')[1].split(' ')[0]
        except Exception:
            cnt+=1
            count2 =  'None'
        out_file2.write(keyword+'|'+node_id+'|'+count1+'|'+count2+'|'+final_link+'|'+final_link1+'\n')

    print cnt



def main():

    slr_link  = 'http://sv-solr2.pv.sv.nextag.com/solr/ns05/select?qt=productSearch&kw=%s&channelid=30199'
    slr_link1 = 'http://sv-solr2.pv.sv.nextag.com/solr/ns05/select?qt=productSearch&kw=%s&nodeId=%s&channelid=30199'

    kw   = open('/home/vkthakur/Desktop/shirish-amit-solar/cat/t1')
    node = open('/home/vkthakur/Desktop/shirish-amit-solar/cat/t2')

    keyword_list = kw.readlines()
    node_id_list = node.readlines()


    N = len(keyword_list)


    no_of_thread = 15
    temp = N/no_of_thread
    start=0
    end=temp
    for i in range(no_of_thread):
        t = threading.Thread(target=countResult, args=(keyword_list, node_id_list, start, end, slr_link, slr_link1, i))
        t.start()
        start+=temp
        end+=temp
        if i==no_of_thread-2:
            end=N

if __name__ == '__main__':
    main()
