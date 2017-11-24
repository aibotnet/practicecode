import re

flag=0
input=open('/home/vkthakur/Desktop/amazon_sport_pet_data/amazon_pet_sport', "r")
output1=open('/home/vkthakur/Desktop/amazon_sport_pet_data/amazon_pet_sport_urls.txt', "w")
output2=open('/home/vkthakur/Desktop/amazon_sport_pet_data/amazon_pet_sport_uid.txt', "w")

lines= input.readlines()
for line in lines :
    if "url:" in line :
       
        url= line.split("/")
        
        if "dp" in url :
                
                i=url.index('dp')
                asin=url[i+1][0:10]
                
                #print asin 
                output1.write('"http://www.amazon.com/product-reviews/'+'%s"'%(asin)+"\n")
                flag=1
        else :        
                if  "gp" in url :
                    asin=re.search(r"ASIN=.........." , line)
                    #print line
            
                    if (asin):
                        a=asin.group(0)
                        b=a.split("=")
                        c=b[1]
                        #print c
                        output1.write('"http://www.amazon.com/product-reviews/'+'%s"'%(c)+"\n")
                        flag=1
                    else :
                        if "offer-listing" in url :
                                            i=url.index('offer-listing')
                                            asin=url[i+1][0:10]
                                            #print asin
                                            output1.write('"http://www.amazon.com/product-reviews/'+'%s"'%(asin)+"\n")
                                            flag=1
                        elif "product" in url :
                            i=url.index('product')
                            asin=url[i+1][0:10]
                            #print asin
                            output1.write('"http://www.amazon.com/product-reviews/'+'%s"'%(asin)+"\n")
                            flag=1
                                        
                        else :
                                print line
                                url=line.split(" ")
                                a=str(url[1].strip())
                                #print a 
                                output1.write('"%s"'%(a)+"\n")
                                flag=1
                            
                
                elif 'ASIN' in url :
                    
                        i=url.index('ASIN')
                        asin=url[i+1][0:10]
                        #print asin
                        output1.write('"http://www.amazon.com/product-reviews/'+'%s"'%(asin)+"\n")
                        flag=1

                    
                    
                else :
                    url=line.split(" ")
                    a=str(url[1].strip())
                    #print a 
                    output1.write('"%s"'%(a)+"\n")
                    flag=1
                    
                    
                    
    if flag :
            if "uid:" in line :
                #continue
                id=line.split(":")
                finalid=id[1]
                #print finalid
                output2.write('%s'%(finalid.split()[0])+"\n")
                #print finalid
                flag=0



input.close() 
output1.close()
output2.close()