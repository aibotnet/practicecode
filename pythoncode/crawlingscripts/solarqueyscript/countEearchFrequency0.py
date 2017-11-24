import urllib2
import threading

def countResult(keyword_list, node_id_list, start, end, slr_link, i):

    filename ='/home/vkthakur/Desktop/shirish-amit-solar/lpet/final%s.txt'%(i)
    out_file2 = open(filename, 'w')

    for val in  range(start, end):
        node_id  = node_id_list[val].split('\n')[0]
        key = keyword_list[val].split('\n')[0]
        keyword = key.split('\n')[0].strip()
        keyword = keyword.replace('&' , '%26')
        keyword = keyword.replace('"' , '%22')

        try:
            final_link = slr_link % (keyword,node_id)
            string = urllib2.urlopen(final_link).read()
            count1= string.split('numFound=')[1].split(' ')[0]

            out_file2.write(key+'|'+node_id+'|'+count1+'\n')
        except Exception:
            print keyword,'\n'
            out_file2.write(key+'|'+node_id+'|'+"None"+'\n')



def main():

    slr_link = 'http://sv-solr1.pv.sv.nextag.com/solr/ns01/select?qt=productSearch&kw=%s&nodeid=%s'

    kw   = open('/home/vkthakur/Desktop/shirish-amit-solar/lpet/t1')
    node = open('/home/vkthakur/Desktop/shirish-amit-solar/lpet/t2')

    keyword_list = kw.readlines()
    node_id_list = node.readlines()

    N = len(keyword_list)


    no_of_thread = 15
    temp = N/no_of_thread
    start=0
    end=temp
    for i in range(no_of_thread):
        t = threading.Thread(target=countResult, args=(keyword_list, node_id_list, start, end, slr_link, i))
        t.start()
        start+=temp
        end+=temp
        if i==no_of_thread-2:
            end=N

if __name__ == '__main__':
    main()
