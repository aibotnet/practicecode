import lxml.html as lh
import urllib2


def ckeck_product_status(url , f):
    try :
        doc = lh.parse(url)
    except:
        print "page unable to load ::::::::::: http://www.bizrate.com/ratings_guide/guide/  \n "
                            
    try :
        List=doc.xpath('.//*[@id="section2"]/div/div/div/a[1]/@href')
        List.extend(doc.xpath('.//*[@id="section3"]/div/div/div/a[1]/@href'))
        List.extend(doc.xpath('.//*[@id="section4"]/div/div/div/a[1]/@href'))

        list_set = set(List)

        for element in list_set:
            try:
                p_url = 'http://aol.nextag.com'+element
                #p_url=p_url.replace('\'','')
                #p_url=p_url.replace(' ','%20')
                response = urllib2.urlopen(p_url)
                doc = lh.parse(response)
                p_list = doc.xpath('.//*[@id="search_results_content_id_0"]/li/div/a/@href')

                if len(p_list) == 0 :
                    raise Exception
               
            except Exception:
                f.write(p_url+'\n')
    except:
        pass


    
def main():   
    f=open('aol_link.txt', "w")
    ckeck_product_status('http://aol.nextag.com/?clickref=invalid_ip', f)
    f.close()


main() 
