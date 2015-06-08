#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb as mdb
import re

con = mdb.connect('10.192.169.139','','', 'wize2')
output=open('/root/Arun/ptitles_wize2data', "w")
with con:

   #start_row=0
   # i=1 
    while 1  :
        #global i
        #i=0 
        cur = con.cursor(mdb.cursors.DictCursor)
        cur.execute(" select distinct products.nextag_ptitle_id ,products.nextag_product_id from products where exists(select * +\
        from reviews where products.nextag_product_id = reviews.product_id") ;
        
        
        rows=cur.fetchall()

        if not rows :
            break


        #start_row +=1000

        for row in rows:
                if not row :
                        break
                        
                else :
                    
                    output.write(str(row['products.nextag_product_id'])+'$     '  +str(row['products.nextag_ptitle_id']) +'$     ' +s+'\n')

                        


output.close()
                        
                        
                        
                        
                        
                        
                        
                        
                        
