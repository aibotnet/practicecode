#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import re

con = mdb.connect('localhost', 'spider')
output=open('/Arun/sql_url_data', "w")
with con:

    start_row=0
    
    while 1 :
    
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute("select product_id , uid ,url from url_queue where rdomain='com.amazon.www' and is_disabled=0 and metadata like "%july%" limit %d,1000"%(start_row)) 
        
        rows=cur.fetchall()
        
        if not rows :
            break
        
        
        start_row +=1000
        
        for row in rows:
                if not row[url] :
                    break
            
                match=re.search('/ASIN/\w*' , row[url])
                if (match):
                
                    a=re.search('\w\w\w\w\w\w\w\w\w\w',match.group())
                    if a :
                        print 'found', a.group() 
                        if a :
                            
                            s='http://www.amazon.com/product-reviews/'+a.group()
                            output.write('row[product_id]  + row[uid] + s + \n')
                        
                
                    
              
                
                
                match = re.search('/dp/\w*' , row[url]) 
                
                if (match) :
                                        
                    a=re.search('\w\w\w\w\w\w\w\w\w\w',match.group())
                    if a :
                        print 'found', a.group() 
                        if a :
                            
                            s='http://www.amazon.com/product-reviews/'+a.group()
              
                
                
                match = re.search('ASIN=\w*' , row[url])
                
                if match : 
                                        
                    a=re.search('\w\w\w\w\w\w\w\w\w\w',match.group())
                    if a :
                        print 'found', a.group() 
                        if a :
                            
                            s='http://www.amazon.com/product-reviews/'+a.group()
                            output.write('row[product_id]  + row[uid] + s + \n')
                            
                            
                            
                match = re.search('http://www.amazon.com/product-reviews/\d\d\d\d\d\d\d\d\d\d' ,row[url])
                if  match :
                      output.write('row[product_id]  + row[uid] + match.group() + \n')
                      
                      
                      
                      
output.close()

  