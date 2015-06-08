import lxml
from lxml import etree
import urllib
import lxml.html as lh
#from bs4 import BeautifulSoup as BS
#import mechanize
#import json
#import simplejson
#import ast
#import random 
#import decimal
#import time


def Find_Departments():
                        url="http://www.bizrate.com/ratings_guide/guide/"
                        #print "123"
                        list=[]
                        try :
                            doc = lh.parse(url)
                        
                        except:
                            print "page unable to load ::::::::::: http://www.bizrate.com/ratings_guide/guide/  \n "
                            
                        try :
                            
                            #text=doc.xpath('//*[id("search_header")]/table/tbody/tr/td/div/div/ul/li/a/text()')
                            #text=doc.xpath('//li/a/text()')                            
                            #print text
                            text=doc.xpath('//div/div/ul/li/a/@href')
                            #print text 
                            for i in text :
                                if "/ratings_guide/listing/" in i :
                                        #print i
                                        j=i.split("/")[3]
                                        list.append(j)
                                                                
                            return list
                            
                        except :
                            
                            print "NO department inforation check for the xpath \n"
 
 
def  Review_Count(doc , i ): 
    try :
        text=doc.xpath('//div[%d]/div[@class="merch"]/div[@class="all_ratings"]/div/span/span/text()'%i)
        return text[0]
        
    except :
        
        try :
            text=doc.xpath('//div[%d]/div[@class="merch"]/div[@class="all_ratings"]/div/div/span/span/text()'%i)
            return text[0]
            
        except :
            try :
                text=doc.xpath('//div[%d]/div[@class="merch"]/div[@class="all_ratings"]/div[@class="not_rated"]/text()'%i)
                return text[0]
                
            except :
                return "NO reviews not rated yet"
        

def Store_Name(doc , i):
    try :
        store_name=doc.xpath('//div[%d]/div/div[@class="merch_name"]/a/span/text()'%int(i))
        return store_name[0].encode('utf-8')
    except :
        return "NO store member-id found , check manualy"
    
    
def Special_Url (doc , i ):
                    try :
                        url_dict=doc.xpath('//div[%d]/div/div[@class="merch_name"]/a/@href'%int(i))
                        if (url_dict) :
                                store_url1="www."+url_dict[0].split("http%3A%2F%2Fhttp%3A%2F%2F")[1].split("&mid")[0]
                                #print store_url
                                store_url= store_url1.split("%")[0]
                                
                                if "www."  not in store_url :
                                    store_url="www."+store_url
                                else : 
                                    pass
                                
                                #print store_url
                        return store_url 
                    
                    except :             
                        
                        return "NO store URL found,check manually"  

    
def Store_Url(doc , i ):
    
    try :
        url_dict=doc.xpath('//div[%d]/div/div[@class="merch_name"]/a/@href'%int(i))
        if (url_dict) :
                store_url1="www."+url_dict[0].split("www.")[1].split("&mid")[0]
                #print store_url
                store_url= store_url1.split("%")[0]
                
                '''if "www."  not in store_url :
                    store_url="www."+store_url
                else : 
                    pass''' 
                
                #print store_url
        return store_url
    except :
            try :
                url_dict=doc.xpath('//div[%d]/div/div[@class="merch_name"]/a/@href'%int(i))
                if (url_dict) :
                        store_url1="www."+url_dict[0].split("http%3A%2F%2F")[1].split("&mid")[0]
                        #print store_url
                        store_url= store_url1.split("%")[0]
                        
                        if "www."  not in store_url :
                            store_url="www."+store_url
                        else : 
                            pass
                        
                    
                        #print store_url
                if store_url=="www." :
                    store_url= Special_Url(doc , i )
                    
                    
                return store_url
        
        
            except :
                
                return "NO store URL found,check manually"


        
def Member_Id(doc , i):
    try :
        url_dict=doc.xpath('//div[%d]/div/div[@class="merch_name"]/a/@href'%int(i))
        if (url_dict) :
                store_mid=url_dict[0].split("&mid=")[1].split("&catId=")[0]           
                return store_mid
    except :
        return "NO store member-id found , check manualy" 
          
             
def Recent_Review_Count(mid):
    url="http://www.bizrate.com/ratings_guide/cust_reviews__mid--"+mid+".html"
    
    try :
        doc=lh.parse(url)
        text=doc.xpath("//*[@id='store_reviews']/div/div/div/text()")
        count=text[0].split("of ")[1]
        return count
        
    except:
        return "No recent reviews"
            
        
def Total_Stores_on_Page(doc):
    try :
        total=doc.xpath('//div/div/div[@class="merch_name"]/a/span/text()')
        return len(total)
    
    except :
        return 0


def Browse_Category_Rest(category , j , f):
    url="http://www.bizrate.com/"+category+"/ratings_guide/listing__start--"+str(j)+".html"
    
    try :
        doc = lh.parse(url)
        #print "url working"
    except:
        print "page unable to load ::::::::::: " +url+ "\n "
        
    i=1
    total_store_count_on_page= Total_Stores_on_Page(doc)
    
    while(i <= total_store_count_on_page) :
            store_name=Store_Name(doc, int(i))
            #store_url=Store_Url(doc,int(i))                
            #store_review_count=Review_Count(doc , int(i)) 
            member_id=Member_Id(doc , i )

            merchant_info=Merchant_Info(member_id)
            
            count=len(merchant_info)
            
                
            f.write(store_name+"|"+str(count))
            #k=0
            if count>=1 :
                for k in range(0,count):
                    f.write("|"+str(merchant_info[k].encode('utf-8')))
                #print "x"
                        
                
            f.write("\n")
            
            #store_recent_reviews_count=Recent_Review_Count(member_id)
            #f.write(category+"|"+store_name+"|"+store_url+"|"+store_review_count+"|"+store_recent_reviews_count+"\n")
            #print i
            #print store_name
            #print store_url
            #print store_review_count
            #print store_recent_reviews_count
            #print "\n" +"*"*150+"\n"
           
            i= i+1
            
    
    j=j+i-1  
    f.flush()
    
    #print i
    if i<26 :
        return
    #if j >=251 :
        #return     
    Browse_Category_Rest(category , j , f)
    

def Merchant_Info(member_id):
    
    url="http://www.bizrate.com/ratings_guide/merchant_info__mid--"+str(member_id)+".html"
    text_list=[]
    #print url
    try :
        doc=lh.parse(url)
        text=doc.xpath("//div[@class='box merchant-categories']/div[@class='merch-title']/text()")
        #text=doc.xpath("//*[@id='mercchant_info']/div/div/div/text()")
        #print text[0]
        if "Appears In..." in text[0] :
            #print "yes"
            
            try :
                text1=doc.xpath("//div[@class='box merchant-categories']/div[@class='merch-cat']/a/text()")
                #print text1
                #print len(text1)
                return text1
            except :
                #print  "no listed categories"
                return text_list
                
        #return
        #return count
        
    except:
            #print "i failed"
            return text_list  
    
                            
def Browse_Category(category , f):
    
    url="http://www.bizrate.com/"+category+"/ratings_guide/listing/"
    
    try :
        doc = lh.parse(url)
        #print "url working"
    except:
        print "page unable to load ::::::::::: " +url+ "\n "
        
    i=1
    total_store_count_on_page= Total_Stores_on_Page(doc)
    
    while(i <= total_store_count_on_page) :
            store_name=Store_Name(doc, int(i))
            #store_url=Store_Url(doc,int(i))                
            #store_review_count=Review_Count(doc , int(i)) 
            member_id=Member_Id(doc , i )
            #store_recent_reviews_count=Recent_Review_Count(member_id)
            merchant_info=Merchant_Info(member_id)
            
            count=len(merchant_info)
            
                
            f.write(store_name+"|"+str(count))
            #k=0
            if count>=1 :
                for k in range(0,count):
                    f.write("|"+str(merchant_info[k].encode('utf-8')))
                #print "x"
                        
                
            f.write("\n")
            #f.write(store_name+"|"+store_url+"|"+store_review_count+"|"+store_recent_reviews_count+"\n")
            #print i
            #print store_name
            #print store_url
            #print store_review_count
            #print store_recent_reviews_count
            #print "\n" +"*"*150+"\n"
            #return
            i= i+1
            
    #print i 
    f.flush()       
    Browse_Category_Rest(category , i , f)
    
    
def main():   
    
    
    f=open('/home/aknauhwar/Desktop/bizrate_text_finalmerchantinfo4.txt' , "w")
    #departments=Find_Departments()
    #print departments
    #print len(departments)
    #return
    departments=['mature', 'music', 'musical-instruments-accessories', 'office-supplies']
    #return
    for department in departments :
        Browse_Category(department , f)
        
    
    f.close()


main() 

