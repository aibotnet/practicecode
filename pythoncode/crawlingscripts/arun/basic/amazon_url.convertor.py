import re


input=open('/home/aknauhwar/Desktop/amazon_url_2.txt', "r")
output1=open('/home/aknauhwar/Desktop/amazon_finalurl_2.txt', "w")
output2=open('/home/aknauhwar/Desktop/amazon_url_uid_1111.txt', "w")

lines= input.readlines()
for line in lines :
    if "url:" in line :
       
        url= line.split("/")
        
        if "dp" in url :
                
                i=url.index('dp')
                asin=url[i+1][0:10]
                
                print asin 
                output1.write('"http://www.amazon.com/product-reviews/'+'%s"'%(asin)+"\n")
                
        else :        
                if  "gp" in url :
                    asin=re.search(r"ASIN=.........." , line)
                    #print line
            
                    if (asin):
                        a=asin.group(0)
                        b=a.split("=")
                        c=b[1]
                        print c
                        output1.write('"http://www.amazon.com/product-reviews/'+'%s"'%(c)+"\n")
                    else :
                        if "offer-listing" in url :
                                            i=url.index('offer-listing')
                                            asin=url[i+1][0:10]
                                            print asin
                                            output1.write('"http://www.amazon.com/product-reviews/'+'%s"'%(asin)+"\n")
                        elif "product" in url :
                            i=url.index('product')
                            asin=url[i+1][0:10]
                            print asin
                            output1.write('"http://www.amazon.com/product-reviews/'+'%s"'%(asin)+"\n")
                                        
                        else :
                                print line
                                url=line.split(" ")
                                a=str(url[1].strip())
                                print a 
                                output1.write('"%s"'%(a)+"\n")
                            
                
                elif 'ASIN' in url :
                    
                        i=url.index('ASIN')
                        asin=url[i+1][0:10]
                        print asin
                        output1.write('"http://www.amazon.com/product-reviews/'+'%s"'%(asin)+"\n")

                    
                    
                else :
                    url=line.split(" ")
                    a=str(url[1].strip())
                    print a 
                    output1.write('"%s"'%(a)+"\n")
                    
                    
                    
        
    if "uid:" in line :
        #continue
        id=line.split(":")
        finalid=id[1]
        print finalid
        output2.write('%s'%(finalid.split()[0])+"\n")
        #print finalid
        









input.close() 
output1.close()
output2.close()