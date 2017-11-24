import urllib2
import threading

def countResult(keyword_list, node_id_list, mfr_list, start, end, slr_link, slr_link_withnode, slr_link_withnode_mfr, i):

    filename ='/home/vkthakur/Desktop/shirish-amit-solar/sept/final%s.txt'%(i)
    out_file2 = open(filename, 'w')

    for val in  range(start, end):
        node_id  = node_id_list[val].split('\n')[0]
        key = keyword_list[val].split('\n')[0]
        keyword = key.split('\n')[0].strip()
        keyword = keyword.replace('&' , '%26')
        keyword = keyword.replace('"' , '%22')



        mfr_id = mfr_list[val].split('\n')[0].strip()

        try:
            final_link = slr_link % (keyword)
            string = urllib2.urlopen(final_link).read()
            count1= string.split('numFound=')[1].split(' ')[0]

            final_link = slr_link_withnode % (keyword,node_id)
            string = urllib2.urlopen(final_link).read()
            count2 = string.split('numFound=')[1].split(' ')[0]


            if mfr_id.strip() == '':
                mfr_id = 'None'
                count3 = "Not Applicable"
            else:
                final_link = slr_link_withnode % (keyword,node_id)
                string = urllib2.urlopen(final_link).read()
                count3 = string.split('numFound=')[1].split(' ')[0]

            out_file2.write(key+'|'+node_id+'|'+mfr_id+'|'+count1+'|'+count2+'|'+count3+'\n')
        except Exception:
            print keyword,'\n'
            out_file2.write(key+'|'+node_id+'|'+mfr_id+'|'+"None"+'|'+"None"+'|'+"None"+'\n')



def main():

    slr_link = 'http://sv-solr1.pv.sv.nextag.com/solr/ns01/select?qt=productSearch&kw=%s'
    slr_link_withnode = 'http://sv-solr1.pv.sv.nextag.com/solr/ns01/select?qt=productSearch&kw=%s&nodeId=%s'
    slr_link_withnode_mfr = 'http://sv-solr1.pv.sv.nextag.com/solr/ns01/select?qt=%s&nodeid=%s&mfrid=%s'

    kw   = open('/home/vkthakur/Desktop/shirish-amit-solar/sept/t1')
    node = open('/home/vkthakur/Desktop/shirish-amit-solar/sept/t2')
    mfr  = open('/home/vkthakur/Desktop/shirish-amit-solar/sept/t3')

    keyword_list = kw.readlines()
    node_id_list = node.readlines()
    mfr_list =  mfr.readlines()

    N = len(keyword_list)

    for i in range(N - len(mfr_list)):
        mfr_list.append('\n')

    no_of_thread = 5
    temp = N/no_of_thread
    start=0
    end=temp
    for i in range(no_of_thread):
        t = threading.Thread(target=countResult, args=(keyword_list, node_id_list,mfr_list, start, end, slr_link, slr_link_withnode,slr_link_withnode_mfr, i))
        t.start()
        start+=temp
        end+=temp
        if i==no_of_thread-2:
            end=N

if __name__ == '__main__':
    main()
